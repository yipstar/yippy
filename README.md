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

- sudo apt-get update
- sudo apt-get install gpsd gpsd-clients python-gps

https://learn.adafruit.com/adafruit-ultimate-gps-hat-for-raspberry-pi/use-gpsd
- edited /etc/defaults/gpsd set the following so it uses proper device on boot:
GPSD_OPTIONS="/dev/ttyUSB0"
GPSD_SOCKET="/var/run/gpsd.sock"

# TODO: finish setting up /fix topic messages:
http://wiki.ros.org/gpsd_client/Tutorials/Getting%20Started%20with%20gpsd_client

Setup Scanse Lidar
https://github.com/scanse/sweep-ros
- install libsweep as described, then clone sweep-ros and catkin_make it
