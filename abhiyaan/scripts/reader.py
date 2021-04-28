#!/usr/bin/env python
import rospy
from std_msgs.msg import String
class Server:
    def __init__(self):
        self.str_1 = ''
        self.str_2 = ''
        self.num = 1

    def callback1(self, msg):
        # "Store" message received.
        self.str_1 = msg.data

    def callback2(self, msg):
        # "Store" the message received.
        self.str_2 = msg.data

def listener(server):
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True)

    rospy.Subscriber("team_abhiyaan", String, server.callback1)
    rospy.Subscriber("autonomy", String, server.callback2)
    rate = rospy.Rate(1)
    rate.sleep()
if __name__ == '__main__':
    server = Server()
    listener(server)
    x = server.str_1 + server.str_2
    print(x)
