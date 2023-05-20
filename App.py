from flask import Flask,render_template,url_for,request
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from newspaper import Article
import nltk
nltk.download('punkt')


app = Flask(__name__, template_folder="template")
@app.route("/",methods=['GET'])
def home():
	return render_template("index.html")

#################POLITICS###########################################

p_site = 'https://news.google.com/rss/search?q=politics '
p_op = urlopen(p_site)  # Open that site
p_rd = p_op.read()  # read data from site
p_op.close()  # close the object
p_sp_page = soup(p_rd, 'xml')  # scrapping data from site
p_news_list = p_sp_page.find_all('item')  # finding news

P_link=[]
P_title=[]
P_image_link=[]
P_best_summary=[]
c=0
try:
  for news in p_news_list:
    c+=1
    if c <=5:
      print('Title: ',news.title.text)
      P_title.append(' '.join(news.title))
      print('News Link: ',news.link.text)
      P_link.append(' '.join(news.link))
      news_data = Article(news.link.text)
      news_data.download()
      news_data.parse()
      news_data.nlp()
      P_best_summary.append(''.join(news_data.summary))
      print('news_summary:',news_data.summary)
      print("News Poster Link: ",news_data.top_image)
      P_image_link.append(news_data.top_image)

except:
  pass

#################FINANCE###########################################

f_site = 'https://news.google.com/rss/search?q=finance '
f_op = urlopen(f_site)  # Open that site
f_rd = f_op.read()  # read data from site
f_op.close()  # close the object
f_sp_page = soup(f_rd, 'xml')  # scrapping data from site
f_news_list = f_sp_page.find_all('item')  # finding news

F_link=[]
F_title=[]
F_image_link=[]
F_best_summary=[]
c=0
try:
  for news in f_news_list:
    c+=1
    if c <=5:
      print('Title: ',news.title.text)
      F_title.append(' '.join(news.title))
      print('News Link: ',news.link.text)
      F_link.append(' '.join(news.link))
      news_data = Article(news.link.text)
      news_data.download()
      news_data.parse()
      news_data.nlp()
      F_best_summary.append(''.join(news_data.summary))
      print('news_summary:',news_data.summary)
      print("News Poster Link: ",news_data.top_image)
      F_image_link.append(news_data.top_image)

except:
  pass

#################SPORTS###########################################

s_site = 'https://news.google.com/rss/search?q=sports '
s_op = urlopen(s_site)  # Open that site
s_rd = s_op.read()  # read data from site
s_op.close()  # close the object
s_sp_page = soup(s_rd, 'xml')  # scrapping data from site
s_news_list = s_sp_page.find_all('item')  # finding news

S_link=[]
S_title=[]
S_image_link=[]
S_best_summary=[]
c=0
try:
  for news in s_news_list:
    c+=1
    if c <=5:
      print('Title: ',news.title.text)
      S_title.append(' '.join(news.title))
      print('News Link: ',news.link.text)
      S_link.append(' '.join(news.link))
      news_data = Article(news.link.text)
      news_data.download()
      news_data.parse()
      news_data.nlp()
      S_best_summary.append(''.join(news_data.summary))
      print('news_summary:',news_data.summary)
      print("News Poster Link: ",news_data.top_image)
      S_image_link.append(news_data.top_image)

except:
  pass



#################ENTERTAINMENT###########################################

e_site = 'https://news.google.com/rss/search?q=entertainment '
e_op = urlopen(e_site)  # Open that site
e_rd = e_op.read()  # read data from site
e_op.close()  # close the object
e_sp_page = soup(e_rd, 'xml')  # scrapping data from site
e_news_list = e_sp_page.find_all('item')  # finding news

E_link=[]
E_title=[]
E_image_link=[]
E_best_summary=[]
c=0
try:
  for news in e_news_list:
    c+=1
    if c <=5:
      print('Title: ',news.title.text)
      E_title.append(' '.join(news.title))
      print('News Link: ',news.link.text)
      E_link.append(' '.join(news.link))
      news_data = Article(news.link.text)
      news_data.download()
      news_data.parse()
      news_data.nlp()
      E_best_summary.append(''.join(news_data.summary))
      print('news_summary:',news_data.summary)
      print("News Poster Link: ",news_data.top_image)
      E_image_link.append(news_data.top_image)

except:
  pass

@app.route("/politics",methods=['GET'])
def politics():
     return render_template("summary_page.html",len=len(P_best_summary),best_summary=P_best_summary,image=P_image_link,link=P_link,title=P_title)

@app.route("/finance",methods=['GET'])
def finance():
     return render_template("summary_page.html",len=len(F_best_summary),best_summary=F_best_summary,image=F_image_link,link=F_link,title=F_title)

@app.route("/sports",methods=['GET'])
def sports():
     return render_template("summary_page.html",len=len(S_best_summary),best_summary=S_best_summary,image=S_image_link,link=S_link,title=S_title)

@app.route("/entertainment",methods=['GET'])
def entertainment():
     return render_template("summary_page.html",len=len(E_best_summary),best_summary=E_best_summary,image=E_image_link,link=E_link,title=E_title)



if __name__=='__main__':
	app.run(debug=True)