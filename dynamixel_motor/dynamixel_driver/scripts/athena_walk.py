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
#import dynamixel_io
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


def athena_walk():
    pub = rospy.Publisher('current', Byte, queue_size=1)
    rospy.init_node('athena_walk', anonymous=True)
    rate = rospy.Rate(500) # 10hz
    angles=np.genfromtxt('athena_pseudo_walk_footheight015_step015',usecols=(9,10,11,12,13,14,15,16,17,18,19,20))
    #athena_pseudo_walk_footheight015_step015	
    					#r-hip-y(0)  r-hip-r(1)   r-hip-p(2)  r-knee-p(3)  r-ankl-p(4) r-ankle-r(5) l-hip-y(6)  l-hip-r(7)  l-hip-p(8)   l-knee-p(9) l-ankle-p(10) l-ankle-r(11)
    angles=angles*2048/3.14159
    print 'Turning right leg torque %s for motor %d' % (torque_on, motor_id)
    if dxl_io_0.ping(motor_id):
                torque_response= dxl_io_0.set_torque_enabled(1,1)
		print "torque enable rhy response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_0.set_torque_enabled(2,1)
		print "torque enable rhr response", torque_response
		time.sleep(1)
                torque_response= dxl_io_0.set_torque_enabled(3,1)
		print "torque enable rhp response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_0.set_torque_enabled(4,1)
		print "torque enable rkp response", torque_response
		time.sleep(1)
                torque_response= dxl_io_0.set_torque_enabled(5,1)
		print "torque enable rap response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_0.set_torque_enabled(6,1)
		print "torque enable rar response", torque_response
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
      
    print 'Turning left leg torque %s for motor %d' % (torque_on, motor_id)
    if dxl_io_1.ping(motor_id):
                torque_response= dxl_io_1.set_torque_enabled(1,1)
		print "torque enable lhy response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_1.set_torque_enabled(2,1)
		print "torque enable lhr response", torque_response
		time.sleep(1)
                torque_response= dxl_io_1.set_torque_enabled(3,1)
		print "torque enable lhp response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_1.set_torque_enabled(4,1)
		print "torque enable lkp response", torque_response
		time.sleep(1)
                torque_response= dxl_io_1.set_torque_enabled(5,1)
		print "torque enable lap response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_1.set_torque_enabled(6,1)
		print "torque enable lar response", torque_response
		time.sleep(1)
                print 'done'
    else:
    	        print 'ERROR: motor %d did not respond. Make sure to specify the correct baudrate.' % motor_id

#    print 'Turning right knee torque %s for motor %d' % (torque_on, motor_id_3)
#    if dxl_io_2.ping(motor_id_3):
#                torque_response= dxl_io_2.set_torque_enabled(7,1)
#		print "torque enable2 response", torque_response
#		time.sleep(1) 
#		torque_response= dxl_io_2.set_torque_enabled(8,1)
#		print "torque enable1 response", torque_response
#		time.sleep(1)
#		torque_response= dxl_io_2.set_torque_enabled(9,1)
#		print "torque enable2 response", torque_response
#		time.sleep(1) 
#		torque_response= dxl_io_2.set_torque_enabled(10,1)
#		print "torque enable1 response", torque_response
#		time.sleep(1)
#                print 'done'
#    else:
#    	        print 'ERROR: motor %d did not respond. Make sure to specify the correct baudrate.' % motor_id_3
#    	            	        
#    print 'Turning left hip torque %s for motor %d' % (torque_on, motor_id_3)
#    if dxl_io_3.ping(motor_id_3):
#                torque_response= dxl_io_3.set_torque_enabled(7,1)
#		print "torque enable2 response", torque_response
#		time.sleep(1) 
#		torque_response= dxl_io_3.set_torque_enabled(8,1)
#		print "torque enable1 response", torque_response
#		time.sleep(1)
#		torque_response= dxl_io_3.set_torque_enabled(9,1)
#		print "torque enable2 response", torque_response
#		time.sleep(1) 
#		torque_response= dxl_io_3.set_torque_enabled(10,1)
#		print "torque enable1 response", torque_response
#		time.sleep(1)
#                print 'done'
#    else:
#    	        print 'ERROR: motor %d did not respond. Make sure to specify the correct baudrate.' % motor_id_3

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
    val = 2049
    nbits = 32


    ################### rhy #########################
    val_rhy=int(round(val+angles[0,0]))
    write_data_whole1= twos_complement(val_rhy, nbits)
    write_data_1rhy = write_data_whole1 & 0xFF
    write_data_2rhy = (write_data_whole1>>8) & 0xFF
    write_data_3rhy = (write_data_whole1>>16) & 0xFF
    write_data_4rhy = (write_data_whole1>>32) & 0xFF
    ################## rhr ##########################
    val_rhr=int(round(val+angles[0,1]))
    write_data_whole1= twos_complement(val_rhr, nbits)
    write_data_1rhr = write_data_whole1 & 0xFF
    write_data_2rhr = (write_data_whole1>>8) & 0xFF
    write_data_3rhr = (write_data_whole1>>16) & 0xFF
    write_data_4rhr = (write_data_whole1>>32) & 0xFF

    ################### rhp #########################
#    val1_rhp=int(round(val+angles[0,0]))
    val_rhp=int(round(val+angles[0,2]))
    write_data_whole1= twos_complement(val_rhp, nbits)
    write_data_1rhp = write_data_whole1 & 0xFF
    write_data_2rhp = (write_data_whole1>>8) & 0xFF
    write_data_3rhp = (write_data_whole1>>16) & 0xFF
    write_data_4rhp = (write_data_whole1>>32) & 0xFF
#    ############## rkp, rap, rar #######################################333
#    val1_rkp=int(round(val+angles[0,1]))
    val_rkp=int(round(val+angles[0,3]))
    write_data_whole1= twos_complement(val_rkp, nbits)
    write_data_1rkp = write_data_whole1 & 0xFF
    write_data_2rkp = (write_data_whole1>>8) & 0xFF
    write_data_3rkp = (write_data_whole1>>16) & 0xFF
    write_data_4rkp = (write_data_whole1>>32) & 0xFF
    val_rap=int(round(val+angles[0,4]))
    write_data_whole1= twos_complement(val_rap, nbits)
    write_data_1rap = write_data_whole1 & 0xFF
    write_data_2rap = (write_data_whole1>>8) & 0xFF
    write_data_3rap = (write_data_whole1>>16) & 0xFF
    write_data_4rap = (write_data_whole1>>32) & 0xFF
    val_rar=int(round(val+angles[0,5]))
    write_data_whole1= twos_complement(val_rar, nbits)
    write_data_1rar = write_data_whole1 & 0xFF
    write_data_2rar = (write_data_whole1>>8) & 0xFF
    write_data_3rar = (write_data_whole1>>16) & 0xFF
    write_data_4rar = (write_data_whole1>>32) & 0xFF


################### lhy #########################
    val_lhy=int(round(val+angles[0,6]))
    write_data_whole1= twos_complement(val_lhy, nbits)
    write_data_1lhy = write_data_whole1 & 0xFF
    write_data_2lhy = (write_data_whole1>>8) & 0xFF
    write_data_3lhy = (write_data_whole1>>16) & 0xFF
    write_data_4lhy = (write_data_whole1>>32) & 0xFF
    ################## lhr ##########################
    val_lhr=int(round(val+angles[0,7]))
    write_data_whole1= twos_complement(val_lhr, nbits)
    write_data_1lhr = write_data_whole1 & 0xFF
    write_data_2lhr = (write_data_whole1>>8) & 0xFF
    write_data_3lhr = (write_data_whole1>>16) & 0xFF
    write_data_4lhr = (write_data_whole1>>32) & 0xFF

    ################### lhp #########################
#    val1_lhp=int(round(val+angles[0,0]))
    val_lhp=int(round(val+angles[0,8]))
    write_data_whole1= twos_complement(val_lhp, nbits)
    write_data_1lhp = write_data_whole1 & 0xFF
    write_data_2lhp = (write_data_whole1>>8) & 0xFF
    write_data_3lhp = (write_data_whole1>>16) & 0xFF
    write_data_4lhp = (write_data_whole1>>32) & 0xFF
#    ############## lkp, lap, lar #######################################333
#    val1_lkp=int(round(val+angles[0,1]))
    val_lkp=int(round(val+angles[0,9]))
    write_data_whole1= twos_complement(val_lkp, nbits)
    write_data_1lkp = write_data_whole1 & 0xFF
    write_data_2lkp = (write_data_whole1>>8) & 0xFF
    write_data_3lkp = (write_data_whole1>>16) & 0xFF
    write_data_4lkp = (write_data_whole1>>32) & 0xFF
    val_lap=int(round(val+angles[0,10]))
    write_data_whole1= twos_complement(val_lap, nbits)
    write_data_1lap = write_data_whole1 & 0xFF
    write_data_2lap = (write_data_whole1>>8) & 0xFF
    write_data_3lap = (write_data_whole1>>16) & 0xFF
    write_data_4lap = (write_data_whole1>>32) & 0xFF
    val_lar=int(round(val+angles[0,11]))
    write_data_whole1= twos_complement(val_lar, nbits)
    write_data_1lar = write_data_whole1 & 0xFF
    write_data_2lar = (write_data_whole1>>8) & 0xFF
    write_data_3lar = (write_data_whole1>>16) & 0xFF
    write_data_4lar = (write_data_whole1>>32) & 0xFF

    sync_write_data = [0x04, 0x00, 0x01, write_data_1rhy, write_data_2rhy, write_data_3rhy, write_data_4rhy, 0x02, write_data_1rhy, write_data_2rhy, write_data_3rhy, write_data_4rhy, 0x03, write_data_1rhp, write_data_2rhp, write_data_3rhp, write_data_4rhp, 0x04, write_data_1rkp, write_data_2rkp, write_data_3rkp, write_data_4rkp, 0x05, write_data_1rap, write_data_2rap, write_data_3rap, write_data_4rap, 0x06, write_data_1rar, write_data_2rar, write_data_3rar, write_data_4rar]
    dxl_io_0.sync_write(sync_write_address, sync_write_data)
    sync_write_data = [0x04, 0x00, 0x01, write_data_1lhy, write_data_2lhy, write_data_3lhy, write_data_4lhy, 0x02, write_data_1lhy, write_data_2lhy, write_data_3lhy, write_data_4lhy, 0x03, write_data_1lhp, write_data_2lhp, write_data_3lhp, write_data_4lhp, 0x04, write_data_1lkp, write_data_2lkp, write_data_3lkp, write_data_4lkp, 0x05, write_data_1lap, write_data_2lap, write_data_3lap, write_data_4lap, 0x06, write_data_1lar, write_data_2lar, write_data_3lar, write_data_4lar]
    dxl_io_1.sync_write(sync_write_address, sync_write_data)
#    #for motor10 value
#    write_data_whole2 = twos_complement(val2_rap, nbits)
#    write_data_12a = write_data_whole2 & 0xFF
#    write_data_22a = (write_data_whole2>>8) & 0xFF
#    write_data_32a = (write_data_whole2>>16) & 0xFF
#    write_data_42a = (write_data_whole2>>24) & 0xFF
#    sync_write_data = [0x04, 0x00, 0x07, write_data_11k, write_data_21k, write_data_31k, write_data_41k, 0x08, write_data_12k,write_data_22k, write_data_32k, write_data_42k, 0x09, write_data_11a, write_data_21a, write_data_31a, write_data_41a, 0x0A, write_data_12a,write_data_22a, write_data_32a, write_data_42a ]
#    dxl_io_2.sync_write(sync_write_address, sync_write_data)
#    ############## lkp, lap #######################################333
#    val1_lkp=int(round(val+angles[0,4]))
#    val2_lkp=int(round(val-angles[0,4]))
#    write_data_whole1= twos_complement(val1_lkp, nbits)
#    write_data_11k = write_data_whole1 & 0xFF
#    write_data_21k = (write_data_whole1>>8) & 0xFF
#    write_data_31k = (write_data_whole1>>16) & 0xFF
#    write_data_41k = (write_data_whole1>>32) & 0xFF
#    #for motor8 value
#    write_data_whole2 = twos_complement(val2_lkp, nbits)
#    write_data_12k = write_data_whole2 & 0xFF
#    write_data_22k = (write_data_whole2>>8) & 0xFF
#    write_data_32k = (write_data_whole2>>16) & 0xFF
#    write_data_42k = (write_data_whole2>>24) & 0xFF
#    #for motor 9,10 value
#    val1_lap=int(round(val+angles[0,5]))
#    val2_lap=int(round(val-angles[0,5]))
#    write_data_whole1= twos_complement(val1_lap, nbits)
#    write_data_11a = write_data_whole1 & 0xFF
#    write_data_21a = (write_data_whole1>>8) & 0xFF
#    write_data_31a = (write_data_whole1>>16) & 0xFF
#    write_data_41a = (write_data_whole1>>32) & 0xFF
#    #for motor10 value
#    write_data_whole2 = twos_complement(val2_lap, nbits)
#    write_data_12a = write_data_whole2 & 0xFF
#    write_data_22a = (write_data_whole2>>8) & 0xFF
#    write_data_32a = (write_data_whole2>>16) & 0xFF
#    write_data_42a = (write_data_whole2>>24) & 0xFF
#    sync_write_data = [0x04, 0x00, 0x07, write_data_11k, write_data_21k, write_data_31k, write_data_41k, 0x08, write_data_12k,write_data_22k, write_data_32k, write_data_42k, 0x09, write_data_11a, write_data_21a, write_data_31a, write_data_41a, 0x0A, write_data_12a,write_data_22a, write_data_32a, write_data_42a ]
#    dxl_io_3.sync_write(sync_write_address, sync_write_data)
    print "sync_write done, position control"
    time.sleep(5)
    last_time=time.time()
#    write_=[]
#    read_cur1=[]
#    read_cur2=[]
#    read_pos1=[]
#    read_vel2=[]
#    write_time=[]
#    read_timecur1=[]
#    read_timecur2=[]
#    read_time2=[]
#    read_time3=[]
#    torque_1=[]
    last_read_vel=0
    i=1
    last_read_time=last_time
	#rr = rospy.Rate(500) # 10hz
#	while not rospy.is_shutdown() :
#	#read position
#		read_response=dxl_io.read(1,DXL_PRESENT_POSITION,4)
#		read_val_pos= read_response[9] | (read_response[10] << 8)| (read_response[11] << 16)| (read_response[12] << 24)
#		print read_val_pos

    while not rospy.is_shutdown() :
		    current_time =time.time()
		    
		    ################### rhy #########################
		    val_rhy=int(round(val+angles[0,0]))
		    write_data_whole1= twos_complement(val_rhy, nbits)
		    write_data_1rhy = write_data_whole1 & 0xFF
		    write_data_2rhy = (write_data_whole1>>8) & 0xFF
		    write_data_3rhy = (write_data_whole1>>16) & 0xFF
		    write_data_4rhy = (write_data_whole1>>32) & 0xFF
		    ################## rhr ##########################
		    val_rhr=int(round(val+angles[0,1]))
		    write_data_whole1= twos_complement(val_rhr, nbits)
		    write_data_1rhr = write_data_whole1 & 0xFF
		    write_data_2rhr = (write_data_whole1>>8) & 0xFF
		    write_data_3rhr = (write_data_whole1>>16) & 0xFF
		    write_data_4rhr = (write_data_whole1>>32) & 0xFF

		    ################### rhp #########################
		#    val1_rhp=int(round(val+angles[0,0]))
		    val_rhp=int(round(val+angles[0,2]))
		    write_data_whole1= twos_complement(val_rhp, nbits)
		    write_data_1rhp = write_data_whole1 & 0xFF
		    write_data_2rhp = (write_data_whole1>>8) & 0xFF
		    write_data_3rhp = (write_data_whole1>>16) & 0xFF
		    write_data_4rhp = (write_data_whole1>>32) & 0xFF
		#    ############## rkp, rap, rar #######################################333
		#    val1_rkp=int(round(val+angles[0,1]))
		    val_rkp=int(round(val+angles[0,3]))
		    write_data_whole1= twos_complement(val_rkp, nbits)
		    write_data_1rkp = write_data_whole1 & 0xFF
		    write_data_2rkp = (write_data_whole1>>8) & 0xFF
		    write_data_3rkp = (write_data_whole1>>16) & 0xFF
		    write_data_4rkp = (write_data_whole1>>32) & 0xFF
		    val_rap=int(round(val+angles[0,4]))
		    write_data_whole1= twos_complement(val_rap, nbits)
		    write_data_1rap = write_data_whole1 & 0xFF
		    write_data_2rap = (write_data_whole1>>8) & 0xFF
		    write_data_3rap = (write_data_whole1>>16) & 0xFF
		    write_data_4rap = (write_data_whole1>>32) & 0xFF
		    val_rar=int(round(val+angles[0,5]))
		    write_data_whole1= twos_complement(val_rar, nbits)
		    write_data_1rar = write_data_whole1 & 0xFF
		    write_data_2rar = (write_data_whole1>>8) & 0xFF
		    write_data_3rar = (write_data_whole1>>16) & 0xFF
		    write_data_4rar = (write_data_whole1>>32) & 0xFF


		################### lhy #########################
		    val_lhy=int(round(val+angles[0,6]))
		    write_data_whole1= twos_complement(val_lhy, nbits)
		    write_data_1lhy = write_data_whole1 & 0xFF
		    write_data_2lhy = (write_data_whole1>>8) & 0xFF
		    write_data_3lhy = (write_data_whole1>>16) & 0xFF
		    write_data_4lhy = (write_data_whole1>>32) & 0xFF
		    ################## lhr ##########################
		    val_lhr=int(round(val+angles[0,7]))
		    write_data_whole1= twos_complement(val_lhr, nbits)
		    write_data_1lhr = write_data_whole1 & 0xFF
		    write_data_2lhr = (write_data_whole1>>8) & 0xFF
		    write_data_3lhr = (write_data_whole1>>16) & 0xFF
		    write_data_4lhr = (write_data_whole1>>32) & 0xFF

		    ################### lhp #########################
		#    val1_lhp=int(round(val+angles[0,0]))
		    val_lhp=int(round(val+angles[0,8]))
		    write_data_whole1= twos_complement(val_lhp, nbits)
		    write_data_1lhp = write_data_whole1 & 0xFF
		    write_data_2lhp = (write_data_whole1>>8) & 0xFF
		    write_data_3lhp = (write_data_whole1>>16) & 0xFF
		    write_data_4lhp = (write_data_whole1>>32) & 0xFF
		#    ############## lkp, lap, lar #######################################333
		#    val1_lkp=int(round(val+angles[0,1]))
		    val_lkp=int(round(val+angles[0,9]))
		    write_data_whole1= twos_complement(val_lkp, nbits)
		    write_data_1lkp = write_data_whole1 & 0xFF
		    write_data_2lkp = (write_data_whole1>>8) & 0xFF
		    write_data_3lkp = (write_data_whole1>>16) & 0xFF
		    write_data_4lkp = (write_data_whole1>>32) & 0xFF
		    val_lap=int(round(val+angles[0,10]))
		    write_data_whole1= twos_complement(val_lap, nbits)
		    write_data_1lap = write_data_whole1 & 0xFF
		    write_data_2lap = (write_data_whole1>>8) & 0xFF
		    write_data_3lap = (write_data_whole1>>16) & 0xFF
		    write_data_4lap = (write_data_whole1>>32) & 0xFF
		    val_lar=int(round(val+angles[0,11]))
		    write_data_whole1= twos_complement(val_lar, nbits)
		    write_data_1lar = write_data_whole1 & 0xFF
		    write_data_2lar = (write_data_whole1>>8) & 0xFF
		    write_data_3lar = (write_data_whole1>>16) & 0xFF
		    write_data_4lar = (write_data_whole1>>32) & 0xFF

		    sync_write_data = [0x04, 0x00, 0x01, write_data_1rhy, write_data_2rhy, write_data_3rhy, write_data_4rhy, 0x02, write_data_1rhy, write_data_2rhy, write_data_3rhy, write_data_4rhy, 0x03, write_data_1rhp, write_data_2rhp, write_data_3rhp, write_data_4rhp, 0x04, write_data_1rkp, write_data_2rkp, write_data_3rkp, write_data_4rkp, 0x05, write_data_1rap, write_data_2rap, write_data_3rap, write_data_4rap, 0x06, write_data_1rar, write_data_2rar, write_data_3rar, write_data_4rar]
		    dxl_io_0.sync_write(sync_write_address, sync_write_data)
		    sync_write_data = [0x04, 0x00, 0x01, write_data_1lhy, write_data_2lhy, write_data_3lhy, write_data_4lhy, 0x02, write_data_1lhy, write_data_2lhy, write_data_3lhy, write_data_4lhy, 0x03, write_data_1lhp, write_data_2lhp, write_data_3lhp, write_data_4lhp, 0x04, write_data_1lkp, write_data_2lkp, write_data_3lkp, write_data_4lkp, 0x05, write_data_1lap, write_data_2lap, write_data_3lap, write_data_4lap, 0x06, write_data_1lar, write_data_2lar, write_data_3lar, write_data_4lar]
		    dxl_io_1.sync_write(sync_write_address, sync_write_data)

#		    print "sync_write done, position control"
#		    i=i+1
#		    pub.publish(val)
		
#		    if  (current_time-last_time)>5:
		    if i==37952:
#		    	i=1
#		    	j=j+1
#			if j==5: break
			torque_response= dxl_io_0.set_torque_enabled(1,0)
			print "torque disable rhy response", torque_response
			time.sleep(1) 
			torque_response= dxl_io_0.set_torque_enabled(2,0)
			print "torque disable rhr response", torque_response
			time.sleep(1)
		        torque_response= dxl_io_0.set_torque_enabled(3,0)
			print "torque disable rhp response", torque_response
			time.sleep(1) 
			torque_response= dxl_io_0.set_torque_enabled(4,0)
			print "torque disable rkp response", torque_response
			time.sleep(1)
		        torque_response= dxl_io_0.set_torque_enabled(5,0)
			print "torque disable rap response", torque_response
			time.sleep(1) 
			torque_response= dxl_io_0.set_torque_enabled(6,0)
			print "torque disable rar response", torque_response
			time.sleep(1)
			torque_response= dxl_io_1.set_torque_enabled(1,0)
			print "torque disable lhy response", torque_response
			time.sleep(1) 
			torque_response= dxl_io_1.set_torque_enabled(2,0)
			print "torque disable lhr response", torque_response
			time.sleep(1)
		        torque_response= dxl_io_1.set_torque_enabled(3,0)
			print "torque disable lhp response", torque_response
			time.sleep(1) 
			torque_response= dxl_io_1.set_torque_enabled(4,0)
			print "torque disable lkp response", torque_response
			time.sleep(1)
		        torque_response= dxl_io_1.set_torque_enabled(5,0)
			print "torque disable lap response", torque_response
			time.sleep(1) 
			torque_response= dxl_io_1.set_torque_enabled(6,0)
			print "torque disable lar response", torque_response
			time.sleep(1)
			print "sync_write done, position control", i
			break

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
        dxl_io_0 = dynamixel_io.DynamixelIO(port_name0, baud_rate)		#left hip
        dxl_io_1 = dynamixel_io.DynamixelIO(port_name1, baud_rate)		#right hip
#        dxl_io_2 = dynamixel_io.DynamixelIO(port_name2, baud_rate)		#right knee
#        dxl_io_3 = dynamixel_io.DynamixelIO(port_name3, baud_rate)		#left knee
    except dynamixel_io.SerialOpenError, soe:
        print 'ERROR:', soe
    else:
	athena_walk()
