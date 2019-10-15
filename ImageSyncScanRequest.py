#coding=utf-8
# 同步图片检测服务接口, 会实时返回检测的结果

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkgreen.request.v20180509 import ImageSyncScanRequest
import json
import uuid
import datetime

import configparser
class ImageScan:
    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read("aliyun.ak.conf")
        # 请替换成你自己的accessKeyId、accessKeySecret, 您可以类似的配置在配置文件里面，也可以直接明文替换
        self.clt = client.AcsClient(cf.get("AK", "accessKeyId"), cf.get("AK", "accessKeySecret"),'cn-shanghai')
        region_provider.modify_point('Green', 'cn-shanghai', 'green.cn-shanghai.aliyuncs.com')
        self.request = ImageSyncScanRequest.ImageSyncScanRequest()
        self.request.set_accept_format('JSON')

    def check(self,list):
        sum = 0
        for i in list:
            sum = sum + 1
            i = [i]
            print(sum ,i)
            self.request.set_content(bytearray(json.dumps({"tasks": i,"scenes": ["porn"]}), "utf-8"))
            response = self.clt.do_action_with_exception(self.request)
            result = json.loads(response)
            if 200 == result["code"]:
                taskResults = result["data"]
                for taskResult in taskResults:
                    if (200 == taskResult["code"]):
                        sceneResults = taskResult["results"]
                        for sceneResult in sceneResults:
                            scene = sceneResult["scene"]
                            suggestion = sceneResult["suggestion"]
                            if suggestion != "pass":
                                print(suggestion,taskResult["url"])
                            # print(scene)
                            #根据scene和suggetion做相关的处理
                            #do something
