#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

x1 = 0
x2 = 0
y1 = 0
y2 = 0
theta1 = 0
theta2 = 0

def poseCallback1(pose_message):
	global x1
	global y1, theta1
	x1 = pose_message.x
	y1 = pose_message.y
	theta1 = pose_message.theta

def poseCallback2(pose_message):
	global x2
	global y2, theta2
	x2 = pose_message.x
	y2 = pose_message.y
        theta2 = pose_message.theta

def move():
	rospy.init_node('turtle_revolve', anonymous=True)
	velocity_publisher = rospy.Publisher('/turtle2/cmd_vel', Twist, queue_size=10)
	position_publisher = rospy.Publisher('/turtle2/pose', Pose, queue_size=10)
	vel_msg = Twist()
	pos_msg = Pose()

	print("Let's move the turtle")
	radius = 1
	angular_velocity = 0.2
	vel_msg.angular.z = 0
	vel_msg.angular.y = 0
	vel_msg.angular.x = 0 
	vel_msg.linear.x = 0.5
	vel_msg.linear.y = 0
	vel_msg.linear.z = 0
	while not rospy.is_shutdown():
		while(math.sqrt((x1-x2)**2 + (y1-y2)**2)>=2):
			#if(math.sqrt((x1-x2)**2 + (y1-y2)**2)>=2):
			velocity_publisher.publish(vel_msg)
		while(theta2<1.1):
			vel_msg.angular.z = 0.25
			vel_msg.linear.x = 0.0
			velocity_publisher.publish(vel_msg)
		while(math.sqrt((x1-x2)**2 + (y1-y2)**2)<2):
			vel_msg.angular.z = 0.0
			vel_msg.linear.x = 0.5
			velocity_publisher.publish(vel_msg)
		while(theta2>0):
			vel_msg.angular.z = - 0.25
			vel_msg.linear.x = 0.0
			velocity_publisher.publish(vel_msg)
		while(x2<8):
			vel_msg.angular.z = 0.0
			vel_msg.linear.x = 0.5
			velocity_publisher.publish(vel_msg)
		break	
				
			
  
if __name__ == '__main__':
    try:
        #Testing our function
	position_topic = '/turtle2/pose'
	pose_subscriber_turtle1 = rospy.Subscriber('/turtle1/pose', Pose, poseCallback1)
	pose_subscriber_turtle2 = rospy.Subscriber('/turtle2/pose', Pose, poseCallback2)
        move()
    except rospy.ROSInterruptException: pass
