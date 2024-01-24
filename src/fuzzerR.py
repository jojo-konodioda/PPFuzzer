from Modules import scenario_mutatorR
from Modules import scenario_executor
from Modules import misbehaviour_detector
from Utils import pcl_parser
from Metrics import mindist
import time
from Utils import scenario_loader
from Utils import logger
import sys
from Utils import pool_manager

class Fuzzer:
    def __init__(self, nog = 16, nop = 8, nomu = 3, execution_time = 25, scenarios = None, log_dir = None, scenario_pool = None):
        self.logger = logger.Logger(log_dir = log_dir, nog = nog, nop = nop, nomu = nomu, execution_time = execution_time)

        self.nog = self.logger.nog
        self.nop = self.logger.nop
        self.nomu = self.logger.nomu
        self.execution_time = self.logger.execution_time
        self.round = self.logger.get_round()

        # random generated scenario pool, used for generate scenario for newly started fuzzing or substitute the scenario which trigger misbehaviors
        self.scenario_pool = scenario_pool

        # if the fuzzing is newly started, load from the pool and save
        if self.logger.is_new_log:
            assert self.scenario_pool != None, "A scenario pool is needed"
            self.scenarios = self.scenario_pool.get_scenarios(self.nog)
            self.logger.save_scenarios(self.scenarios)
            self.logger.save_info()

        # if the fuzzing is not newly started, load from history
        else:
            self.scenarios = self.logger.load_scenarios()

        self.mutator = scenario_mutatorR.Mutator(nog = self.nog, nop = self.nop, nomu = self.nomu, scenario_pool = scenario_pool)

    def run(self):
        self.scenarios = self.logger.load_scenarios()
        print('Round: {}, running'.format(self.round))
        print('=======================================')
        # executor and detector
        time1 = time.time()
        misbehaviours_list = self.execute_and_detect()
        print(misbehaviours_list)
        print(time.time()-time1)

        # save misbehaviours and add scenarios without misbehaviours for mutation
        scenarios_for_mutation = []
        for i, misbehaviour in enumerate(misbehaviours_list):
            if misbehaviour != None:
                self.logger.save_misbehaviour(self.scenarios[i], misbehaviour, i)
            else:
                scenarios_for_mutation.append(self.scenarios[i])

        # None metrics for mutation

        # Mutator
        self.mutator.set_input_scenarios(scenarios_for_mutation)
        self.mutator.mutate()
        self.scenarios = self.mutator.get_mutated_scenarios()

        # the scenarios index of next round
        self.round = self.round + 1
        self.logger.round_add()

        # Save info of this round
        self.logger.save_scenarios(self.scenarios)
        self.logger.save_info()
        print('=======================================')

    # execute the simulation meanwhile detect misbehaviours, logging the ds
    def execute_and_detect(self):
        misbehaviours = []
        for index, scenario in enumerate(self.scenarios):
            print('Round: {}, scenario: {}, running'.format(self.round, index))
            print('------------------------------------------')
            executor = scenario_executor.Executor()
            detector = misbehaviour_detector.Detector(dest_point = [6.5,-5,1.5])

            executor.set_scenario(scenario)
            executor.start()
            detector.start()
            time.sleep(self.execution_time)
            detector.stop()
            executor.stop()

            scenario.DS = detector.get_ds()
            
            misbehaviours.append(detector.report())
            print('------------------------------------------')

        return misbehaviours


if __name__ == '__main__':
    sp = pool_manager.PoolManager('data/seed/room1/1')
    fuzzer = Fuzzer(log_dir = sys.argv[1], scenario_pool = sp)

    while fuzzer.round < 16:
        print("Executing: ", sys.argv[0], " ", sys.argv[1])
        fuzzer.run()
    print('======================================')
    print("Complete: ", sys.argv[0], " ", sys.argv[1])
    print('======================================')
