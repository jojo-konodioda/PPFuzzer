# PPFuzzer
## Setup
- Install `Ego-Planner` following the official instructions and make sure it installed in you home directory:
&emsp; <https://github.com/ZJU-FAST-Lab/ego-planner/tree/master>

- Make sure the `Ego-Planner` is correctly installed by executing the official example.

- Clone our source code.

```javascript
git clone PPFuzzer
cd PPFuzzer/src
```
## Replay
- Execute  `replay.py` to generate the vulnerability scenario, the parameter  `1` indicates to replay vulnerability type #1.
```javascript
python3 replay.py 1
```

- Open another new terminal and launch `rviz`.
```javascript
roslaunch ego_planner rviz.launch
```

- Open another new terminal and launch `Ego-Planner`.
```javascript
roslaunch ego_planner run_in_sim.launch
```