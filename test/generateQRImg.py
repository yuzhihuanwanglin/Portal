"""
    -*- coding: utf-8 -*-
    @Time    : 2021/3/31 20:20
    @Author  : zhongxiaoting
    @Site    : 
    @File    : generateQRImg.py.py
    @Software: PyCharm
"""
import qrcode
from PIL import Image
from qrcode import ERROR_CORRECT_H


def create_qrcode(url, filename):
    """制作带logo的二维码"""
    qr = qrcode.QRCode(version=1, error_correction=ERROR_CORRECT_H, box_size=10, border=4) # 设置容错率
    # 添加路由数据
    qr.add_data(url)
    # 填充数据
    qr.make(fit=True)
    # 生成彩色图片
    img = qr.make_image()
    img = img.convert("RGBA")
    # 添加logo图片,打开图片
    icon = Image.open(filename)
    # 获取图片大小
    img_w, img_h = img.size
    # 设置logo大小
    factor = 4
    size_w = int(img_w / factor)
    size_h = int(img_w / factor)
    icon_w, icon_h = icon.size
    if icon_w > size_w:
        icon_w = size_w
    if icon_h > size_h:
        icon_h = size_h
    # 重新设置logo尺寸
    icon = icon.resize((icon_w, icon_h), Image.ANTIALIAS)
    # 得到画图x,y的坐标，居中显示
    w = int((img_w - icon_w) / 2)
    h = int((img_h - icon_h) / 2)
    # 制作成彩色图片
    icon = icon.convert("RGBA")
    newing = Image.new("RGBA", (icon_w + 8, icon_h + 8), (255, 255, 255))
    # 黏贴logo图片
    img.paste(newing, (w - 4, h - 4), newing)
    img.paste(icon, (w, h), icon)
    # 保存
    img.save('qr.png', quality=1000)


if __name__ == '__main__':
    create_qrcode("http://python3web.com", 'logo.jpeg')
    print("完成")

