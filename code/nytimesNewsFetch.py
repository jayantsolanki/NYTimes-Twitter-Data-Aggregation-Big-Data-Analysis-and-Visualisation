
# -*- coding: utf-8 -*-

# <span style="color:red;font-weight:bold">Jayant Solanki</span>
# <hr/>
# ## <span style="float:left">Finding trending words from a news topic in NYTimes website.</span>
# ### <span style="float:right">Using nytimes articles API to fetch articles for a particular search topic</span>
# <hr/>

# In[2]:


#Background: The nytimes api doesn't returns full article body, just the snippet of it each returned
# so, I have to write the code to fetch the weburl for each article, then perfrom further requests to those url and 
#fetch the story body of each article
import requests # for performing html request to nytimes API
from datetime import datetime
from time import sleep
import lxml.html as html # for scrapping the content of the article URL of nytimes
import json


# In[3]:


# Each API keys can provide 10000 response hits
topic = "trade+war"#topic to be looked for
apikey = "527c18ffc4e648cb936f582a0e264ff1"
fl = "snippet,web_url"#selective attributes of json response
pageNo = "0"#initial page is 0, articles fetched using api are grouped in 10 per page starting 0 and upto page 100
dateRange = ["20180331", "20180401", "20180402", "20180403", "20180404", "20180405", "20180406", "20180407"]# can be changed t any period


# In[4]:


#this function parse the json response from nytimes and create new dictionary using two attributes only
def parse_articles(articles):
    '''
    This function takes in a response to the NYT api and parses
    the articles into a list of dictionaries
    '''
    news = []
    fetch = articles['response']['docs']
    for i in range(0,len(fetch)):
        dic = {}
#         print(fetch[i])
        dic['web_url'] = fetch[i]['web_url']
        if fetch[i]['snippet'] is not None:
            dic['snippet'] = fetch[i]['snippet']
#         dic['url'] = i['web_url']
        news.append(dic)
    return(news)


# In[5]:


# this function perfrom request to nytimes api using the paramters passed and returns the parseed responsed to the caller function
def get_articles(topic, begin_date, end_date, fl, apikey):
    all_articles = []#stores all articles for a particular day
    page = 0
    while(page<100):
        sleep(1)
#     for page in range(0,100): #NYT limits pages to first 100 pages starting page 0, each page has 10 articles max
        try:
            
            url = "http://api.nytimes.com/svc/search/v2/articlesearch.json?q="+topic+"&begin_date="+begin_date+"&end_date="+end_date+"&fl="+fl+"&page="+str(page)+"&api-key="+apikey
            print(url)
            requestArticles = requests.get(url)
            data = requestArticles.json()
            if len(data["response"]["docs"])>0:
                all_articles.append(parse_articles(data))
#                 print(data)
            else:# checks if further pages have no articles to show, if yes then break the loop and return the fetched articles
                print(parse_articles(data))
                break
        except:
            print("You called the api way to fast, Dude, trying again")
            print(data)
#             page = page - 1
            sleep(1)
            continue#try again
        print("Page: "+str(page))
#         break
        page=page+1
    return(all_articles)


# In[7]:


#caller function
processArticles = []
for i in range(0,7):
    datetimeobject = datetime.strptime(dateRange[i],'%Y%m%d')
    beginDate = datetimeobject.strftime('%m-%d-%Y')
    datetimeobject = datetime.strptime(dateRange[i+1],'%Y%m%d')
    endDate = datetimeobject.strftime('%m-%d-%Y')
    print("Fetching articles for Data period: " + beginDate + " - "+ endDate)
    processArticles = get_articles(topic, dateRange[i], dateRange[i+1],fl, apikey)
    if(len(processArticles)>0):
#         try:
#             dataToWrite = processArticles
# #             print(dataToWrite)
#         except:
#             print(len(processArticles))
#             print(processArticles)
#             print(processArticles[0])
#             break
        with open("FinalData/"+topic+dateRange[i]+".txt", 'w') as outfile:#used for storing snippets
            for item in processArticles:
                for articles in item:
#                     print(articles)
		    dta = str(articles["snippet"].encode("ascii", "ignore"))
                    outfile.write(dta)
                    outfile.write("\n")
        with open("FinalData/"+topic+dateRange[i]+"-full.txt", 'w') as outfile:#used for storing full articles
            for item in processArticles:
                for articles in item:
                    fullpage = requests.get(articles["web_url"])
                    htmlbody = html.fromstring(requests.get(articles["web_url"]).content)
                    output = "".join(htmlbody.xpath('//p[contains(@class,"story-body-text")]//text()'))#scrapper
#                     print(output+"\n\n")
#                     output = output.decode('utf8').encode('latin1').decode('utf8')
                    output = str(output.encode("ascii", "ignore"))#since the body has lots of escape characters, I have to convert
    # utf-8 response into ascii using ignore flag to bypass those escape characters
                    outfile.write(output[2:-1])
                    outfile.write("\n")
    else:
        print("Insufficient data for date: "+beginDate+" to save")
#     break
# print(processArticles[0][0:-1])


# In[ ]:


# /usr/local/hadoop/bin/hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.8.3.jar -input /user/jayant/input/ -output /user/jayant/output_new2 -mapper /home/jayant/wordcount_mapper.py -reducer /home/jayant/wordcount_reducer.py -numReduceTasks 1

