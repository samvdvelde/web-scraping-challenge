
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from IPython.display import HTML


def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


def scrape():
    browser = init_browser()

newsurl = 'https://redplanetscience.com/'
browser.visit(newsurl)



html = browser.html


soup = bs(html, 'html.parser')


slide_elem = soup.select_one('div.list_text')
news_title = slide_elem.find("div", class_="content_title").get_text()
news_p = slide_elem.find("div", class_="article_teaser_body").get_text()


print(news_title)
print(news_p)


imageurl = 'https://spaceimages-mars.com/'
browser.visit(imageurl)


html = browser.html



soup = bs(html, 'html.parser')




jpg = soup.find('img', class_='headerimage fade-in')
imagejpg = jpg['src']
print(imagejpg)


# Can't find image url in the html

# In[13]:


featured_image_url = f'https://spaceimages-mars.com/{imagejpg}'


# In[14]:


factsurl = 'https://galaxyfacts-mars.com/'
facts = pd.read_html(factsurl)
facts


# In[15]:


marslist1 = facts[0]

marslist1 = marslist1.iloc[1:,:-1]

marslist1


# In[16]:


marslist2 = facts[1]
marslist2


# In[17]:


marslists = [marslist1, marslist2]


# In[18]:


marsdata = pd.concat(marslists)


# In[19]:


marsdata


# In[20]:


marsdata.columns = ['property', 'data']
marsdata.set_index('property', inplace=True)
marsdata


# In[21]:


marsdata.html = marsdata.to_html()


# In[22]:


hemiurl = 'https://marshemispheres.com/'
browser.visit(hemiurl)


# In[23]:


html = browser.html


# In[24]:


soup = bs(html, 'html.parser')
soup


# In[25]:


# for x in range(4):

#     browser.links.find_by_partial_text('Hemisphere Enhanced').click()
    
#     html = browser.html
    
#     soup = BeautifulSoup(html, 'html.parser')
    
#     hemi = soup.find('div', class_='cover')
#     hemititle1 = result.find('h2').text.split()[0]
#     hemititle2 = result.find('h2').text.split()[1]
#     hemititle = f'{hemititle1} {hemititle2}'
          
# results = soup.find_all('div', class_='description')
# for result in results:
#     hemititle1 = result.find('h3').text.split()[0]
#     hemititle2 = result.find('h3').text.split()[1]
#     hemititle = f'{hemititle1} {hemititle2}'
    


# In[26]:


results = soup.find_all('div', class_='item')

hemisphere_image_urls = []



for result in results:
    hemititle = result.find('h3').text.rsplit(' ', 1)[0]
    titlefirst = result.find('h3').text.split()[0]
    print(hemititle)
    browser.links.find_by_partial_text(titlefirst).click()
    html = browser.html
    soup = bs(html, 'html.parser')
    con = soup.find('div', class_='container')
    cov = con.find('div', class_='cover')
    desc = cov.find('div', class_='description')
    dl = desc.find('dl')
    dd = dl.find('dd')
    link = dd.find('a')
    href = link['href']
    print(href)
    browser.back()
    
# for result in results:
#     desc = result.find('div', class_='description')
#     a = desc.find('a')
#     browser.links.find_by_partial_text(hemititle).click()
#     soup = bs(html, 'html.parser')
#     div = soup.find('div', class_='description')
#     dl = div.find('dl')
#     #dd = dl.find('dd')
#     link = dd.find('a')
#     href = link['href']
#     hemisphere_image_urls.append(href)
#     hemi = {'title': hemititle, 'img_url': href}
#     hemisphere_image_urls.append(hemi)
    
#     browser.back()
    
imglinks = ['https://marshemispheres.com/images/cerberus_enhanced.tif','https://marshemispheres.com/images/schiaparelli_enhanced.tif','https://marshemispheres.com/images/syrtis_major_enhanced.tif','https://marshemispheres.com/images/valles_marineris_enhanced.tif']  
        

    



hemisphere_image_urls = [
    {"title":"Cerberus Hemisphere", "img_url":'https://marshemispheres.com/images/cerberus_enhanced.tif'},
    {"title": "Schiaparelli Hemisphere", "img_url": 'https://marshemispheres.com/images/schiaparelli_enhanced.tif'},
    {"title": "Syrtis Major Hemisphere", "img_url": 'https://marshemispheres.com/images/syrtis_major_enhanced.tif'},
    {"title": "Valles Marineris Hemisphere", "img_url": 'https://marshemispheres.com/images/valles_marineris_enhanced.tif'}
]


browser.quit()




