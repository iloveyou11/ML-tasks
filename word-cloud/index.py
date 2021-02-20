# -*- coding: utf-8 -*-
import os
import jieba
import random
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud,ImageColorGenerator

def getPath(name):
  return os.path.join(os.path.dirname(__file__),name)

# 自定义颜色函数
def random_color(word, font_size, position, orientation, font_path, random_state):
	s = 'hsl(0, %d%%, %d%%)' % (random.randint(60, 80), random.randint(60, 80))
	print(s)
	return s

# 打开文本，这里可以自定义文本数据
text = open(getPath('./asset/Chinese.txt')).read()

# 中文分词，如果上面加载的是英文词库，则不需要分词
text = ' '.join(jieba.cut(text))
print(text[:100])

# 生成对象
mask = np.array(Image.open(getPath('./asset/black_mask.png')))
# mask = np.array(Image.open(getPath('./asset/color_mask.png')))

wc = WordCloud(
  # color_func=random_color, # 自定义颜色函数，可选
  mask=mask, # 可以增加遮罩层，可选
  font_path=os.path.join(getPath('./asset/Hiragino.ttf')), 
  width=800, 
  height=600, 
  mode='RGBA', 
  background_color=None
).generate(text)

# 根据图片来生成颜色
# image_colors = ImageColorGenerator(mask)
# wc.recolor(color_func=image_colors)

# 显示词云
plt.imshow(wc, interpolation='bilinear')
plt.axis('off')
plt.show()