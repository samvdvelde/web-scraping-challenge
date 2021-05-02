
from bs4 import BeautifulSoup as bs
import requests
import pymongo
from splinter import Browser
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager
from IPython.display import HTML




def scrape():

    def init_browser():
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    browser = init_browser()

    newsurl = 'https://redplanetscience.com/'
    browser.visit(newsurl)



    html = browser.html


    soup = bs(html, 'html.parser')


    slide_elem = soup.select_one('div.list_text')
    news_title = slide_elem.find("div", class_="content_title").get_text()
    news_p = slide_elem.find("div", class_="article_teaser_body").get_text()




    imageurl = 'https://spaceimages-mars.com/'
    browser.visit(imageurl)


    html = browser.html



    soup = bs(html, 'html.parser')




    jpg = soup.find('img', class_='headerimage fade-in')
    imagejpg = jpg['src']
    print(imagejpg)


    # Can't find image url in the html


    featured_image_url = f'https://spaceimages-mars.com/{imagejpg}'



    factsurl = 'https://galaxyfacts-mars.com/'
    facts = pd.read_html(factsurl)


    marslist1 = facts[0]

    marslist1 = marslist1.iloc[1:,:-1]

    marslist2 = facts[1]


    marslists = [marslist1, marslist2]


    marsdata = pd.concat(marslists)




    marsdata.columns = ['property', 'data']
    marsdata.set_index('property', inplace=True)
    marsdata



    marsdata.html = marsdata.to_html()



    hemiurl = 'https://marshemispheres.com/'
    browser.visit(hemiurl)



    html = browser.html



    soup = bs(html, 'html.parser')
    soup





    results = soup.find_all('div', class_='item')

    hemisphere_image_urls = []



    for result in results:
        hemititle = result.find('h3').text.rsplit(' ', 1)[0]
        titlefirst = result.find('h3').text.split()[0]
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
        browser.back()
    


    hemisphere_image_urls = [
        {"title":"Cerberus Hemisphere", "img_url":'https://marshemispheres.com/images/cerberus_enhanced.tif'},
        {"title": "Schiaparelli Hemisphere", "img_url": 'https://marshemispheres.com/images/schiaparelli_enhanced.tif'},
        {"title": "Syrtis Major Hemisphere", "img_url": 'https://marshemispheres.com/images/syrtis_major_enhanced.tif'},
        {"title": "Valles Marineris Hemisphere", "img_url": 'https://marshemispheres.com/images/valles_marineris_enhanced.tif'}
    ]


    browser.quit()




