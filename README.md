# yippy

# installing on raspberry pi 3
- install from gero disk image, gives ubuntu mate and ros kinetic preinstalled.
- fix language and keyboard (PITA)
- backup and remove /etc/rc.local (starts all gero stuff)

- ROS deps

- sudo apt install ros-kinetic-opencv3
- sudo apt install ros-kinetic-cv-bridge
- sudo apt install ros-kinetic-video-stream-opencv
- sudo apt install ros-kinetic-image-pipeline
- sudo apt install ros-kinetic-vision-opencv
- sudo apt install ros-kinetic-image-transport
- sudo apt install ros-kinetic-compressed-depth-image-transport
- sudo apt install ros-kinetic-compressed-image-transport

To launch the camera stream
roslaunch image_stream_opencv camera.launch

To view:
rosrun image_view image_view image:=/camera/camera_raw compressed

