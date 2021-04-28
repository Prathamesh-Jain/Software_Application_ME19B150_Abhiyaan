#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def main():
    
    # 1. Create a handle to publish messages to a topic.
    pub = rospy.Publisher('team_abhiyaan', String, queue_size=10)
    
    # 2. Initializes the ROS node for the process.
    rospy.init_node('node1', anonymous=True)

    # 3. Set the Loop Rate 
    rate = rospy.Rate(1) # 1 Hz : Loop will its best to run 1 time in 1 second
    
    # 4. Write the infinite Loop
    while not rospy.is_shutdown():
        str_1 = "Team Abhiyaan:"
        pub.publish(str_1)
        rate.sleep()



# Python Main
if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass

