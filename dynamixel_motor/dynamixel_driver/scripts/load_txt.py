#!/usr/bin/env python
__author__ = 'Ash'
__copyright__ = '...'

#__license__ = 'BSD'
__maintainer__ = 'Ashrarul Sifat'
__email__ = 'ashrar7@vt.edu'

## Simple talker demo that published std_msgs/Strings messages
## to the 'chatter' topic
#import roslib; roslib.load_manifest('numpy_tutorials')
import sys
#from optparse import OptionParser
import math
import sys
import errno
import time
import roslib
roslib.load_manifest('dynamixel_driver')
from dynamixel_driver import dynamixel_io
import rospy
import numpy as np
from std_msgs.msg import Byte
from dynamixel_driver.dynamixel_const import *

from dynamixel_msgs.msg import MotorState
from dynamixel_msgs.msg import MotorStateList

def twos_complement(val, nbits):
    	"""Compute the 2's complement of int value val"""
    	if val < 0:
             val = (1 << nbits) + val
    	else:
             if (val & (1 << (nbits - 1))) != 0:
            	# If sign bit is set.
            	# compute negative value.
            	val = val - (1 << nbits)
    	return val


def pos_control2():
    pub = rospy.Publisher('current', Byte, queue_size=1)
    rospy.init_node('pos_control2', anonymous=True)
    rate = rospy.Rate(1000) # 10hz
    #angles=np.genfromtxt('athena_pseudo_walk_joint_angles',usecols=(9,10,11,12,13,14,15,16,17,18,19,20))
    angles=np.genfromtxt('athena_pseudo_walk_footheight015_step015',usecols=(9,10,11,12,13,14,15,16,17,18,19,20))
    #athena_pseudo_walk_footheight015_step015	
    					#r-hip-y(0)  r-hip-r(1)   r-hip-p(2)  r-knee-p(3)  r-ankl-p(4) r-ankle-r(5) l-hip-y(6)  l-hip-r(7)  l-hip-p(8)   l-knee-p(9) l-ankle-p(10) l-ankle-r(11)
    angles=angles*2048/3.14159
    val=angles[3,:]
    print val
    val2=val;
    print 'Turning left hip torque %s for motor %d' % (torque_on, motor_id)
    if dxl_io_0.ping(motor_id):
                torque_response= dxl_io_0.set_torque_enabled(1,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_0.set_torque_enabled(2,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
		torque_response= dxl_io_0.set_torque_enabled(3,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_0.set_torque_enabled(4,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
                torque_response= dxl_io_0.set_torque_enabled(5,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_0.set_torque_enabled(6,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
                print 'done'
    else:
    	        print 'ERROR: motor %d did not respond. Make sure to specify the correct baudrate.' % motor_id
     
#    torque_response= dxl_io_0.set_torque_enabled(5,1)
#    print "torque enable2 response", torque_response
#    time.sleep(1) 
#    torque_response= dxl_io_0.set_torque_enabled(6,1)
#    print "torque enable1 response", torque_response
#    time.sleep(1)
#    print 'done'
      
    print 'Turning right hip torque %s for motor %d' % (torque_on, motor_id)
    if dxl_io_1.ping(motor_id):
                torque_response= dxl_io_1.set_torque_enabled(1,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_1.set_torque_enabled(2,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
		torque_response= dxl_io_1.set_torque_enabled(3,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_1.set_torque_enabled(4,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
                torque_response= dxl_io_1.set_torque_enabled(5,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_1.set_torque_enabled(6,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
                print 'done'
    else:
    	        print 'ERROR: motor %d did not respond. Make sure to specify the correct baudrate.' % motor_id_3

    print 'Turning right knee torque %s for motor %d' % (torque_on, motor_id_3)
    if dxl_io_2.ping(motor_id_3):
                torque_response= dxl_io_2.set_torque_enabled(7,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_2.set_torque_enabled(8,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
		torque_response= dxl_io_2.set_torque_enabled(9,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_2.set_torque_enabled(10,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
		torque_response= dxl_io_2.set_torque_enabled(11,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_2.set_torque_enabled(12,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
                print 'done'
    else:
    	        print 'ERROR: motor %d did not respond. Make sure to specify the correct baudrate.' % motor_id_3
    	            	        
    print 'Turning left hip torque %s for motor %d' % (torque_on, motor_id_3)
    if dxl_io_3.ping(motor_id_3):
                torque_response= dxl_io_3.set_torque_enabled(7,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_3.set_torque_enabled(8,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
		torque_response= dxl_io_3.set_torque_enabled(9,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_3.set_torque_enabled(10,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
		torque_response= dxl_io_3.set_torque_enabled(11,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_3.set_torque_enabled(12,1)
		print "torque enable1 response", torque_response
		time.sleep(1)
                print 'done'
    else:
    	        print 'ERROR: motor %d did not respond. Make sure to specify the correct baudrate.' % motor_id_3

    time.sleep(4)
#    torque_response= dxl_io_3.set_torque_enabled(7,1)
#    print "torque enable2 response", torque_response
#    time.sleep(1) 
#    torque_response= dxl_io_3.set_torque_enabled(8,1)
#    print "torque enable1 response", torque_response
#    time.sleep(1)
#    print 'done'

#    write_address= [0x74, 0x00]
#    write_data = [0xAA, 0x02, 0x00, 0x00 ]
#    write_response = dxl_io.write(1,write_address, write_data)
#    print "write done, response:", write_response
    #sync_write_address= [0x66, 0x00]  		#current
    sync_write_address= [0x74, 0x00]		#position
    val = 2048
    nbits = 32
    ###########3 zero to left hip yaw
#    sync_write_data = [0x04, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00 ]
#    dxl_io_0.sync_write(sync_write_address, sync_write_data)
    ############### lhp #########################
    val1_lhp=int(round(val-angles[0,8]))
    val2_lhp=int(round(val+angles[0,8]))
#    val1_lhp=val
#    val2_lhp=val
    write_data_whole1= twos_complement(val1_lhp, nbits)
    write_data_11p = write_data_whole1 & 0xFF
    write_data_21p = (write_data_whole1>>8) & 0xFF
    write_data_31p = (write_data_whole1>>16) & 0xFF
    write_data_41p = (write_data_whole1>>32) & 0xFF
    #for motor2 value
    write_data_whole2 = twos_complement(val2_lhp, nbits)
    write_data_12p = write_data_whole2 & 0xFF
    write_data_22p = (write_data_whole2>>8) & 0xFF
    write_data_32p = (write_data_whole2>>16) & 0xFF
    write_data_42p = (write_data_whole2>>24) & 0xFF
    ############### lhr #########################
    val1_lhr=int(round(val-angles[0,7]))
    val2_lhr=int(round(val+angles[0,7]))
#    val1_lhp=val
#    val2_lhp=val
    write_data_whole1= twos_complement(val1_lhr, nbits)
    write_data_11r = write_data_whole1 & 0xFF
    write_data_21r = (write_data_whole1>>8) & 0xFF
    write_data_31r = (write_data_whole1>>16) & 0xFF
    write_data_41r = (write_data_whole1>>32) & 0xFF
    #for motor2 value
    write_data_whole2 = twos_complement(val2_lhr, nbits)
    write_data_12r = write_data_whole2 & 0xFF
    write_data_22r = (write_data_whole2>>8) & 0xFF
    write_data_32r = (write_data_whole2>>16) & 0xFF
    write_data_42r = (write_data_whole2>>24) & 0xFF
#    sync_write_data = [0x04, 0x00,0x03, write_data_11r, write_data_21r, write_data_31r, write_data_41r, 0x04, write_data_12r,write_data_22r, write_data_32r, write_data_42r, 0x05, write_data_11p, write_data_21p, write_data_31p, write_data_41p, 0x06, write_data_12p,write_data_22p, write_data_32p, write_data_42p ]
    sync_write_data = [0x04, 0x00, 0x05, write_data_11p, write_data_21p, write_data_31p, write_data_41p, 0x06, write_data_12p,write_data_22p, write_data_32p, write_data_42p ]
    dxl_io_0.sync_write(sync_write_address, sync_write_data)
    ###########3 zero to right hip yaw
#    sync_write_data = [0x04, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00 ]
#    dxl_io_1.sync_write(sync_write_address, sync_write_data)
    ################### rhp #########################
    val1_rhp=int(round(val+angles[0,2]))
    val2_rhp=int(round(val-angles[0,2]))
#    val1_rhp=val
#    val2_rhp=val
    write_data_whole1= twos_complement(val1_rhp, nbits)
    write_data_11 = write_data_whole1 & 0xFF
    write_data_21 = (write_data_whole1>>8) & 0xFF
    write_data_31 = (write_data_whole1>>16) & 0xFF
    write_data_41 = (write_data_whole1>>32) & 0xFF
    #for motor2 value
    write_data_whole2 = twos_complement(val2_rhp, nbits)
    write_data_12 = write_data_whole2 & 0xFF
    write_data_22 = (write_data_whole2>>8) & 0xFF
    write_data_32 = (write_data_whole2>>16) & 0xFF
    write_data_42 = (write_data_whole2>>24) & 0xFF
    ############### rhr #########################
    val1_rhr=int(round(val-angles[0,1]))
    val2_rhr=int(round(val+angles[0,1]))
#    val1_lhp=val
#    val2_lhp=val
    write_data_whole1= twos_complement(val1_rhr, nbits)
    write_data_11r = write_data_whole1 & 0xFF
    write_data_21r = (write_data_whole1>>8) & 0xFF
    write_data_31r = (write_data_whole1>>16) & 0xFF
    write_data_41r = (write_data_whole1>>32) & 0xFF
    #for motor2 value
    write_data_whole2 = twos_complement(val2_rhr, nbits)
    write_data_12r = write_data_whole2 & 0xFF
    write_data_22r = (write_data_whole2>>8) & 0xFF
    write_data_32r = (write_data_whole2>>16) & 0xFF
    write_data_42r = (write_data_whole2>>24) & 0xFF
#    sync_write_data = [0x04, 0x00,0x03, write_data_11r, write_data_21r, write_data_31r, write_data_41r, 0x04, write_data_12r,write_data_22r, write_data_32r, write_data_42r, 0x05, write_data_11, write_data_21, write_data_31, write_data_41, 0x06, write_data_12,write_data_22, write_data_32, write_data_42 ]
    sync_write_data = [0x04, 0x00, 0x05, write_data_11, write_data_21, write_data_31, write_data_41, 0x06, write_data_12,write_data_22, write_data_32, write_data_42 ]
    dxl_io_1.sync_write(sync_write_address, sync_write_data)
    ############## rkp, rap #######################################333
    val1_rkp=int(round(val-angles[0,3]))
    val2_rkp=int(round(val+angles[0,3]))
#    val1_rkp=val
#    val2_rkp=val
    write_data_whole1= twos_complement(val1_rkp, nbits)
    write_data_11k = write_data_whole1 & 0xFF
    write_data_21k = (write_data_whole1>>8) & 0xFF
    write_data_31k = (write_data_whole1>>16) & 0xFF
    write_data_41k = (write_data_whole1>>32) & 0xFF
    #for motor8 value
    write_data_whole2 = twos_complement(val2_rkp, nbits)
    write_data_12k = write_data_whole2 & 0xFF
    write_data_22k = (write_data_whole2>>8) & 0xFF
    write_data_32k = (write_data_whole2>>16) & 0xFF
    write_data_42k = (write_data_whole2>>24) & 0xFF
    #for motor 9,10 value#####  rap #############
    val1_rap=int(round(val+angles[0,4]))
    val2_rap=int(round(val-angles[0,4]))
#    val1_rap=val
#    val2_rap=val
    write_data_whole1= twos_complement(val1_rap, nbits)
    write_data_11a = write_data_whole1 & 0xFF
    write_data_21a = (write_data_whole1>>8) & 0xFF
    write_data_31a = (write_data_whole1>>16) & 0xFF
    write_data_41a = (write_data_whole1>>32) & 0xFF
    #for motor10 value
    write_data_whole2 = twos_complement(val2_rap, nbits)
    write_data_12a = write_data_whole2 & 0xFF
    write_data_22a = (write_data_whole2>>8) & 0xFF
    write_data_32a = (write_data_whole2>>16) & 0xFF
    write_data_42a = (write_data_whole2>>24) & 0xFF
    ############### rar #########################
    val1_rar=int(round(val+angles[0,5]))
    val2_rar=int(round(val-angles[0,5]))
#    val1_lhp=val
#    val2_lhp=val
    write_data_whole1= twos_complement(val1_rar, nbits)
    write_data_11r = write_data_whole1 & 0xFF
    write_data_21r = (write_data_whole1>>8) & 0xFF
    write_data_31r = (write_data_whole1>>16) & 0xFF
    write_data_41r = (write_data_whole1>>32) & 0xFF
    #for motor2 value
    write_data_whole2 = twos_complement(val2_rar, nbits)
    write_data_12r = write_data_whole2 & 0xFF
    write_data_22r = (write_data_whole2>>8) & 0xFF
    write_data_32r = (write_data_whole2>>16) & 0xFF
    write_data_42r = (write_data_whole2>>24) & 0xFF
    sync_write_data = [0x04, 0x00, 0x07, write_data_11k, write_data_21k, write_data_31k, write_data_41k, 0x08, write_data_12k,write_data_22k, write_data_32k, write_data_42k, 0x09, write_data_11a, write_data_21a, write_data_31a, write_data_41a, 0x0A, write_data_12a,write_data_22a, write_data_32a, write_data_42a, 0x0B, write_data_11r, write_data_21r, write_data_31r, write_data_41r, 0x0C, write_data_12r,write_data_22r, write_data_32r, write_data_42r ]
    dxl_io_2.sync_write(sync_write_address, sync_write_data)
    ############## lkp, lap #######################################333
    val1_lkp=int(round(val+angles[0,9]))
    val2_lkp=int(round(val-angles[0,9]))
#    val1_lkp=val
#    val2_lkp=val
    write_data_whole1= twos_complement(val1_lkp, nbits)
    write_data_11k = write_data_whole1 & 0xFF
    write_data_21k = (write_data_whole1>>8) & 0xFF
    write_data_31k = (write_data_whole1>>16) & 0xFF
    write_data_41k = (write_data_whole1>>32) & 0xFF
    #for motor8 value
    write_data_whole2 = twos_complement(val2_lkp, nbits)
    write_data_12k = write_data_whole2 & 0xFF
    write_data_22k = (write_data_whole2>>8) & 0xFF
    write_data_32k = (write_data_whole2>>16) & 0xFF
    write_data_42k = (write_data_whole2>>24) & 0xFF
    #for motor 9,10 value
    val1_lap=int(round(val-angles[0,10]))
    val2_lap=int(round(val+angles[0,10]))
#    val1_lap=val
#    val2_lap=val
    write_data_whole1= twos_complement(val1_lap, nbits)
    write_data_11a = write_data_whole1 & 0xFF
    write_data_21a = (write_data_whole1>>8) & 0xFF
    write_data_31a = (write_data_whole1>>16) & 0xFF
    write_data_41a = (write_data_whole1>>32) & 0xFF
    #for motor10 value
    write_data_whole2 = twos_complement(val2_lap, nbits)
    write_data_12a = write_data_whole2 & 0xFF
    write_data_22a = (write_data_whole2>>8) & 0xFF
    write_data_32a = (write_data_whole2>>16) & 0xFF
    write_data_42a = (write_data_whole2>>24) & 0xFF
    ############### lar #########################
    val1_lar=int(round(val+angles[0,11]))
    val2_lar=int(round(val-angles[0,11]))
#    val1_lhp=val
#    val2_lhp=val
    write_data_whole1= twos_complement(val1_lar, nbits)
    write_data_11r = write_data_whole1 & 0xFF
    write_data_21r = (write_data_whole1>>8) & 0xFF
    write_data_31r = (write_data_whole1>>16) & 0xFF
    write_data_41r = (write_data_whole1>>32) & 0xFF
    #for motor2 value
    write_data_whole2 = twos_complement(val2_lar, nbits)
    write_data_12r = write_data_whole2 & 0xFF
    write_data_22r = (write_data_whole2>>8) & 0xFF
    write_data_32r = (write_data_whole2>>16) & 0xFF
    write_data_42r = (write_data_whole2>>24) & 0xFF
    sync_write_data = [0x04, 0x00, 0x07, write_data_11k, write_data_21k, write_data_31k, write_data_41k, 0x08, write_data_12k,write_data_22k, write_data_32k, write_data_42k, 0x09, write_data_11a, write_data_21a, write_data_31a, write_data_41a, 0x0A, write_data_12a,write_data_22a, write_data_32a, write_data_42a, 0x0B, write_data_11r, write_data_21r, write_data_31r, write_data_41r, 0x0C, write_data_12r,write_data_22r, write_data_32r, write_data_42r ]
    dxl_io_3.sync_write(sync_write_address, sync_write_data)
    print "sync_write done, position control"
    time.sleep(5)
    i=1
    j=0
		#write_.append(val1)
#    write_data_whole1= twos_complement(val1, nbits)
##		write_data_L1 = write_data_whole1 & 0xFF
##		write_data_H1 = (write_data_whole1>>8) & 0xFF
#    write_data_11 = write_data_whole1 & 0xFF
#    write_data_21 = (write_data_whole1>>8) & 0xFF
#    write_data_31 = (write_data_whole1>>16) & 0xFF
#    write_data_41 = (write_data_whole1>>32) & 0xFF
#		#for motor2 value
#    write_data_whole2 = twos_complement(val2, nbits)
##		write_data_L2=write_data_whole2 & 0xFF
##		write_data_H2 = (write_data_whole2>>8) & 0xFF
#    write_data_12 = write_data_whole2 & 0xFF
#    write_data_22 = (write_data_whole2>>8) & 0xFF
#    write_data_32 = (write_data_whole2>>16) & 0xFF
#    write_data_42 = (write_data_whole2>>24) & 0xFF
#    sync_write_address= [0x74, 0x00]
#    #sync_write_data = [0x04, 0x00, 0x01, 0x00, 0x00, 0x00, 0x00, 0x02, 0x00, 0x00, 0x00, 0x00 ]
#    sync_write_data = [0x04, 0x00, 0x05, write_data_11, write_data_21, write_data_31, write_data_41, 0x06, write_data_12,write_data_22, write_data_32, write_data_42 ]
#    dxl_io_0.sync_write(sync_write_address, sync_write_data)
#    sync_write_data = [0x04, 0x00, 0x07, write_data_11, write_data_21, write_data_31, write_data_41, 0x08, write_data_12,write_data_22, write_data_32, write_data_42 ]
#    dxl_io_3.sync_write(sync_write_address, sync_write_data)
#    print "sync_write done, position control"
#    time.sleep(5)
    

    while not rospy.is_shutdown() :
    		    ############### lhp #########################
		    val1_lhp=int(round(val-angles[i,8]))
		    val2_lhp=int(round(val+angles[i,8]))
		#    val1_lhp=val
		#    val2_lhp=val
		    write_data_whole1= twos_complement(val1_lhp, nbits)
		    write_data_11p = write_data_whole1 & 0xFF
		    write_data_21p = (write_data_whole1>>8) & 0xFF
		    write_data_31p = (write_data_whole1>>16) & 0xFF
		    write_data_41p = (write_data_whole1>>32) & 0xFF
		    #for motor2 value
		    write_data_whole2 = twos_complement(val2_lhp, nbits)
		    write_data_12p = write_data_whole2 & 0xFF
		    write_data_22p = (write_data_whole2>>8) & 0xFF
		    write_data_32p = (write_data_whole2>>16) & 0xFF
		    write_data_42p = (write_data_whole2>>24) & 0xFF
		    ############### lhr #########################
		    val1_lhr=int(round(val-angles[i,7]))
		    val2_lhr=int(round(val+angles[i,7]))
		#    val1_lhp=val
		#    val2_lhp=val
		    write_data_whole1= twos_complement(val1_lhr, nbits)
		    write_data_11r = write_data_whole1 & 0xFF
		    write_data_21r = (write_data_whole1>>8) & 0xFF
		    write_data_31r = (write_data_whole1>>16) & 0xFF
		    write_data_41r = (write_data_whole1>>32) & 0xFF
		    #for motor2 value
		    write_data_whole2 = twos_complement(val2_lhr, nbits)
		    write_data_12r = write_data_whole2 & 0xFF
		    write_data_22r = (write_data_whole2>>8) & 0xFF
		    write_data_32r = (write_data_whole2>>16) & 0xFF
		    write_data_42r = (write_data_whole2>>24) & 0xFF
		    #sync_write_data = [0x04, 0x00,0x03, write_data_11r, write_data_21r, write_data_31r, write_data_41r, 0x04, write_data_12r,write_data_22r, write_data_32r, write_data_42r, 0x05, write_data_11p, write_data_21p, write_data_31p, write_data_41p, 0x06, write_data_12p,write_data_22p, write_data_32p, write_data_42p ]
		    sync_write_data = [0x04, 0x00, 0x05, write_data_11p, write_data_21p, write_data_31p, write_data_41p, 0x06, write_data_12p,write_data_22p, write_data_32p, write_data_42p ]
		    dxl_io_0.sync_write(sync_write_address, sync_write_data)
		    ################### rhp #########################
		    val1_rhp=int(round(val+angles[i,2]))
		    val2_rhp=int(round(val-angles[i,2]))
		#    val1_rhp=val
		#    val2_rhp=val
		    write_data_whole1= twos_complement(val1_rhp, nbits)
		    write_data_11 = write_data_whole1 & 0xFF
		    write_data_21 = (write_data_whole1>>8) & 0xFF
		    write_data_31 = (write_data_whole1>>16) & 0xFF
		    write_data_41 = (write_data_whole1>>32) & 0xFF
		    #for motor2 value
		    write_data_whole2 = twos_complement(val2_rhp, nbits)
		    write_data_12 = write_data_whole2 & 0xFF
		    write_data_22 = (write_data_whole2>>8) & 0xFF
		    write_data_32 = (write_data_whole2>>16) & 0xFF
		    write_data_42 = (write_data_whole2>>24) & 0xFF
		    ############### rhr #########################
		    val1_rhr=int(round(val-angles[i,1]))
		    val2_rhr=int(round(val+angles[i,1]))
		#    val1_lhp=val
		#    val2_lhp=val
		    write_data_whole1= twos_complement(val1_rhr, nbits)
		    write_data_11r = write_data_whole1 & 0xFF
		    write_data_21r = (write_data_whole1>>8) & 0xFF
		    write_data_31r = (write_data_whole1>>16) & 0xFF
		    write_data_41r = (write_data_whole1>>32) & 0xFF
		    #for motor2 value
		    write_data_whole2 = twos_complement(val2_rhr, nbits)
		    write_data_12r = write_data_whole2 & 0xFF
		    write_data_22r = (write_data_whole2>>8) & 0xFF
		    write_data_32r = (write_data_whole2>>16) & 0xFF
		    write_data_42r = (write_data_whole2>>24) & 0xFF
		    #sync_write_data = [0x04, 0x00,0x03, write_data_11r, write_data_21r, write_data_31r, write_data_41r, 0x04, write_data_12r,write_data_22r, write_data_32r, write_data_42r, 0x05, write_data_11, write_data_21, write_data_31, write_data_41, 0x06, write_data_12,write_data_22, write_data_32, write_data_42 ]
		    sync_write_data = [0x04, 0x00, 0x05, write_data_11, write_data_21, write_data_31, write_data_41, 0x06, write_data_12,write_data_22, write_data_32, write_data_42 ]
		    dxl_io_1.sync_write(sync_write_address, sync_write_data)
		    ############## rkp, rap #######################################333
		    val1_rkp=int(round(val-angles[i,3]))
		    val2_rkp=int(round(val+angles[i,3]))
		#    val1_rkp=val
		#    val2_rkp=val
		    write_data_whole1= twos_complement(val1_rkp, nbits)
		    write_data_11k = write_data_whole1 & 0xFF
		    write_data_21k = (write_data_whole1>>8) & 0xFF
		    write_data_31k = (write_data_whole1>>16) & 0xFF
		    write_data_41k = (write_data_whole1>>32) & 0xFF
		    #for motor8 value
		    write_data_whole2 = twos_complement(val2_rkp, nbits)
		    write_data_12k = write_data_whole2 & 0xFF
		    write_data_22k = (write_data_whole2>>8) & 0xFF
		    write_data_32k = (write_data_whole2>>16) & 0xFF
		    write_data_42k = (write_data_whole2>>24) & 0xFF
		    #for motor 9,10 value#####  rap #############
		    val1_rap=int(round(val+angles[i,4]))
		    val2_rap=int(round(val-angles[i,4]))
		#    val1_rap=val
		#    val2_rap=val
		    write_data_whole1= twos_complement(val1_rap, nbits)
		    write_data_11a = write_data_whole1 & 0xFF
		    write_data_21a = (write_data_whole1>>8) & 0xFF
		    write_data_31a = (write_data_whole1>>16) & 0xFF
		    write_data_41a = (write_data_whole1>>32) & 0xFF
		    #for motor10 value
		    write_data_whole2 = twos_complement(val2_rap, nbits)
		    write_data_12a = write_data_whole2 & 0xFF
		    write_data_22a = (write_data_whole2>>8) & 0xFF
		    write_data_32a = (write_data_whole2>>16) & 0xFF
		    write_data_42a = (write_data_whole2>>24) & 0xFF
		    ############### rar #########################
		    val1_rar=int(round(val+angles[i,5]))
		    val2_rar=int(round(val-angles[i,5]))
		#    val1_lhp=val
		#    val2_lhp=val
		    write_data_whole1= twos_complement(val1_rar, nbits)
		    write_data_11r = write_data_whole1 & 0xFF
		    write_data_21r = (write_data_whole1>>8) & 0xFF
		    write_data_31r = (write_data_whole1>>16) & 0xFF
		    write_data_41r = (write_data_whole1>>32) & 0xFF
		    #for motor2 value
		    write_data_whole2 = twos_complement(val2_rar, nbits)
		    write_data_12r = write_data_whole2 & 0xFF
		    write_data_22r = (write_data_whole2>>8) & 0xFF
		    write_data_32r = (write_data_whole2>>16) & 0xFF
		    write_data_42r = (write_data_whole2>>24) & 0xFF
		    sync_write_data = [0x04, 0x00, 0x07, write_data_11k, write_data_21k, write_data_31k, write_data_41k, 0x08, write_data_12k,write_data_22k, write_data_32k, write_data_42k, 0x09, write_data_11a, write_data_21a, write_data_31a, write_data_41a, 0x0A, write_data_12a,write_data_22a, write_data_32a, write_data_42a, 0x0B, write_data_11r, write_data_21r, write_data_31r, write_data_41r, 0x0C, write_data_12r,write_data_22r, write_data_32r, write_data_42r ]
		    dxl_io_2.sync_write(sync_write_address, sync_write_data)
		    ############## lkp, lap #######################################333
		    val1_lkp=int(round(val+angles[i,9]))
		    val2_lkp=int(round(val-angles[i,9]))
		#    val1_lkp=val
		#    val2_lkp=val
		    write_data_whole1= twos_complement(val1_lkp, nbits)
		    write_data_11k = write_data_whole1 & 0xFF
		    write_data_21k = (write_data_whole1>>8) & 0xFF
		    write_data_31k = (write_data_whole1>>16) & 0xFF
		    write_data_41k = (write_data_whole1>>32) & 0xFF
		    #for motor8 value
		    write_data_whole2 = twos_complement(val2_lkp, nbits)
		    write_data_12k = write_data_whole2 & 0xFF
		    write_data_22k = (write_data_whole2>>8) & 0xFF
		    write_data_32k = (write_data_whole2>>16) & 0xFF
		    write_data_42k = (write_data_whole2>>24) & 0xFF
		    #for motor 9,10 value
		    val1_lap=int(round(val-angles[i,10]))
		    val2_lap=int(round(val+angles[i,10]))
		#    val1_lap=val
		#    val2_lap=val
		    write_data_whole1= twos_complement(val1_lap, nbits)
		    write_data_11a = write_data_whole1 & 0xFF
		    write_data_21a = (write_data_whole1>>8) & 0xFF
		    write_data_31a = (write_data_whole1>>16) & 0xFF
		    write_data_41a = (write_data_whole1>>32) & 0xFF
		    #for motor10 value
		    write_data_whole2 = twos_complement(val2_lap, nbits)
		    write_data_12a = write_data_whole2 & 0xFF
		    write_data_22a = (write_data_whole2>>8) & 0xFF
		    write_data_32a = (write_data_whole2>>16) & 0xFF
		    write_data_42a = (write_data_whole2>>24) & 0xFF
		    ############### lar #########################
		    val1_lar=int(round(val+angles[i,11]))
		    val2_lar=int(round(val-angles[i,11]))
		#    val1_lhp=val
		#    val2_lhp=val
		    write_data_whole1= twos_complement(val1_lar, nbits)
		    write_data_11r = write_data_whole1 & 0xFF
		    write_data_21r = (write_data_whole1>>8) & 0xFF
		    write_data_31r = (write_data_whole1>>16) & 0xFF
		    write_data_41r = (write_data_whole1>>32) & 0xFF
		    #for motor2 value
		    write_data_whole2 = twos_complement(val2_lar, nbits)
		    write_data_12r = write_data_whole2 & 0xFF
		    write_data_22r = (write_data_whole2>>8) & 0xFF
		    write_data_32r = (write_data_whole2>>16) & 0xFF
		    write_data_42r = (write_data_whole2>>24) & 0xFF
		    sync_write_data = [0x04, 0x00, 0x07, write_data_11k, write_data_21k, write_data_31k, write_data_41k, 0x08, write_data_12k,write_data_22k, write_data_32k, write_data_42k, 0x09, write_data_11a, write_data_21a, write_data_31a, write_data_41a, 0x0A, write_data_12a,write_data_22a, write_data_32a, write_data_42a, 0x0B, write_data_11r, write_data_21r, write_data_31r, write_data_41r, 0x0C, write_data_12r,write_data_22r, write_data_32r, write_data_42r ]
		    dxl_io_3.sync_write(sync_write_address, sync_write_data)
		    print "sync_write done, position control"
		    i=i+1
		    #pub.publish(val)
#		    if i==20765: #break
		    if i==37952: #break
		    	i=1
		    	j=j+1
#		if  (current_time-last_time)>5:
#		    if  angles[i,:]==[]:
#			val = 2048
#			val1=int(round(val))#write_.append(val1)
#    			write_data_whole1= twos_complement(val1, nbits)
##		write_data_L1 = write_data_whole1 & 0xFF
##		write_data_H1 = (write_data_whole1>>8) & 0xFF
#    			write_data_1 = write_data_whole1 & 0xFF
#    			write_data_2 = (write_data_whole1>>8) & 0xFF
#    			write_data_3 = (write_data_whole1>>16) & 0xFF
#    			write_data_4 = (write_data_whole1>>32) & 0xFF
#			sync_write_data = [0x04, 0x00, 0x05, write_data_1,write_data_2,write_data_3,write_data_4, 0x06, write_data_1, write_data_2, write_data_3, write_data_4 ]
#			dxl_io_0.sync_write(sync_write_address, sync_write_data)
#			sync_write_data = [0x04, 0x00, 0x07, write_data_1,write_data_2,write_data_3,write_data_4, 0x08, write_data_1, write_data_2, write_data_3, write_data_4, 0x09, write_data_1,write_data_2,write_data_3,write_data_4, 0x0A, write_data_1, write_data_2, write_data_3, write_data_4 ]
#			dxl_io_3.sync_write(sync_write_address, sync_write_data)
#			print "sync_write done, position control", i
			if j==5: break
		#pub.publish(val)

    		    rate.sleep()


if __name__ == '__main__':
    port_name0='/dev/ttyUSB0'
    port_namespace0='ttyUSB0'
    port_name1='/dev/ttyUSB1'
    port_namespace1='ttyUSB1'
    port_name2='/dev/ttyUSB2'
    port_namespace2='ttyUSB2'
    port_name3='/dev/ttyUSB3'
    port_namespace3='ttyUSB3'
    baud_rate=3000000
    min_motor_id=1
    max_motor_id=25
    update_rate=5
    diagnostics_rate=1
    error_level_temp=75
    warn_level_temp=70
    readback_echo=False
    torque_on=True
    motor_id = 1
    motor_id_3 = 7
    r=0.126
    m=842
    I=m*r*r
    c=r*m*9.81
    #i=0
#    sync_write_address= [0x66, 0x00]
    try:
        dxl_io_0 = dynamixel_io.DynamixelIO(port_name0, baud_rate)
        dxl_io_1 = dynamixel_io.DynamixelIO(port_name1, baud_rate)
        dxl_io_2 = dynamixel_io.DynamixelIO(port_name2, baud_rate)
        dxl_io_3 = dynamixel_io.DynamixelIO(port_name3, baud_rate)
    except dynamixel_io.SerialOpenError, soe:
        print 'ERROR:', soe
    else:
	pos_control2()
