# extract_trajectory

## Brief


> Extract trajectory with topics that contain containing nav_msgs/Odometry.

## Input file structure

- bagfiles with topics that contain ```nav_msgs/Odometry``` messages

Check .bag:

```
rosbag info <file.bag>

...
types:  nav_msgs/Odometry
topics: /aft_mapped_to_init
...
```

## Output file structure

- trajectory.txt

```
timestamp tx ty tz qx qy qz qw
```

More infos: https://vision.in.tum.de/data/datasets/rgbd-dataset/file_formats


## Run the package


```
python code.py
```

