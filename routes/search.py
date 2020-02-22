import requests
import sys
import webbrowser
import bs4

res = requests.get('https://stackoverflow.com/search?q='+''.join(sys.argv[1:]))
f= open("guru99.txt","w+")
#print(res.url)
#print(res.text)
res.raise_for_status()
# print(res.raise_for_status())
f.write(res.text)
f.close

soup = bs4.BeautifulSoup(res.text,"html.parser")
# print(soup.prettify())
linkElements = soup.select('.question-hyperlink')
linkToOpen = min(5,len(linkElements))
print (linkElements)
print (linkToOpen)

for i in range(linkToOpen):
  webbrowser.open('https://stackoverflow.com'+linkElements[i].get('href'))
