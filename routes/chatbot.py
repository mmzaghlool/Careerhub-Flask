# importing lib
import requests
import sys
import webbrowser
from bs4 import BeautifulSoup
import bs4
import requests
from . import routes

# chat list
@routes.route('/chatbot/<query>', methods=['GET'])
def stackoverflow(query):
   try:
      # quary
      quary = query
      # request
      res = requests.get('https://stackoverflow.com/search?q='+quary)
      # res.raise_for_status()
      soup = bs4.BeautifulSoup(res.text, "html.parser")
      linkElements = soup.select('.question-hyperlink')
      linkToOpen = min(2, len(linkElements))

      # scrab in the first scrab
      res2 = requests.get('https://stackoverflow.com'+linkElements[0].get('href'))

      # requested soup
      soup2 = BeautifulSoup(res2.text, 'html.parser')

      # answer for quary
      answer = soup2.find('div', class_='answercell post-layout--right').div

      # linkes inside the answer

      # link_list = answer.find_all('a')
      # print (soup3)
      # print (link_list[2].get('href'))


      try:
         insidelinks = answer.find_all('a')
      except:
         insidelinks = 'null'

      # share link for the answer

      shareLink = soup2.find('div', class_='post-menu')

      # answer vote
      vote = soup2.findAll(
         'div', class_='js-vote-count grid--cell fc-black-500 fs-title grid fd-column ai-center')


      # print (answer.text)
      # print (vote.text)
      insideLinkF = []
      link_ = ''
      for link in insidelinks:
         link_ = link.get('href')
         if link_[0] is '/':
            insideLinkF.append('https://stackoverflow.com'+link.get('href'))
         else:
            insideLinkF.append(link.get('href'))

      # print ('https://stackoverflow.com'+linkElements[0].get('href'))
      # webbrowser.open('https://stackoverflow.com'+linkElements[0].get('href'))


      state = {
         "question": quary,
         "answer": answer.text,
         "vote": vote[1].text,
         'insidelinkes': insideLinkF,
         'shareLink': 'https://stackoverflow.com'+linkElements[0].get('href')
      }
      # print(state)
      # print(answer.text)
      # print(vote[1].text)
      # print('https://stackoverflow.com'+linkElements[0].get('href'))
      # print(insideLinkF)
      # print('https://stackoverflow.com'+linkElements[0].get('href'))

      return {
         "success": True,
         "message": "Answer sent",
         "data": state,
      }, 200
   except Exception as NMN:
      return {
         "success": False,
         "message": "{0}".format(NMN)
      }, 400  
