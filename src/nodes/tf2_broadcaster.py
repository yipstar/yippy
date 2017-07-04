#!/usr/bin/env python  
import rospy

# Because of transformations
import tf

import tf2_ros
import geometry_msgs.msg


if __name__ == '__main__':
    rospy.init_node('tf_yippy')

    broadcaster = tf2_ros.StaticTransformBroadcaster()

    t = geometry_msgs.msg.TransformStamped()
    t.header.stamp = rospy.Time.now()
    t.header.frame_id = "base_link"
    t.child_frame_id = "base_laser"

    t.transform.translation.x = 0
    t.transform.translation.y = 0
    t.transform.translation.z = .125
    q = tf.transformations.quaternion_from_euler(0, 0, 0)
    t.transform.rotation.x = q[0]
    t.transform.rotation.y = q[1]
    t.transform.rotation.z = q[2]
    t.transform.rotation.w = q[3]

    broadcaster.sendTransform(t)

    rospy.spin()
