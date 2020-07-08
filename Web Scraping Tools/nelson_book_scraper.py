#%% imports and inis

import requests
from bs4 import BeautifulSoup
import mechanicalsoup
import re

login_url = 'https://www.mynelson.com/mynelson/staticcontent/html/PublicLogin.html'
post_url ='https://www.mynelson.com/mynelson/service/json_authentication_check?_=1593770358577&keepMeLogin=false'
book_url = 'https://www.mynelson.com/mynelson/staticcontent/html/ExplorerProduct.html?pid=1199631&isbn13=9780176520625'
sample_url = 'https://www.mynelson.com/mynelson/staticcontent/html/Dashboard.html'

pdf_url = 'https://www.mynelson.com/mynelson/staticcontent/html/OpenLink.html?linkid=2122517&levelID={}&isbn13=9780176529369&accessURL=http://k12resources.nelson.com/science/9780176529369/student'.format(732002)

headers = {
    'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'
}

payload = {
	'captchaArg': "",
    'pswd': "cict4808181",
    'userName': "cictacademic@gmail.com"
}

#%%

browser = mechanicalsoup.StatefulBrowser()
browser.open(login_url)

#%%
with requests.Session() as s:
    r = s.post(login_url)
    print(r)
    # r2 = s.post(post_url, data = payload)
    # print(r2.content)



#%% Plug those chapter section ids in this api call

api_call = 'https://www.mynelson.com/mynelson/service/productdetail/links.json?productid=1199631&levelid={}'.format(chapter_section)

# %% Scrape local html file

local_file = r"C:\Users\dougl\Programming\html-files\chembook.html"

# Intermediate step to crack open a local html
page = open(local_file, encoding="utf8")
# r = requests.get(page.read())


# c = r.content
soup = BeautifulSoup(page,'html.parser')
soup

# set as string to run regex
soupy_string = str(soup.contents)
listChapterids = re.findall('linkid=\"(\d+)\"', soupy_string)
# %% Got the soup, time to strip out chapter ids

for link in soup.find_all("div", {"class":"jspContainer"}):
    print(link.get('title'))


# %%
soup.find_all('linkid')

# %%
