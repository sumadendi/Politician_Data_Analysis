# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bayVhbYFXO8n0enT8EWWeGRTHoLzUefA
"""

from google.colab import files
uploaded = files.upload()

import pandas as pd
import io
  
df = pd.read_csv(io.BytesIO(uploaded['df (4).csv']))
df = df.astype(str)
print(df)

!pip install wordcloud
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt

profs = []
for x in df.professions:
  profs.append(x)
print(profs)
#text = profs
#wordcloud = WordCloud().generate(text[:5])
wordcloud = WordCloud().generate(" ".join(profs))
#width = 1000, height = 500

repdf = df[df.party.eq("Republican")]
repwordcloud = repdf.professions
repdf

demdf = df[df.party.eq("Democratic")]
demwordcloud = demdf.professions
demdf

rep_profs = []
for x in repdf.professions:
  rep_profs.append(x)
wordcloud = WordCloud(width = 1000, height = 500, background_color = "white").generate(" ".join(rep_profs))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()

from google.colab import files
#mask = files.upload()

import os
import matplotlib.pyplot as plt
os.system('curl -O https://static.wikia.nocookie.net/logopedia/images/8/88/Republican_%28GOP%29_logo.jpeg')
mask = plt.imread('Republican_%28GOP%29_logo.jpeg')
mask.shape[1]
#data
#elephant = np.array(mask)

wc = WordCloud(mask = mask, width = mask.shape[1], height = mask.shape[0], background_color = "white", contour_width = 2, contour_color = 'grey').generate(" ".join(rep_profs))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.show()
wc.to_file("rep_cloud.png")
print(wc.words_.keys())

dem_profs = []
for x in demdf.professions:
  dem_profs.append(x)
cloud = WordCloud(width = 1000, height = 500, background_color = "white").generate(" ".join(dem_profs))
plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
plt.show()

os.system('curl -O https://i1.wp.com/www.cardinalandcream.info/wp-content/uploads/2019/10/CollegeDemocrats.jpg')
dem_mask = plt.imread('CollegeDemocrats.jpg')
print(mask)

cloud = WordCloud(mask = dem_mask, width = mask.shape[1], height = mask.shape[0], background_color = "white", contour_width = 2, contour_color = 'grey').generate(" ".join(dem_profs))
plt.imshow(cloud, interpolation='bilinear')
plt.axis("off")
plt.show()
print(cloud.words_.keys())

cloud.to_file("dem_cloud.png")