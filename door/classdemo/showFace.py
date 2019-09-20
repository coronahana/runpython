#!/usr/bin/python
# -*- coding: UTF-8 -*-
#-*- coding:utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("gbk")
import os  
import pygame  
from pygame.locals import *
pygame.init()
from PIL import Image, ImageDraw, ImageFont
img = Image.open("head.jpg")#250*250
jgz = Image.open("face.jpg")#101*113
img.paste(jgz,(73,47))#左右，上下
#img.show()
draw = ImageDraw.Draw(img)
ttfront = ImageFont.truetype('simhei.ttf', 24)
draw.text((32, 190),"我的内心毫无波动\n   甚至还想笑".decode('gbk'),fill=(0,0,0), font=ttfront)
#img.show()
img.save("Python生成的表情包.jpg")

