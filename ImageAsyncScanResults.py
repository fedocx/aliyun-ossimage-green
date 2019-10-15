#coding=utf-8
# 同步图片检测服务接口, 会实时返回检测的结果

from aliyunsdkcore import client
from aliyunsdkcore.profile import region_provider
from aliyunsdkgreen.request.v20180509 import ImageAsyncScanResultsRequest
import json
import uuid
import datetime

import configparser
class ImageAsyncScanResult:
    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read("aliyun.ak.conf")
        # 请替换成你自己的accessKeyId、accessKeySecret, 您可以类似的配置在配置文件里面，也可以直接明文替换
        self.clt = client.AcsClient(cf.get("AK", "accessKeyId"), cf.get("AK", "accessKeySecret"),'cn-shanghai')
        region_provider.modify_point('Green', 'cn-shanghai', 'green.cn-shanghai.aliyuncs.com')
        self.request = ImageAsyncScanResultsRequest.ImageAsyncScanResultsRequest()
        self.request.set_accept_format('JSON')
        self.request.set_read_timeout(20)
        self.request.set_connect_timeout(20)
    def GetTaskId(self):
        with open('tasklist.txt','r') as f:
            data = f.read()
            data = data.split(',')
            return data
    def GetResult(self,taskidlist):
        self.request.set_content(bytearray(json.dumps(taskidlist), "utf-8"))

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
                        # print(response)
                        if scene != "porn":
                            print(response)
                            print(scene)
                        #根据scene和suggetion做相关的处理
                        #do some
if __name__ == '__main__':
    a = ImageAsyncScanResult()
    tasklist = a.GetTaskId()
    print(len(tasklist))
    # for i in tasklist:
    #     i = [i]
    #     a = ImageAsyncScanResult()
    #     a.GetResult(i)

