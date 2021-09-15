#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    name, age, height = data.data.split(",")
    print(name)
    print(age)
    print(height)
    
def listener():

    rospy.init_node('data_processing', anonymous=True)

    rospy.Subscriber("raw_data", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()