
#%%
get_ipython().run_line_magic('matplotlib', 'inline')
import requests
from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import numpy as np


#%%
url = 'http://www.uh.edu/~cldue/texts/demeter.html'
r = requests.get(url)
r.encoding = 'utf-8'
html = r.text
soup = BeautifulSoup(html)
body = soup.find('div', {'class': 'Section1'})
body = body.text


#%%
body = re.sub('\\n', ' ', body)
body = re.sub('\\xa0', '', body)
body = re.sub('[^A-z\s]', '', body)
body = re.sub('\[', '', body)
body = re.sub('\]', '', body)
words = body.split(' ')


#%%
for word in words:
    if word == '':
        words.remove(word)


#%%
word_index = sorted(list(set(words)))
indexer = dict(zip(word_index, np.arange(len(word_index))))
labeler = dict(zip(np.arange(len(word_index)), word_index))
counter = np.zeros(len(word_index))


#%%
for word in words:
    counter[indexer[word]] += 1


#%%
top_10 = np.argsort(counter)[-20:][::-1]
labels = [labeler[i] for i in top_10]
counts = list(counter[top_10])


#%%
plt.bar(labels, counts)
plt.show()


#%%
len(words)
