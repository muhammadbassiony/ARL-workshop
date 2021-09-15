#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)

    name, age, height = data.data.split(",")
    # print(name)
    # print(age)
    # print(height)
    talker(name, age, height)


    
def listener():

    rospy.init_node('data_processing', anonymous=True)

    rospy.Subscriber("raw_data", String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()




def talker(name, age, height):

    # rospy.init_node('data_processing', anonymous=True)
    rate = rospy.Rate(1) # 1hz

    while not rospy.is_shutdown():
        # hello_str = "name:Rose, age:20, height:170"
        # rospy.loginfo(hello_str)
        name_pub.publish(name)
        rospy.loginfo(name)

        age_pub.publish(age)
        rospy.loginfo(age)

        height_pub.publish(height)
        rospy.loginfo(height)
        
        rate.sleep()


if __name__ == '__main__':
    name_pub = rospy.Publisher('name', String, queue_size=10)
    age_pub = rospy.Publisher('age', String, queue_size=10)
    height_pub = rospy.Publisher('height', String, queue_size=10)

    listener()