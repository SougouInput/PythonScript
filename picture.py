# -*- coding: utf-8 -*-
#! /usr/bin/env python
"""
Created on Thu Jun  7 10:32:14 2018

@author: May.golddemon@gmail.com
"""

from PIL import Image,ImageDraw,ImageFont

im=Image.open('D:/File/python/cute.jpg')
text='author是个菜鸡'
draw=ImageDraw.Draw(im)
t_font=ImageFont.truetype('D:/File/python/simkai.ttf',55)
draw.text((110,520),text,fill=(255,33,33),font=t_font)
im.show()
im.save("./cute_text.jpg")