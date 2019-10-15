from itertools import islice
# from ImageSyncScanRequest import ImageScan
from ImageAsyncScanRequest import ImageAsyncScan
import oss2
from OssList  import osslist
import uuid
import datetime

oss = osslist()
list = oss.HeadmapList()
# print(list[-1])
# print(len(list))
# imagescan = ImageScan()
# response = imagescan.check(list)
# print(response)
# task = ImageAsyncScan()
# a = task.check([list[0]])


sum = 0
tasklist = []
for i in list:
    sum = sum + 1
    # if sum < 13418:
    #     continue
    i = [i]
    print(sum ,i)
    imagescan = ImageAsyncScan()
    tasklist1 = imagescan.check(i)
    tasklist.append(tasklist1)
data = ','.join(tasklist)
with open('tasklist.txt', 'w') as tasklistfile:
    tasklistfile.write(data)



