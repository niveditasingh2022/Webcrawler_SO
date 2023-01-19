from gettext import find
import requests
from bs4 import BeautifulSoup
import urllib.parse
import re
from pprint import pprint
def stackoverflow_crawler():
    name = []
code = []
i=1
search1 = str(input('enter the word to search'))
search1= "+".join(search1.split())
address = "https://stackoverflow.com/search?q=" + search1
print(address)
res = requests.get(address)
soup = BeautifulSoup(res.text, "html.parser")
s = soup.select(".s-post-summary")
f = open("Crawler.text", "w+")
for que in s:
    if (que.select_one('.s-link')!=None):
        s2 = que.select_one('.s-link')
    elif(que.select_one('answer-hyperlink')!= None):
        s2 = que.select_one('answer-hyperlink')
    print("Question-",i , s2.getText())
    que_strng = "Question-"+ str(s2)
    start = que_strng.find('/questions')
    end = que_strng.find('?r', start)
    question = que_strng[start:end]
    newaddress = "https://stackoverflow.com" + str(question)
    print(newaddress)
    i=i+1
#def stackoverflow_answer_crawler():
    res1 = requests.get(newaddress)
    soup1 = BeautifulSoup(res1.text, "html.parser")
    #pprint(soup1.prettify()[:2000])
    answer = soup1.find("div",{"class": "answer"})
    answertext = answer.find("div", {"class": "s-prose js-post-body"})
    for a1 in answertext:
        print(answertext.get_text().strip())
        print("******************************************************************************************************************************\n")
