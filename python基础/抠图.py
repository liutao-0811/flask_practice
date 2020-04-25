"""
步骤：
1、导入模块
2、加载模型
3、获取文件列表
4、抠图
"""
import os
import paddlehub as hub
#加载模型
humanseg = hub.Module(name='deeplabv3p_xception65_humanseg')
#获取文件目录
path = r'C:\Users\13664\Desktop\img'
#获取目录下的文件
files = os.listdir(path)
imgs = []
for i in files:
    imgs.append(path+i)
#抠图
results = humanseg.segmentation(data={'image':imgs})
