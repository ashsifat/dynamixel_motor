#!/usr/bin/env python
# license removed for brevity
import rospy
from sensor_msgs.msg import JointState
from sensor_msgs.msg import JointState as JointStatePR2

def talker():
    pub = rospy.Publisher('chatter', JointState, queue_size=1)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    msg=JointStatePR2()
    msg.name=[]
    msg.position=[]
    msg.velocity=[]
    msg.effort=[]    
    while not rospy.is_shutdown():
#        hello_str = "hello world %s" % rospy.get_time()
#        rospy.loginfo(hello_str)
	del msg.name[:]
	del msg.position[:]
	del msg.velocity[:]
	del msg.effort[:]
	hello_str="joint"
	msg.name.append(hello_str)
	msg.position.append(10)
	msg.velocity.append(100)
	msg.effort.append(20)
        pub.publish(msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass



##################################################3

#from sensor_msgs.msg import JointState
#from numpy import zeros, array, linspace

#currentJointState = JointState()
#def jointStatesCallback(msg):
#    global currentJointState
#    currentJointState = msg
#    
#    
#        rospy.Subscriber("chatter", JointState, jointStatesCallback)    
#        
#		print currentJointState.position
