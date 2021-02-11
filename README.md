# extract_trajectory

## Brief

<a href="https://www.python.org/downloads/"><img alt="Python 2.7" src="https://img.shields.io/badge/python-2.7-yellow.svg" /></a>
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-red.svg)](https://www.python.org/downloads/) [![support level: community](https://img.shields.io/badge/support%20level-community-lightgray.png)](http://wiki.ros.org/Industrial)


> Extract trajectory with topics that contain containing nav_msgs/Odometry.

## Input file structure

- bagfiles with topics that contain ```nav_msgs/Odometry``` messages.

Check **.bag**:

```
rosbag info <file.bag>

...
types:  nav_msgs/Odometry
topics: /integrated_to_init    
...
```

## Output file structure

- trajectory.txt

```
timestamp tx ty tz qx qy qz qw
```

* **timestamp** (float) gives the number of seconds.
* **tx ty tz** (3 floats) give the position, where t is the translation vector.
* **qx qy qz qw** (4 floats) give the orientation, where q is a quaternion describing the rotation.

**Note:** with each value separated by a space.

More info: https://vision.in.tum.de/data/datasets/rgbd-dataset/file_formats


## Run the package

- Rename the topic [/integrated_to_init](https://github.com/cristianrubioa/extract_trajectory/blame/main/src/extract_data.py#L38) and rename the file [trajectory.txt](https://github.com/cristianrubioa/extract_trajectory/blame/main/src/extract_data.py#L48)

- Extract trajectory:
```
python extract_data.py
```

## Trajectory Evaluation

- Plot trajectory: ```python plot_data.py <file.txt>```
```
python plot_data.py trajectory.txt
```

With evo kit: [MichaelGrupp/evo](https://github.com/MichaelGrupp/evo)
```
evo_traj tum trajectory.txt -p --plot_mode=xz
```



