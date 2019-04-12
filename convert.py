#!/usr/bin/python2.7 

import os
import sys 

net_list = ["densenet-121","densenet-161","densenet-169","densenet-201","squeezenet-1",
		"vgg16","vgg19","inception-resnet-v2","googlenet-v1","googlenet-v2","googlenet-v4",
		"alexnet","resnet-50","resnet-101","resnet-152","googlenet-v3"]

convert = "/opt/intel/computer_vision_sdk/deployment_tools/model_optimizer/mo_caffe.py"

class model_pre:

	def __init__(self,model_fullname):

		self.fullname = model_fullname

	def pre_solve(self):

		model = self.fullname[:self.fullname.find("-")]
		para = self.fullname[self.fullname.find("-") + 1:]
		return model,para
	"""	print model,para """

	def path_solve(self,model_name,model_para):
		root_dir = "/home/chenweiwei/study/NCS2/model/classification/"+ model_name +"/"+ model_para +"/caffe"
		model_path = root_dir +"/"+ self.fullname +".caffemodel"
		para_path = root_dir +"/"+ self.fullname +".prototxt"

		return model_path,para_path
		"""	print model
		if os.path.exists(root_dir):
			print root_dir """

	def model_run(self,model_path,para_path):

		os.system("python3 "+ convert +" --input_model "+ model_path +" --input_proto "+ para_path 
			+ " --data_type FP16 -o ./IR")

def main():
	for i in net_list:
		net = model_pre(i)
		model_name,model_para = net.pre_solve()
		model_path,para_path = net.path_solve(model_name,model_para)
		net.model_run(model_path,para_path)

if __name__ == '__main__':
	main()