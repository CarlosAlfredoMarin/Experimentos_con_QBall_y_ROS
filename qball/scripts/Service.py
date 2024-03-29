#!/usr/bin/env python3

import rospy 
import rospkg 
from gazebo_msgs.msg import ModelState 
from gazebo_msgs.srv import SetModelState

def main():
    rospy.init_node('set_pose')

    state_msg = ModelState()
    state_msg.model_name = 'qball'
    state_msg.pose.position.x = 2
    state_msg.pose.position.y = 2
    state_msg.pose.position.z = 6
    state_msg.pose.orientation.x = 0
    state_msg.pose.orientation.y = 0
    state_msg.pose.orientation.z = 0
    state_msg.pose.orientation.w = 0

    while not rospy.is_shutdown():
        rospy.wait_for_service('/gazebo/set_model_state')
        try:
            set_state = rospy.ServiceProxy('/gazebo/set_model_state', SetModelState)
            resp = set_state( state_msg )
        except rospy.ServiceException:
            print("Service call failed")

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass
