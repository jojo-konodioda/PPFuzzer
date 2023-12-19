# PPFuzzer 


## Setup

- Install `Ego-Planner` following the official instructions and make sure it is installed in your home directory:  

  &emsp;<https://github.com/ZJU-FAST-Lab/ego-planner/tree/master>

- Execute the official example to ensure `Ego-Planner` is correctly installed.

- Clone the source code:

```javascript
git clone PPFuzzer
cd PPFuzzer/src
```


## Replay 

- Execute `replay.py` to replay vulnerability scenario #1:


## Replay
- Execute `replay.py` to setup the vulnerability scenario, the parameter  `1` indicates to replay vulnerability type #1.
```javascript
python3 replay.py 1
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
python3 replay.py index_number_of_type
```