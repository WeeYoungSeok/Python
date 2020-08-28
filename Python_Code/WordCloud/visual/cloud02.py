# -*- coding:utf-8 -*-

from wordcloud import WordCloud, ImageColorGenerator
import json
import numpy as np
from PIL import Image
from wordcloud import STOPWORDS
import matplotlib.pyplot as plt




alice_mask = np.array(Image.open("alice_mask.png"))
stopwords = set(STOPWORDS)
stopwords.add("said")

alice_mask

with open('webtoons.json', encoding='utf-8') as file:
    webtoon = json.load(file)

res = dict()
for webtoon in webtoon['webtoons']:
    res[webtoon['title']] = int(float(webtoon['star']) *100)

str_res = str(res)




wc = WordCloud(font_path='Goyang.ttf',background_color='white', max_words=30, mask=alice_mask, stopwords=stopwords).generate(str_res)
print(wc)

plt.figure(figsize=(8,8))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()




