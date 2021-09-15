#!/usr/bin/env python3
# license removed for brevity

import rospy
from std_msgs.msg import String
import numpy as np


path = '../xdata.txt'
 
def talker():
    pub = rospy.Publisher('model_data', String, queue_size=10)
    rospy.init_node('bicycle_model_pub', anonymous=True)
    rate = rospy.Rate(0.001)# 1hz

    

    while not rospy.is_shutdown():

        f = open(path, "r")
        for x in f:
            rospy.loginfo(x)
            pub.publish(x)


        # hello_str = "name:Rose, age:20, height:170"
        # rospy.loginfo(hello_str)
        
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass