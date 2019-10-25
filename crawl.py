import requests 
from bs4 import BeautifulSoup
h={'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36'}
r=requests.get('https://www.bilibili.com'.headers=h)
c=r.content
soup=BeautifulSoup(c,'html.parser')
f=soup.find('ul',{'class':'bili-wrapper'})
print(f)
items=f.find_all('li',{'class':'fl clear'})
for(i,item) in enumerate (items):
    title=item.find('h3').find('a').text
    intro=item.find('div',{'class':'d2'}).text
    img=item.find('img')['src']
print(i,title,'\t', intro, img)