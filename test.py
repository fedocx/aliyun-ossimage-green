#coding=utf-8
# 同步图片检测服务接口, 会实时返回检测的结果

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkgreen.request.v20180509 import ImageSyncScanRequest
import json
import uuid
import datetime

import configparser
cf = configparser.ConfigParser()
cf.read("aliyun.ak.conf")
# 请替换成你自己的accessKeyId、accessKeySecret, 您可以类似的配置在配置文件里面，也可以直接明文替换
clt = client.AcsClient(cf.get("AK", "accessKeyId"), cf.get("AK", "accessKeySecret"),'cn-shanghai')
region_provider.modify_point('Green', 'cn-shanghai', 'green.cn-shanghai.aliyuncs.com')
request = ImageSyncScanRequest.ImageSyncScanRequest()
request.set_accept_format('JSON')

# 同步现支持单张图片，即一个task
# task1 = {"dataId": str(uuid.uuid1()),
#          "url":"http://xxxx.jpg",
#          "time":datetime.datetime.now().microsecond
#         }
task1 = {'dataId': '804bd560-ecdd-11e9-9f01-d8cb8a717eff', 'url': 'https://qc-res.oss-cn-hangzhou.aliyuncs.com/covermap/0101cc5b3d564ba7914d4c5725cf6634.jpeg', 'time': 589173}

request.set_content(bytearray(json.dumps({"tasks": [task1], "scenes": ["porn"]}), "utf-8"))

response = clt.do_action(request)
print(response)
result = json.loads(response)
if 200 == result["code"]:
    taskResults = result["data"]
    for taskResult in taskResults:
        if (200 == taskResult["code"]):
            sceneResults = taskResult["results"]

            for sceneResult in sceneResults:
                scene = sceneResult["scene"]
                suggestion = sceneResult["suggestion"]
                print(suggestion)
                print(scene)
                #根据scene和suggetion做相关的处理
                #do something
