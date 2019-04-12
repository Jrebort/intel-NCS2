#!/usr/bin/python2.7 

import os
import sys

net_list = ["densenet-121","densenet-161","densenet-169","densenet-201","squeezenet-1",
		"vgg16","vgg19","inception-resnet-v2","googlenet-v1","googlenet-v2","googlenet-v4",
		"alexnet","resnet-50","resnet-101","resnet-152","googlenet-v3"]

root_dir = "/home/chenweiwei/study/NCS2/IR"
bmp_path = "/opt/intel/computer_vision_sdk/deployment_tools/demo/car_1.bmp"
for i in net_list:
	os.system("/home/chenweiwei/inference_engine_samples_build/intel64/Release/classification_sample -i "+ bmp_path 
		+" -m "+ root_dir +"/"+ i +".xml -d MYRIAD")
