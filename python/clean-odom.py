from dataclasses import dataclass
import sys
import yaml

class Data:
	seq: int = -1
	secs: int = -1
	nsecs: int = -1
	frame_id: str = ""
	child_frame_id: str = ""
	position_x: float = 0.0
	position_y: float = 0.0
	position_z: float = 0.0
	orientation_x: float = 0.0
	orientation_y: float = 0.0
	orientation_z: float = 0.0
	orientation_w: float = 0.0
	covariance: list = []
	linear_x: float = 0.0
	linear_y: float = 0.0
	linear_z: float = 0.0
	angular_x: float = 0.0
	angular_y: float = 0.0
	angular_z: float = 0.0
	twist_covariance: list = []
	
	def __str__(self):
		return "seq" + str(self.seq)


def read_file(file_name):
	with open(file_name, 'r') as file:
		data = file.read()
	return data

def clear(block):
	
	clean = Data()
	
	data = yaml.safe_load(block)

	clean.seq = data['header']['seq']
	clean.secs = data['header']['stamp']['secs']
	clean.nsecs = data['header']['stamp']['nsecs']
	clean.frame_id = data['header']['frame_id']
	clean.child_frame_id = data['child_frame_id']
	clean.position_x = data['pose']['pose']['position']['x']
	clean.position_y = data['pose']['pose']['position']['y']
	clean.position_z = data['pose']['pose']['position']['z']
	clean.orientation_x = data['pose']['pose']['orientation']['x']
	clean.orientation_y = data['pose']['pose']['orientation']['y']
	clean.orientation_z = data['pose']['pose']['orientation']['z']
	clean.orientation_w = data['pose']['pose']['orientation']['w']
	clean.covariance = data['pose']['covariance']
	clean.linear_x = data['twist']['twist']['linear']['x']
	clean.linear_y = data['twist']['twist']['linear']['y']
	clean.linear_z = data['twist']['twist']['linear']['z']
	clean.angular_x = data['twist']['twist']['angular']['x']
	clean.angular_y = data['twist']['twist']['angular']['y']
	clean.angular_z = data['twist']['twist']['angular']['z']
	clean.twist_covariance = data['twist']['covariance']
		
	return clean


#main

#source file
file_name = 'odom.out'

#reads imu_data.txt file
data = read_file(file_name)

#cleans header
blocks = data.strip().split('---')

for block in blocks:
	if block:
		#print(block)
		teste = clear(block)
		
print(teste)
