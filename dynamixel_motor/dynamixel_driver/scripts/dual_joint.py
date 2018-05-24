#!/usr/bin/env python
__author__ = 'Ash'
__copyright__ = '...'

#__license__ = 'BSD'
__maintainer__ = 'Ashrarul Sifat'
__email__ = 'ashrar7@vt.edu'


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
#import dynamixel_io
from dynamixel_driver.dynamixel_const import *
from sensor_msgs.msg import JointState
#from numpy import zeros, array, linspace
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

currentJointState = JointState()
def jointStatesCallback(msg):
    global currentJointState
    currentJointState = msg

if __name__ == '__main__':
    port_name_0='/dev/ttyUSB0'
    port_namespace_0='ttyUSB0'
    port_name_1='/dev/ttyUSB1'
    port_namespace_1='ttyUSB1'
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
    r=0.126
    m=842
    I=m*r*r
    c=r*m*9.81
#    sync_write_address= [0x66, 0x00]		#current goal
    try:
	rospy.init_node('dual_joint', anonymous=True)
	rospy.Subscriber("minie/joint_cmd", JointState, jointStatesCallback)   
#	name: [r_hip_y0, r_hip_r1, r_hip_p2, r_knee_p3, r_ankle_p4, r_ankle_r5, l_hip_y6, l_hip_r7, l_hip_p8,
#  l_knee_p9, l_ankle_p10, l_ankle_r11, torso_y12, r_shoulder_p13, r_shoulder_r14, r_shoulder_y15,
#  r_elbow_p16, l_shoulder_p17, l_shoulder_r18, l_shoulder_y19, l_elbow_p_20]
#	position: [0.0, 0.0, -0.34906585039886573, 0.6981317007977315, -0.34906585039886573, 0.0, 0.0, 0.0, -0.34906585039886573, 0.6981317007977315, -0.34906585039886573, 0.0, 0.0, 0.3740066054098645, -0.49960922502963645, 0.03811450020505214, -1.2552722139608568, 0.0, 0.08726646259971643, 0.0, -0.34906585039886573]
#	velocity: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0379350803579471, 0.027854058598427905, 0.03089937889047767, -0.10561999594783833, 0.0, 0.0, 0.0, 0.0]
#	effort: [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

	 
        dxl_io_0 = dynamixel_io.DynamixelIO(port_name_0, baud_rate)
        dxl_io_1 = dynamixel_io.DynamixelIO(port_name_1, baud_rate)
    except dynamixel_io.SerialOpenError, soe:
        print 'ERROR:', soe
    else:
        print 'Turning left torque %s for motor %d' % (torque_on, motor_id)
        if dxl_io_0.ping(motor_id):
        	torque_response= dxl_io_0.set_torque_enabled(4,1)
		print "torque enable4 response", torque_response
		time.sleep(1)
		torque_response= dxl_io_0.set_torque_enabled(3,1)
		print "torque enable3 response", torque_response
		time.sleep(1) 
                torque_response= dxl_io_0.set_torque_enabled(2,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_0.set_torque_enabled(1,1)
		print "torque enable1 response", torque_response
		time.sleep(3)
                print 'left arm done'
        else:
            print 'ERROR: motor %d did not respond. Make sure to specify the correct baudrate.' % motor_id
            
        print 'Turning right torque %s for motor %d' % (torque_on, motor_id)
        if dxl_io_1.ping(motor_id):
        	torque_response= dxl_io_1.set_torque_enabled(4,1)
		print "torque enable4 response", torque_response
		time.sleep(1)
		torque_response= dxl_io_1.set_torque_enabled(3,1)
		print "torque enable3 response", torque_response
		time.sleep(1) 
                torque_response= dxl_io_1.set_torque_enabled(2,1)
		print "torque enable2 response", torque_response
		time.sleep(1) 
		torque_response= dxl_io_1.set_torque_enabled(1,1)
		print "torque enable1 response", torque_response
		time.sleep(3)
                print 'right arm done'
        else:
            print 'ERROR: motor %d did not respond. Make sure to specify the correct baudrate.' % motor_id
            
            

	#write_address= [0x74, 0x00]
#	write_data = [0xAA, 0x02, 0x00, 0x00 ]
#	write_response = self.dxl_io.write(1,write_address, write_data)
#	print "write done, response:", write_response

	# write current goal to motor 1
#	write_address= [0x66, 0x00]
	sync_write_address= [0x74, 0x00]		#position
	val = 2048
	nbits = 32
	write_data_whole= twos_complement(val, nbits)
	write_data_L=write_data_whole & 0xFF
	write_data_H = (write_data_whole>>8) & 0xFF
	write_data = [write_data_L, write_data_H ]
#	write_response = dxl_io_0.write(1,write_address, write_data)
#	write_response = dxl_io_1.write(1,write_address, write_data)
#	print "write done, response:", write_response
###################################################################
#	val1=val
#	val2=-val1;
#	#write_.append(val1)
#	write_data_whole1= twos_complement(val1, nbits)
#	write_data_L1=write_data_whole1 & 0xFF
#	write_data_H1 = (write_data_whole1>>8) & 0xFF
#	#for motor2 value
#	write_data_whole2= twos_complement(val2, nbits)
#	write_data_L2=write_data_whole2 & 0xFF
#	write_data_H2 = (write_data_whole2>>8) & 0xFF
#	sync_write_data = [0x02, 0x00, 0x01, write_data_L1, write_data_H1, 0x02, write_data_L2, write_data_H2]
#	dxl_io.sync_write(sync_write_address, sync_write_data)
#	print "sync_write done, current control"
##############################################################################
	last_time=time.time()
#	write_=[]
#	read_cur1=[]
#	read_cur2=[]
#	read_pos1=[]
#	read_vel2=[]
#	write_time=[]
#	read_timecur1=[]
#	read_timecur2=[]
#	read_time2=[]
#	read_time3=[]
#	torque_1=[]
	data=[]
	last_read_vel=0
	last_read_time=last_time
	#rr = rospy.Rate(500) # 10hz
#	while not rospy.is_shutdown() :
#	#read position
#		read_response=dxl_io.read(1,DXL_PRESENT_POSITION,4)
#		read_val_pos= read_response[9] | (read_response[10] << 8)| (read_response[11] << 16)| (read_response[12] << 24)
#		print read_val_pos

	while not rospy.is_shutdown() :
		current_time =time.time()
#		print "position", currentJointState.position
		data=currentJointState.position
		data=np.array(data, dtype=np.float32)
		data=data*2048/3.14159
		print "data position", data
#		print currentJointState.velocity
#		print currentJointState.effort				
		############### right arm ####################################
#		val=20*math.sin(3.1416*current_time)-20
#		val=20*math.sin(3.1416*0.5*current_time)+20 	##right rsp
		val_rsp=int(round(val+data[13]))
		write_data_whole1= twos_complement(val_rsp, nbits)
    		write_data_1rsp = write_data_whole1 & 0xFF
    		write_data_2rsp = (write_data_whole1>>8) & 0xFF
    		write_data_3rsp = (write_data_whole1>>16) & 0xFF
    		write_data_4rsp = (write_data_whole1>>32) & 0xFF
		#val=-20
#		val=int(round(val))
#		write_data_whole= twos_complement(val, nbits)
#		write_data_L=write_data_whole & 0xFF
#		write_data_H = (write_data_whole>>8) & 0xFF
#		write_data = [write_data_L, write_data_H ]
#		write_response = dxl_io_1.write(1,write_address, write_data)
#		print "right arm write done, response:", write_response
		######write to motor 2############
#		val=20*math.sin(3.1416*current_time)+20
#		val=5*math.sin(3.1416*0.5*current_time)-15		##right rsr
		val_rsr=int(round(val+data[14]))
		write_data_whole1= twos_complement(val_rsr, nbits)
    		write_data_1rsr = write_data_whole1 & 0xFF
    		write_data_2rsr = (write_data_whole1>>8) & 0xFF
    		write_data_3rsr = (write_data_whole1>>16) & 0xFF
    		write_data_4rsr = (write_data_whole1>>32) & 0xFF
		#val=20
#		val=int(round(val))
#		write_data_whole= twos_complement(val, nbits)
#		write_data_L=write_data_whole & 0xFF
#		write_data_H = (write_data_whole>>8) & 0xFF
#		write_data = [write_data_L, write_data_H ]
#		write_response = dxl_io_1.write(2,write_address, write_data)
#		print "write done, response:", write_response
#		######write to motor 3############
##		val=5*math.sin(3.1416*current_time)-5
#		val=5*math.sin(3.1416*current_time)+5		##right rsy
		val_rsy=int(round(val+data[15]))
		write_data_whole1= twos_complement(val_rsy, nbits)
    		write_data_1rsy = write_data_whole1 & 0xFF
    		write_data_2rsy = (write_data_whole1>>8) & 0xFF
    		write_data_3rsy = (write_data_whole1>>16) & 0xFF
    		write_data_4rsy = (write_data_whole1>>32) & 0xFF
#		#val=-5
#		val=int(round(val))
#		write_data_whole= twos_complement(val, nbits)
#		write_data_L=write_data_whole & 0xFF
#		write_data_H = (write_data_whole>>8) & 0xFF
#		write_data = [write_data_L, write_data_H ]
#		write_response = dxl_io_1.write(3,write_address, write_data)
#		print "write done, response:", write_response
##		########## write to motor 4 ##############
#		val=20*math.sin(3.1416*current_time)-10
#		val=10*math.sin(3.1416*0.5*current_time)+5		##right	re	
		val_re=int(round(val-data[16]))
		write_data_whole1= twos_complement(val_re, nbits)
    		write_data_1re = write_data_whole1 & 0xFF
    		write_data_2re = (write_data_whole1>>8) & 0xFF
    		write_data_3re = (write_data_whole1>>16) & 0xFF
    		write_data_4re = (write_data_whole1>>32) & 0xFF
    		sync_write_data = [0x04, 0x00,0x01, write_data_1rsp, write_data_2rsp, write_data_3rsp, write_data_4rsp, 0x02, write_data_1rsr,write_data_2rsr, write_data_3rsr, write_data_4rsr, 0x03, write_data_1rsy, write_data_2rsy, write_data_3rsy, write_data_4rsy, 0x04, write_data_1re,write_data_2re, write_data_3re, write_data_4re ]
    		dxl_io_1.sync_write(sync_write_address, sync_write_data)
		#val=0
#		val=int(round(val))
#		write_data_whole= twos_complement(val, nbits)
#		write_data_L=write_data_whole & 0xFF
#		write_data_H = (write_data_whole>>8) & 0xFF
#		write_data = [write_data_L, write_data_H ]
##		write_response = dxl_io_1.write(4,write_address, write_data)
#		print "write arm done, response:", write_response
		################ left arm ###############################3
#		val=20*math.sin(3.1416*0.5*current_time)-15		## lsp
		val_lsp=int(round(val+data[17]))
		write_data_whole1= twos_complement(val_lsp, nbits)
    		write_data_1lsp = write_data_whole1 & 0xFF
    		write_data_2lsp = (write_data_whole1>>8) & 0xFF
    		write_data_3lsp = (write_data_whole1>>16) & 0xFF
    		write_data_4lsp = (write_data_whole1>>32) & 0xFF
		#val=-20
#		val=int(round(val))
#		write_data_whole= twos_complement(val, nbits)
#		write_data_L=write_data_whole & 0xFF
#		write_data_H = (write_data_whole>>8) & 0xFF
#		write_data = [write_data_L, write_data_H ]
##		write_response = dxl_io_0.write(1,write_address, write_data)
#		print "left arm write done, response:", write_response
		######write to motor 2############
#		val=5*math.sin(3.1416*0.5*current_time)+15		## lsr
		val_lsr=int(round(val+data[18]))
		write_data_whole1= twos_complement(val_lsr, nbits)
    		write_data_1lsr = write_data_whole1 & 0xFF
    		write_data_2lsr = (write_data_whole1>>8) & 0xFF
    		write_data_3lsr = (write_data_whole1>>16) & 0xFF
    		write_data_4lsr = (write_data_whole1>>32) & 0xFF
		#val=20
#		val=int(round(val))
#		write_data_whole= twos_complement(val, nbits)
#		write_data_L=write_data_whole & 0xFF
#		write_data_H = (write_data_whole>>8) & 0xFF
#		write_data = [write_data_L, write_data_H ]
#		write_response = dxl_io_0.write(2,write_address, write_data)
#		print "write done, response:", write_response
#		######write to motor 3############
#		val=5*math.sin(3.1416*current_time)-5		## lsy
		val_lsy=int(round(val+data[19]))
		write_data_whole1= twos_complement(val_lsy, nbits)
    		write_data_1lsy = write_data_whole1 & 0xFF
    		write_data_2lsy = (write_data_whole1>>8) & 0xFF
    		write_data_3lsy = (write_data_whole1>>16) & 0xFF
    		write_data_4lsy = (write_data_whole1>>32) & 0xFF
		#val=-5
#		val=int(round(val))
#		write_data_whole= twos_complement(val, nbits)
#		write_data_L=write_data_whole & 0xFF
#		write_data_H = (write_data_whole>>8) & 0xFF
#		write_data = [write_data_L, write_data_H ]
		#write_response = dxl_io_0.write(3,write_address, write_data)
#		print "write done, response:", write_response
##		########## write to motor 4 ##############
#		val=10*math.sin(3.1416*0.5*current_time)-8		##le
		val_le=int(round(val+data[20]))
		write_data_whole1= twos_complement(val_le, nbits)
    		write_data_1le = write_data_whole1 & 0xFF
    		write_data_2le = (write_data_whole1>>8) & 0xFF
    		write_data_3le = (write_data_whole1>>16) & 0xFF
    		write_data_4le = (write_data_whole1>>32) & 0xFF
    		sync_write_data = [0x04, 0x00,0x01, write_data_1lsp, write_data_2lsp, write_data_3lsp, write_data_4lsp, 0x02, write_data_1lsr,write_data_2lsr, write_data_3lsr, write_data_4lsr, 0x03, write_data_1lsy, write_data_2lsy, write_data_3lsy, write_data_4lsy, 0x04, write_data_1le,write_data_2le, write_data_3le, write_data_4le ]
    		dxl_io_0.sync_write(sync_write_address, sync_write_data)
    		print "sync write done, response:"
		#val=0
#		val=int(round(val))
#		write_data_whole= twos_complement(val, nbits)
#		write_data_L=write_data_whole & 0xFF
#		write_data_H = (write_data_whole>>8) & 0xFF
#		write_data = [write_data_L, write_data_H ]
#		write_response = dxl_io_0.write(4,write_address, write_data)
#		print "left write done, response:", write_response
		##############for sync write###############################################
#		val1=int(round(val))
#		val2=-val1;
#		write_.append(val1)
#		write_data_whole1= twos_complement(val1, nbits)
#		write_data_L1=write_data_whole1 & 0xFF
#		write_data_H1 = (write_data_whole1>>8) & 0xFF
#		#for motor2 value
#		write_data_whole2= twos_complement(val2, nbits)
#		write_data_L2=write_data_whole2 & 0xFF
#		write_data_H2 = (write_data_whole2>>8) & 0xFF
#		write_data = [write_data_L, write_data_H ]
		#write_response = dxl_io.write(1,write_address, write_data)
#		sync_write_data = [0x02, 0x00, 0x01, write_data_L1, write_data_H1, 0x02, write_data_L2, write_data_H2]
#		self.dxl_io.sync_write(sync_write_address, sync_write_data)
#		print "sync_write done, current control"
#		write_time.append(time.time())
#		#print "write done, response:", write_response
################################################################################################
		############### data collection ############################
#		read_response=dxl_io.read(1,DXL_PRESENT_CURRENT,2)
#		read_val1= read_response[9] | (read_response[10] << 8)
#		read_val=twos_complement(read_val1, nbits)
#		read_cur1.append(read_val)
#		read_timecur1.append(read_response[13])
##		read_response=dxl_io.read(2,DXL_PRESENT_CURRENT,2)
##		read_val1= read_response[9] | (read_response[10] << 8)
##		read_val=twos_complement(read_val1, nbits)
##		read_cur2.append(read_val)
##		read_timecur2.append(read_response[13])
#		#read position
#		read_response=dxl_io.read(1,DXL_PRESENT_POSITION,4)
#		read_val_pos= read_response[9] | (read_response[10] << 8)| (read_response[11] << 16)| (read_response[12] << 24)
#		print read_val_pos
#		#read_val_pos=twos_complement(read_val3, 32)
#		read_pos1.append(read_val_pos)
#		read_time3.append(read_response[15])
#		#read vel
#		read_response=dxl_io.read(1,DXL_PRESENT_VELOCITY,4)
#		read_val2= read_response[9] |  (read_response[10] << 8)
#		read_velocity=twos_complement(read_val2, nbits)
#		print "present velocity", read_velocity
#		read_vel2.append(read_velocity)
#		read_time2.append(read_response[15])
#		theta=2*3.1416*read_val_pos/4096
#		tau1=I*(read_velocity-last_read_vel)*0.023981/(read_response[15]-last_read_time)#-c*math.sin(theta)
#		print math.sin(theta)		
#		print (read_velocity-last_read_vel)
#		#print (read_response[15]-last_read_time)
#		last_read_vel=read_velocity
#		last_read_time=read_response[15]
#		torque_1.append(tau1)
##		read_response=self.dxl_io.read(2,DXL_PRESENT_CURRENT,2)
##		read_val2= read_response[9] |  (read_response[10] << 8)
##		read_val=self.twos_complement(read_val2, nbits)
##		read_2.append(read_val)
##		read_time2.append(read_response[13])
#		#print "read done, response:", read_response
		##################### data collection done ########################################
		
		if  (current_time-last_time)>50:
			print "time up"
			val = 0
			write_data_whole= twos_complement(val, nbits)
			write_data_L=write_data_whole & 0xFF
			write_data_H = (write_data_whole>>8) & 0xFF
			write_data = [write_data_L, write_data_H ]
#			write_response = dxl_io_0.write(1,write_address, write_data)
#			write_response = dxl_io_0.write(2,write_address, write_data)
#			write_response = dxl_io_0.write(3,write_address, write_data)
#			write_response = dxl_io_0.write(4,write_address, write_data)
#			write_response = dxl_io_1.write(1,write_address, write_data)
#			write_response = dxl_io_1.write(2,write_address, write_data)
#			write_response = dxl_io_1.write(3,write_address, write_data)
#			write_response = dxl_io_1.write(4,write_address, write_data)
#			print "write done, response:", write_response
#			write_data_whole= self.twos_complement(val, nbits)
#			write_data_L=write_data_whole & 0xFF
#			write_data_H = (write_data_whole>>8) & 0xFF
###############################################################################################
#			sync_write_data = [0x02, 0x00, 0x01, val, val, 0x02, val, val]
#			dxl_io.sync_write(sync_write_address, sync_write_data)
#			print "sync write done"
#			torque_response= dxl_io.set_torque_enabled(2,0)
#			print "torque enable2 response", torque_response
#			time.sleep(1) 
###############################################################################################
			######### torque disable ##################################
			torque_response= dxl_io_0.set_torque_enabled(1,0)
			torque_response= dxl_io_0.set_torque_enabled(2,0)
			torque_response= dxl_io_0.set_torque_enabled(3,0)
			torque_response= dxl_io_0.set_torque_enabled(4,0)
			torque_response= dxl_io_1.set_torque_enabled(1,0)
			torque_response= dxl_io_1.set_torque_enabled(2,0)
			torque_response= dxl_io_1.set_torque_enabled(3,0)
			torque_response= dxl_io_1.set_torque_enabled(4,0)
			print "torque disable response"#, torque_response
			########################################################3
##			print "data write", write_
##			print "data write_time", write_time
#			print "data read motor 1curr", read_cur1
##			print "data read motor 2curr", read_cur2 
##			print "data read_timecurr", read_timecur1,read_timecur2
#			print "data read_timevel", read_time2
#			print "data read_timepos", read_time3
#			print "torque", torque_1
#			print "velocity", read_vel2
#			print "read position1", read_pos1
##			print "data read motor 2",  read_2
##			print "data read_time2", read_time2
			##############################################################
			break
		#rr.sleep()

	
	# set goal position on multiple motors
#	sync_write_address= [0x74, 0x00]
#	sync_write_data = [0x04, 0x00, 0x01, 0xAA, 0x00, 0x00, 0x00, 0x02, 0xAA, 0x00, 0x00, 0x00 ]
#	self.dxl_io.sync_write(sync_write_address, sync_write_data)
#	print "sync_write done, position control"

	#set goal current on multiple motors
#	sync_write_address= [0x66, 0x00]
#	sync_write_data = [0x02, 0x00, 0x01, write_data_L, write_data_H, 0x02, write_data_L, write_data_H]
#	self.dxl_io.sync_write(sync_write_address, sync_write_data)
#	print "sync_write done, current control"
    

