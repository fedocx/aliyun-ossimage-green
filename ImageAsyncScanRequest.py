#coding=utf-8
# 异步图片检测服务接口, 需要根据该接口返回的taskId来轮询结果

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkgreen.request.v20180509 import ImageAsyncScanRequest
import json
import time
import uuid
import datetime

import configparser

class ImageAsyncScan:
    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read("aliyun.ak.conf")
        # 请替换成你自己的accessKeyId、accessKeySecret, 您可以类似的配置在配置文件里面，也可以直接明文替换
        self.clt = client.AcsClient(cf.get("AK", "accessKeyId"), cf.get("AK", "accessKeySecret"),'cn-shanghai')
        region_provider.modify_point('Green', 'cn-shanghai', 'green.cn-shanghai.aliyuncs.com')
        self.request = ImageAsyncScanRequest.ImageAsyncScanRequest()
        self.request.set_accept_format('JSON')
        self.request.set_read_timeout(20)
        self.request.set_connect_timeout(20)

    def check(self,list):
        self.request.set_content(bytearray(json.dumps({"tasks": list, "scenes": ["porn"]}), "utf-8"))
        response = self.clt.do_action_with_exception(self.request)
        print(response)
        result = json.loads(response)
        if 200 == result["code"]:
            taskResults = result["data"]
            for taskResult in taskResults:
                if(200 == taskResult["code"]):
                    taskId = taskResult["taskId"]
                    print(taskId)
        return taskId




