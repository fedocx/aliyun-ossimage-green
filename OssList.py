# -*- coding: utf-8 -*-
import oss2
from itertools import islice
import uuid
import datetime

import configparser
import re

class osslist:
    def __init__(self):
        cf = configparser.ConfigParser()
        cf.read("aliyun.ak.conf")
        # 阿里云主账号AccessKey拥有所有API的访问权限，风险很高。强烈建议您创建并使用RAM账号进行API访问或日常运维，请登录 https://ram.console.aliyun.com 创建RAM账号。
        self.auth = oss2.Auth(cf.get("AK", "accessKeyId"), cf.get("AK", "accessKeySecret"))
        # Endpoint以杭州为例，其它Region请按实际情况填写。
        self.bucket = oss2.Bucket(self.auth, 'http://oss-cn-hangzhou.aliyuncs.com', 'qc-res')
    def CovermapList(self):
        list = []
        BaseUrl = "https://qc-res.oss-cn-hangzhou.aliyuncs.com/"
        for b in oss2.ObjectIterator(self.bucket,prefix="covermap"):
        # for b in islice(oss2.ObjectIterator(self.bucket,prefix="covermap"),3):
            url = BaseUrl + str(b.key)
            if bool(re.match(".*(jpeg|png)",url)):
                task = {"dataId": str(uuid.uuid1()),
                        "url" : url,
                        "time":datetime.datetime.now().microsecond
                        }
                list.append(task)
        return list
    def HeadmapList(self):
        list = []
        BaseUrl = "https://qc-res.oss-cn-hangzhou.aliyuncs.com/"
        for b in oss2.ObjectIterator(self.bucket,prefix="headmap"):
            # for b in islice(oss2.ObjectIterator(self.bucket,prefix="covermap"),3):
            url = BaseUrl + str(b.key)
            if bool(re.match(".*(jpeg|png)",url)):
                task = {"dataId": str(uuid.uuid1()),
                        "url" : url,
                        "time":datetime.datetime.now().microsecond
                        }
                list.append(task)
        return list

    def ImageListSave(self,list):
        # list = ','.join(list)
        list = str(list)
        list = bytes(list,encoding='utf-8')
        with open('ImageList.txt','w') as f:
            f.write(list)

if __name__ == "__main__":
    oss = osslist()
    list = oss.HeadmapList()
    print(list[-1])
    print(len(list))

    # oss.ImageListSave(list)

