# coding: utf-8

text = open("article.txt",'r')
text = text.read()


for char in '-,.\n"':
    text = text.replace(char,' ')
text = text.lower()

for digit in '0123456789':
    text = text.replace(digit,' ')
    
stopwords=[' what ',' who ',' the ',' a ',' at ',' is ',' he ',' for ',' of ',' to ',' we ',' were ',' not ',' and ',' or ',' are ']

for word in stopwords:
    text = text.replace(word,' ')

word_list = text.split()

d = {}

for word in word_list:
    d[word] = d.get(word,0)+1
    
word_freq = []
for key, value in d.items():
    word_freq.append((value, key))
    
word_freq.sort(reverse = True)

def Convert(tup, di): 
    di = dict(tup) 
    return di 

tup = word_freq
di ={}

word_freq = Convert(tup,di)

title = max(word_freq.items(), key = lambda x: x[0])

w = title[1]

print("Suggestion of Title for your artice is: ")

import requests 
from bs4 import BeautifulSoup


url_base = 'https://www.title-generator.com/best-online-title-generator.html?qs='
url = url_base + w + '&page=1'

fileOpen = requests.get(url)

soup = BeautifulSoup(fileOpen.text,"html.parser")

page_content = soup.find(class_ = "table table-striped")
page_txt = page_content.find_all("td")

for item in page_txt:
	print(item.contents[0])


