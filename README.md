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
1497705851.35 -0.0113885076717 -1.09817642624e-06 0.00693530961871 6.2331225421e-06 -0.000854817389752 6.7346687524e-06 0.999999634601
1497705851.46 -0.0229631382972 -1.20041595437e-05 0.0135130966082 1.53998456449e-05 -0.000962992962284 6.34903556518e-06 0.999999536183
1497705851.56 -0.0341137200594 2.92173426715e-05 0.00636271294206 2.10170615833e-05 -0.000765090764832 9.8156363075e-06 0.999999707049
1497705851.67 -0.0281987823546 4.50947554782e-05 0.0080398786813 2.69942153636e-05 -0.000359260024172 5.08400885803e-06 0.999999935089
1497705851.77 -0.0341357178986 3.85829880543e-05 0.00421400088817 2.95107239816e-05 -0.000356331106573 8.57329788175e-07 0.999999936078
```
Check the file with ```head -n5 trajectory.txt```

- *File format*:
```
timestamp tx ty tz qx qy qz qw
```

* **timestamp** (float) gives the number of seconds.
* **tx ty tz** (3 floats) give the position, where t is the translation vector.
* **qx qy qz qw** (4 floats) give the orientation, where q is a quaternion describing the rotation.

**Note:** with each value separated by a space.

More info: https://vision.in.tum.de/data/datasets/rgbd-dataset/file_formats



## Run the package

- Rename the topic ['/integrated_to_init'](https://github.com/cristianrubioa/extract_trajectory/blame/main/src/extract_data.py#L38) and rename the file ['trajectory.txt'](https://github.com/cristianrubioa/extract_trajectory/blame/main/src/extract_data.py#L48)

- Extract trajectory with:
```
python extract_data.py
```

- Play existing bag files:
```
rosbag play <file.bag>
```

## Plot trajectory

**Note:** trajectory.txt is a sample file generated from extract_data.py

- With plot_data.py: ```python plot_data.py <file.txt>```
```
python plot_data.py trajectory.txt
```
<img src = "https://raw.githubusercontent.com/cristianrubioa/extract_trajectory/main/img/plot_data.png" width = "300">

With evo kit: [MichaelGrupp/evo](https://github.com/MichaelGrupp/evo)
```
evo_traj tum trajectory.txt -p --plot_mode=xz
```
<img src = "https://raw.githubusercontent.com/cristianrubioa/extract_trajectory/main/img/evo.png" width = "230"><img src = "https://raw.githubusercontent.com/cristianrubioa/extract_trajectory/main/img/evo_1.png" width = "230"><img src = "https://raw.githubusercontent.com/cristianrubioa/extract_trajectory/main/img/evo_2.png" width = "230">





