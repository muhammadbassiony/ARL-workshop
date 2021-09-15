#! /usr/bin/env python3
import rospy
from std_msgs.msg import String
import numpy as np


class Bicycle():
    def __init__(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0
        
        self.L = 2
        self.lr = 1.2
        self.w_max = 1.22
        
        self.sample_time = 0.01
        
    def reset(self):
        self.xc = 0
        self.yc = 0
        self.theta = 0
        self.delta = 0
        self.beta = 0

    # def printState():
    #     print()

    def step(self, v, w):
        
        t = 10e-3
        
        if w > 0:
            w = min(w, self.w_max)
        else:
            w = max(w, -self.w_max)
        
        
        
        xc_dot = v * np.cos(self.theta + self.beta)
        yc_dot = v * np.sin(self.theta + self.beta)
        theta_dot = (v / self.L) * (np.cos(self.beta) * np.tan(self.delta))
        delta_dot = w
        self.beta = np.arctan(self.lr * np.tan(self.delta) / self.L)
        
        self.xc += xc_dot * t
        self.yc += yc_dot * t
        self.theta += theta_dot * t 
        self.delta += delta_dot * t

# -----------------------------------------

model = Bicycle()

def callback(data):
    # rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
    
    v, w = data.data.split(", ")
    print(v)
    print(w)

    v = float(v)
    w = float(w)

    model.step(v, w)
    print(model.xc, model.yc)
    


def listener():
    
    rospy.init_node('model_sub', anonymous=True)

    rospy.Subscriber("model_data", String, callback)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
