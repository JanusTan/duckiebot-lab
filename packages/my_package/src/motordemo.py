#!/usr/bin/env python
import os
import rospy
from duckietown import DTROS
from std_msgs.msg import String
from duckietown_msgs.msg import WheelsCmdStamped, BoolStamped, LEDPattern
from duckietown_msgs.srv import SetCustomLEDPattern, ChangePattern

class MyNode(DTROS):
    def __init__(self, node_name):
        # initialize the DTROS parent class        
        super(MyNode, self).__init__(node_name=node_name)       
        # construct publisher
        name = 'duckiebot7/wheels_driver_node/wheels_cmd'         
        self.wheelpub = rospy.Publisher(name, WheelsCmdStamped, queue_size=1) 


    

    def run(self):
        while not rospy.is_shutdown():
            # Delayed Start
            rospy.sleep(4.)
            

                
            # Drive Forward
            msg = WheelsCmdStamped()
            msg.header.stamp = rospy.get_rostime()
            msg.vel_left = 0.6
            msg.vel_right = 0.6
            self.wheelpub.publish(msg)
            rospy.sleep(2.)

            # Left Turn
            msg.vel_left = -0.2
            msg.vel_right = 0.2
            self.pub.publish(msg) 
            rospy.sleep(1.5)

            # Forward
            msg.vel_left = 0.5
            msg.vel_right = 0.5
            self.pub.publish(msg) 
            rospy.sleep(2.)   

            msg.vel_left = 0.0
            msg.vel_right = 0.0
            self.pub.publish(msg)
            rospy.sleep(4.)

    def onShutdown(self):
        rospy.is_shutdown()

        # Stop Wheels
        msg = WheelsCmdStamped()
        msg.header.stamp = rospy.get_rostime()
        msg.vel_left = 0.0
        msg.vel_right = 0.0
        self.wheelpub.publish(msg)
        rospy.sleep(5.)

      

if __name__ == '__main__':    
    # create the node    
    node = MyNode(node_name='motordemo')    
    # run node    
    node.run()    
    # keep spinning    
    rospy.spin()
