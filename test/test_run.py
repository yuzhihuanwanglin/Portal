"""
    -*- coding: utf-8 -*-
    @Time    : 2021/4/12 17:43
    @Author  : zhongxiaoting
    @Site    : 
    @File    : test_run.py
    @Software: PyCharm
"""

import cv2
import requests

url = "http://localhost:8000/serviceApp/facedetect/"

# 上传图片并检测
tracker = None
img_path = "home.jpg"
files = {
    "image": ("filename2", open(img_path, "rb"), "image/jpeg")
}
req = requests.post(url, data=tracker, files=files).json()
print("获取图片信息：{}".format(req))

# 将检测结果显示在图像上
image_to_read = cv2.imread(img_path)
for (w, x, y, z) in req['faces']:
    cv2.rectangle(image_to_read, (w, x), (y, z), (0, 255, 0), 2)

cv2.imshow("检测图像：", image_to_read)
cv2.waitKey(0)