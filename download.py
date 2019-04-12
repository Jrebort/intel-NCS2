#!/usr/bin/python2.7 

import os
import sys 

net = ["densenet-121","densenet-161","densenet-169","densenet-201","squeezenet1.0",
		"vgg16","vgg19","inception-resnet-v2","googlenet-v1","googlenet-v2","googlenet-v4",
		"alexnet","resnet-50","resnet-101","resnet-152","googlenet-v3"]
for i in net:
	os.system("sudo proxychains /opt/intel/computer_vision_sdk/deployment_tools/model_downloader/downloader.py --name "+i+" -o ./model")

