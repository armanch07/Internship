#!/usr/bin/env python
# coding: utf-8

# # 1. Write a python program to display all the header tags from wikipedia.org.

# In[86]:


from bs4 import BeautifulSoup
import requests


# In[88]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[89]:


soup = BeautifulSoup(page.content)
print(soup)


# In[90]:


titles = soup.find_all(['h1', 'h2','h3','h4','h5','h6'])
print('List all the header tags :', *titles, sep='\n\n')


# # 2. Write a python program to display IMDB’s Top rated 100 movies’ data (i.e. name, rating, year of release) and make data frame.

# In[91]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

link = "https://www.imdb.com/chart/top/"
page = requests.get(link)
page


# In[77]:


bs = BeautifulSoup(page.content, "html.parser")
print(bs)


# In[78]:


print(soup.prettify())


# In[94]:


#scrapped movie names
movie_name = bs.find_all('td', class_="titleColumn")
movie_name


# In[96]:


# Parse movie name

movies = []

for movie in movie_name:
    movie = movie.get_text().replace('\n', "") #Removing extra line
    movie = movie.strip ("  ") #Removing extra spaces
    movies.append(movie)
movies


# In[97]:


# Movies Rating

movie_rating = bs.find_all('td', class_="ratingColumn imdbRating")
movie_rating


# In[100]:


# Parse movie rating

ratings = []

for rating in movie_rating:
    rating = rating.get_text().replace('\n', '') #Removing extra line
    ratings.append(rating)
ratings


# In[107]:


# Movies Release Year

release_year = bs.find_all('span', class_="secondaryInfo")
release_year


# In[109]:


# Parse release year

year = []

for i in release_year:
    year.append (i.text)
year


# In[111]:


data = pd.DataFrame()
data['Movie Name'] = movies
data['Movie Rating'] = ratings
data['Relear Year'] = year
data.head(100)


# # 3. Write a python program to display IMDB’s Top rated 100 Indian movies’ data (i.e. name, rating, year of release) and make data frame.

# In[113]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[114]:


url = 'https://www.imdb.com/india/top-rated-indian-movies/'
page = requests.get(url)
page


# In[119]:


bs = BeautifulSoup(page.content,"html.parser")
print(bs.prettify)


# In[120]:


# scrapped top indian movie name

indian_movie = bs.find_all('td',class_="titleColumn")
indian_movie


# In[122]:


# extract the movie name

movies = []

for movie in indian_movie:
    movie = movie.get_text().replace('\n', " ")
    movie = movie.strip("  ")
    movies.append(movie)
movies


# In[124]:


# Indian movie rating

indian_movies_rating = bs.find_all('td',class_="ratingColumn imdbRating")
indian_movies_rating


# In[125]:


# Extract Rating

ratings = []

for rating in indian_movies_rating:
    rating = rating.get_text().replace('\n',' ')
    ratings.append(rating)
ratings


# In[126]:


# Indian Movies relase year

indian_movies_release_year = bs.find_all('span', class_="secondaryInfo")
indian_movies_release_year


# In[127]:


# extract release year

year = []

for i in indian_movies_release_year:
    year.append(i.text)
year


# In[128]:


data = pd.DataFrame()
data['Movies Name'] = movies
data['Rating'] = ratings
data['Release Year'] = year
data.head(100)


# # 4. Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:
# 
# a) Top 10 ODI teams in men’s cricket along with the records for matches, points and rating.
# 
# b) Top 10 ODI Batsmen in men along with the records of their team and rating.
# 
# c) Top 10 ODI bowlers along with the records of their team and rating

# In[144]:


from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


# In[153]:


url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'
page = requests.get(url)
bs = BeautifulSoup(page.text, "html.parser")
print(bs.prettify)


# In[154]:


teams = []

for i in bs.find_all('td',class_="rankings-block__banner--team-name"):
    teams.append(i.text.split('\n')[-2])


# In[157]:


for i in bs.find_all('td', class_="table-body__cell rankings-table__team"):
    teams.append(i.text.split('\n') [-2])


# In[160]:


for i in bs.find_all('span',class_='u-hide-phablet'):
    teams.append(i.text)


# In[161]:


teams=teams[:10]
teams


# In[167]:


match = bs.find('td',class_="rankings-block__banner--matches").text
match


# In[168]:


matches=[]
for i in bs.find_all('td',class_="table-body__cell u-center-text"):
    matches.append(i.text)


# In[169]:


played=matches[::2]
played.insert(0,match)


# In[170]:


played=played[:10]
played


# In[171]:


point = bs.find('td',class_="rankings-block__banner--points").text
point


# In[172]:


points = matches[1::2]
points.insert(0,point)
points = points[:10]
points


# In[177]:


ratings=[]
for i in bs.find_all('td', class_="rankings-block__banner--rating u-text-right"):
                       ratings.append(i.text.replace("\n","").replace(" ",""))


# In[178]:


ratings


# In[180]:



for i in bs.find_all('td', class_="table-body__cell u-text-right rating"):
    ratings.append(i.text.replace(" ","").replace("\n",""))


# In[181]:


ratings=ratings[:10]
ratings


# In[182]:


Odi_Mens_Team = pd.DataFrame({"Team":teams,"Matches":played,"Points":points,"Ratings":ratings})
Odi_Mens_Team


# # B) Top 10 ODI Batsmen in men along with the records of their team and rating.

# In[183]:


url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi'
page = requests.get(url)
bs = BeautifulSoup(page.text, "html.parser")
print(bs.prettify)


# In[188]:


p=[]
for i in bs.find_all("div",class_="rankings-block__banner--name"):
    p.append(i.text)

player=[]
player.append(p[0])

for i in  bs.find_all('td',class_="table-body__cell name"):
    player.append(i.text.replace("\n",""))

player


# In[201]:


ctry=bs.find("div",class_="rankings-block__banner--nationality")
team=[]
team.append(ctry.text.replace("\n",""))

for i in bs.find_all('span',class_="table-body__logo-text"):
    team.append(i.text.replace("\n",""))

team


# In[202]:


r=bs.find("div",class_="rankings-block__banner--rating").text


rating=[]
rating.append(r)


for i in bs.find_all('td',class_='table-body__cell u-text-right rating'):
    rating.append(i.text)

rating


# In[203]:


Odi_Top_Batsman = pd.DataFrame({ 'Player':player[:10], 'Team':team[:10], 'Rating':rating[:10]})


# In[204]:


Odi_Top_Batsman


# # C) Top 10 ODI bowlers along with the records of their team and rating

# In[205]:


url = 'https://www.icc-cricket.com/rankings/mens/player-rankings/odi'
page = requests.get(url)
bs = BeautifulSoup(page.text, "html.parser")
print(bs.prettify)


# In[213]:


pl=[]
[pl.append(i.text) for i in bs.find_all('div',class_='rankings-block__banner--name')]
pl[1]


# In[217]:


player=[]
for i in bs.find_all('td',class_='table-body__cell name'):
    player.append(i.text.replace("\n",""))


# In[218]:


player=player[9:18]
player.insert(0,pl[1])
player


# In[219]:


ct=[]
for i in bs.find_all('div',class_='rankings-block__banner--nationality'):
    ct.append(i.text.replace('\n',""))

ct[1] 

country=[]
for i in bs.find_all('span',class_='table-body__logo-text'):
    country.append(i.text.replace("\n",""))
country=country[9:18]
country.insert(0,ct[1])

country


# In[221]:


rt=[]
for i in bs.find_all('div',class_='rankings-block__banner--rating'):
    rt.append(i.text.replace("\n",""))
rt[1]


# In[228]:


rating=[]
for i in bs.find_all('td',class_='table-body__cell u-text-right rating'):
    rating.append(i.text.replace("\n",""))
rating=rating[9:18]
rating.insert(0,rt[1])

odiTopBowler=pd.DataFrame({
    "Player":player,
    "Team":country,
    "rating":rating
})


# In[229]:


odiTopBowler


# # 5) Write a python program to scrape cricket rankings from icc-cricket.com. You have to scrape:

# # A) Top 10 ODI teams in women’s cricket along with the records for matches, points and rating

# In[232]:


url = 'https://www.icc-cricket.com/rankings/womens/team-rankings/odi'
page = requests.get(url)
bs = BeautifulSoup(page.text, "html.parser")
print(bs.prettify)


# In[246]:


team=[]
for i in bs.find_all('span',class_="u-hide-phablet"):
    team.append(i.text)

team


# In[235]:


mt = bs.find('td',class_='rankings-block__banner--matches').text

mt


# In[248]:


matches = []
for i in bs.find_all('td',class_='table-body__cell u-center-text'):
    matches.append(i.text)
mts = matches[::2]
mts.insert(0,mt)


# In[239]:


pt = bs.find('td',class_='rankings-block__banner--points').text
pt


# In[253]:


pts = matches[1::2]
pts.insert(0,pt)
pts = pts[:10]
pts


# In[242]:


rt = bs.find('td',class_='rankings-block__banner--rating u-text-right').text.replace("\n","").replace(" ","")
rt


# In[243]:


rts = []
rts.append(rt)
for i in bs.find_all('td',class_="table-body__cell u-text-right rating"):
    rts.append(i.text.replace("\n","").replace(" ",""))
rts


# In[255]:


odiWTeam = pd.DataFrame({"Teams":team[:10], "Matches":mts[:10], "Points":pts[:10], "Ratings":rts[:10]})


# In[256]:


odiWTeam


# # B) Top 10 women’s ODI players along with the records of their team and rating.
# 

# In[257]:


url = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
bs = BeautifulSoup(url.text,'html.parser')

pl=[]

for i in bs.find_all("div",class_='rankings-block__banner--name'):
    pl.append(i.text)
pl 


# In[258]:


pls = []
for i in bs.find_all("td",class_="table-body__cell name"):
    pls.append(i.text.replace("\n",""))
    
player=pls[:9]
player.insert(0,pl[0])
player


# In[260]:


ct=[]
for i in bs.find_all('div',class_="rankings-block__banner--nationality"):
    ct.append(i.text.replace("\n"," "))
ct[0]


# In[261]:


pt=[]
for i in bs.find_all('div',class_="rankings-block__banner--rating"):
    pt.append(i.text.replace("\n",""))
pt[0]


# In[264]:


cts=[]
for i in bs.find_all("span",class_="table-body__logo-text"):
    cts.append(i.text.replace("\n",""))
cts
country=cts[:9]
country.insert(0,ct[0])
country


# In[265]:


pts = []
for i in bs.find_all("td",class_="table-body__cell u-text-right rating"):
    pts.append(i.text.replace("\n",""))
pts
rating=pts[:9]
rating.insert(0,pt[0])
rating


# In[270]:


odi_top_women = pd.DataFrame({
    'Player':player,
    "Teams":country,
    "Rating":rating
})

odi_top_women


# # C)  Top 10 women’s ODI all-rounder along with the records of their team and rating.
# 

# In[271]:


url = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi")
bs = BeautifulSoup(url.text,'html.parser')

pl=[]
for i in bs.find_all("div",class_="rankings-block__banner--name"):
    pl.append(i.text)

pl1=pl[2]
pl1


# In[272]:


pls = []

for i in bs.find_all('td',class_='table-body__cell name'):
    pls.append(i.text.replace("\n",""))
players=pls[18:]
players.insert(0,pl1)
players


# In[274]:


ct = []

for i in bs.find_all('div',class_='rankings-block__banner--nationality'):
    ct.append(i.text.replace("\n",""))
ct1=ct[2]
ct1


# In[275]:


country = []

for i in bs.find_all('span',class_="table-body__logo-text"):
    country.append(i.text)
country1=country[18:]
country1.insert(0,ct1)
country1


# In[276]:


pt=[]

for i in bs.find_all('div',class_='rankings-block__banner--rating'):
    pt.append(i.text)
pt1=pt[2]
pt1


# In[277]:


point=[]

for i in bs.find_all('td',class_="table-body__cell u-text-right rating"):
    point.append(i.text)
point1=point[18:]
point1


# In[278]:


point1.insert(0,pt1)
point1


# In[279]:


Top_Women_AllRounder =pd.DataFrame({'players':players,"teams":country1,"Points":point1})
Top_Women_AllRounder


# # 6) Write a python program to scrape details of all the posts from coreyms.com. Scrape the heading, date, content and the code for the video from the link for the youtube video from the post.

# In[281]:


url=requests.get("https://coreyms.com/")

bs = BeautifulSoup(url.text,'html.parser')

headings=[]

for i in bs.find_all('h2',class_='entry-title'):
    headings.append(i.text)


# In[284]:


len(headings)

date=[]

for i in bs.find_all('time',class_="entry-time"):
    date.append(i.text)
date


# In[285]:


len(date)


# In[286]:


content=[]

for i in bs.find_all("div",class_='entry-content'):
    content.append(i.text.replace("\n",''))
content


# In[287]:


len(content)


# In[288]:


link=[]

for i in bs.find_all("iframe",class_='youtube-player'):
    link.append(i['src'])
link


# In[289]:


link.insert(4,None)


# In[290]:


len(link)


# In[292]:


CoreyMS = pd.DataFrame({ "Heading":headings, "date":date, "Content":content, "Video_link":link})
CoreyMS


# # 7) Write a python program to scrape house details from mentioned URL. It should include house title, location, area, EMI and price from nobroker.in.
# 

# In[293]:


url = requests.get("https://www.nobroker.in/property/sale/gurgaon/Sector%2022?searchParam=W3sibGF0IjoyOC41MDcyNDEsImxvbiI6NzcuMDY0MDQ4NTk5OTk5OTksInBsYWNlSWQiOiJDaElKVDYzQlFub1pEVGtSZEFzSlBmamVkRzQiLCJwbGFjZU5hbWUiOiJTZWN0b3IgMjIifV0=&radius=2.0&city=gurgaon&locality=Sector%2022")
bs = BeautifulSoup(url.text,'html.parser')

houseTitle=[]
for i in bs.find_all("h2",class_="heading-6 font-semi-bold nb__25Cl7"):
    houseTitle.append(i.text)
houseTitle


# In[294]:


location = []

for i in bs.find_all("div",class_="nb__1EwQz"):
    location.append(i.text)
location


# In[295]:


area=[]

for i in bs.find_all("div",class_="nb__FfHqA"):
    area.append(i.text)
area


# In[296]:


emi=[]

for i in bs.find_all("div",class_="font-semi-bold heading-6"):
    emi.append(i.text.replace("â\x82¹",""))
emis=emi[1::3]
emis


# In[297]:


price=emi[2::3]
price


# In[298]:


nobroker_data = pd.DataFrame({ "HouseTitle":houseTitle, "Location":location, "Area":area, "EMI":emis, "Price":price})
nobroker_data


# # 8) Write a python program to scrape mentioned details from dineout.co.in :
# i) Restaurant name
# 
# ii) Cuisine
# 
# iii) Location
# 
# iv) Ratings
# 
# v) Image URL

# In[300]:


url=requests.get('https://www.dineout.co.in/delhi-restaurants/buffet-special')

bs = BeautifulSoup(url.text,"html.parser")

title=[]
for i in bs.find_all("div",class_="restnt-info cursor"):
    title.append(i.text)
title


# In[301]:


loc = []
for i in bs.find_all("div",class_="restnt-loc ellipsis"):
    loc.append(i.text)
loc


# In[302]:


p_c = []
for i in bs.find_all("span",class_="double-line-ellipsis"):
    p_c.append(i.text.split("|"))
price=[]
for i in range(len(p_c)):
    price.append(p_c[i][0])
price


# In[303]:


cuisine = []

for i in range(len(p_c)):
    cuisine.append(p_c[i][1])
cuisine


# In[304]:


rt=[]

for i in bs.find_all("div",class_="restnt-rating rating-4"):
        rt.append(i.text)
rt


# In[306]:


imgUrl=[]

for i in bs.find_all('img',class_='no-img'):
    imgUrl.append(i['data-src'])
    
imgUrl


# In[307]:


dineout=pd.DataFrame({"Restaurant name":title,
                     "Cuisine":cuisine,
                     'Location':loc,
                     'ratings':rt,
                     " Image URL":imgUrl})

dineout


# # 9) Write a python program to scrape weather details for last 24 hours from Tutiempo.net :
# i) Hour
# ii) Temperature
# iii) Wind
# iv) Weather condition
# v) Humidity
# vi) Pressure

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd
url = requests.get('https://en.tutiempo.net/delhi.html?data=last-24-hours')
url


# # 10) Write a python program to scrape monument name, monument description, image URL about top 10 monuments from puredestinations.co.uk

# In[6]:


from bs4 import BeautifulSoup
import requests
import pandas as pd

url = requests.get('https://www.puredestinations.co.uk/top-10-famous-monuments-to-visit-in-india/')
url


# In[7]:


bs = BeautifulSoup(url.text,'html.parser')

m_name=[]
for i in bs.find_all('div',class_='blog--single__content column--3-4 u-spacing-third'):
    m_name.append(i.text.split('\n'))
m_name


# In[8]:


monument_name=m_name[0][3::3]
monument_name[:10]


# In[9]:


monument_desc=m_name[0][4::3]
monument_desc[:10]


# In[11]:


imgUrl = bs.find('div',class_="blog--single__content column--3-4 u-spacing-third")
print(imgUrl)


# In[13]:


imgUrl = bs.find('img',class_="alignnone size-full wp-image-36626 lazyload")
i1=imgUrl['data-src']
i1


# In[15]:


imgUrl = bs.find('img',class_="alignnone size-full wp-image-36628 lazyload")
i2=imgUrl['data-src']
i2


# In[16]:


imgUrl = bs.find('img',class_="alignnone size-full wp-image-36630 lazyload")
i3=imgUrl['data-src']
i3


# In[17]:


imgUrl = bs.find('img',class_="alignnone size-full wp-image-36631 lazyload")
i31=imgUrl['data-src']
i31


# In[18]:


imgUrl = bs.find('img',class_="alignnone size-full wp-image-36632 lazyload")
i4=imgUrl['data-src']
i4


# In[19]:


imgUrl = bs.find('img',class_="alignnone size-full wp-image-36623 lazyload")
i41=imgUrl['data-src']
i41


# In[20]:


imgUrl = bs.find('img',class_="alignnone size-full wp-image-36634 lazyload")
i5=imgUrl['data-src']
i5


# In[21]:


imgUrl = bs.find('img',class_="alignnone size-full wp-image-36636 lazyload")
i6=imgUrl['data-src']
i6


# In[22]:


imgUrl = bs.find('img',class_="alignnone size-full wp-image-36637 lazyload")
i7=imgUrl['data-src']
i7


# In[23]:


imgUrl = bs.find('img',class_="alignnone size-full wp-image-36646 lazyload")
i8=imgUrl['data-src']
i8


# In[24]:


imgUrl = bs.find('img',class_="alignnone size-full wp-image-36630 lazyload")
i8=imgUrl['data-src']
i8


# In[25]:


len(monument_desc)


# In[27]:


Monument_top10 = pd.DataFrame({'Monument name':monument_name[:10],
                            "Content":monument_desc[:10],
                            "Image_url":[i1,i2,i3,i31,i4,i41,i5,i6,i7,i8]})

Monument_top10


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




