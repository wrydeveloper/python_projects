import requests
import re
from bs4 import BeautifulSoup
import urllib.request

#https://www.jianshu.com/p/c77d3eb145ea

# def getPage(url):
#     respose = requests.get(url)
#     if respose.status_code == 200:
#         return respose.text
#
# if __name__ == "__main__":
#     print(getPage('https://www.jianshu.com/p/c77d3eb145ea'))

# msg = requests.get(u'https://www.jianshu.com/p/c77d3eb145ea')
#
# print(msg)
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
# page = urllib.request.Request('https://www.jianshu.com/p/c77d3eb145ea',headers=headers)
#
# html = urllib.request.urlopen(page).read()
#
# print(html)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}

page = requests.get(u'http://open.iciba.com/dsapi/', headers=headers, timeout=0.001)

# re.findall('^[\d|\D]?\、\w?[\u4e00-\u9fa5]*$', page.text)
# html = page.text
# soup = BeautifulSoup(html, 'html.parser')
# print(soup.find(class="show-content-free"))
contents = page.json()

try:

print(page.encoding)


