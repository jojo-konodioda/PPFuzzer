# PPFuzzer

- The <font color=blue>videos</font> directory shows the video record about vulnerabilities.

- The <font color=blue>src</font> directory is the code for replaying vulnerabilities.

- The <font color=blue>vul_scenarios</font> directory contains the point cloud files of scenarios that trigger vulnerabilities of path planners.

- The <font color=blue>parameters</font> directory contains the parameters setting of path planners.

## Setup

- Install `Ego-Planner` following the official instructions and make sure it is installed in your home directory:  

  &emsp;<https://github.com/ZJU-FAST-Lab/ego-planner/tree/master>

- Execute the official demo to ensure `Ego-Planner` is correctly installed.

- Clone the source code:

```javascript
git clone PPFuzzer
cd PPFuzzer/src
```


## Replay 

- Execute `replay.py` to replay vulnerability type #1 scenario:
```javascript
python3 replay.py type1
```

- Open another new terminal and launch `rviz`:
```javascript
roslaunch ego_planner rviz.launch
```

- Open another new terminal and launch `Ego-Planner`:
```javascript
roslaunch ego_planner run_in_sim.launch
```

- Similarly, to replay other vulnerability types, execute:
```javascript
python3 replay.py folder_name
# for example:
python3 replay.py type2 (replay vulnerability type #2 scenario)
roslaunch ego_planner rviz.launch (launch simulator GUI in another new terminal)
roslaunch ego_planner run_in_sim.launch (launch Ego-Planner in another new terminal)
```

## Note
- As path planners use fast search algorithms (e.g. A*, RRT*) which randomly search a path, therefore the vulnerability may not trigger every time you run the path planner. If the vulnerability is not triggered, please **retry**.

- We simulated a 0.3 m wheelbase drone, thus a collision is assumed when the drone center reaches an obstacle distance within 0.15 m, equivalent to half the wheelbase length.

- The code is tested in `ubuntu 20.04`.
