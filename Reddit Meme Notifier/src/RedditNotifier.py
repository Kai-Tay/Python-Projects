from bs4 import BeautifulSoup
import requests
import pync
import schedule
import time
import PickupLines as pl
import random


def job():
    pickup_line = random.choice(pl.sentences)
    #Starting Up + Pickup Line!
    pync.notify('\n' + pickup_line, title='MEME OF THE HOUR?! STARTING UP!', contentImage='https://i.kym-cdn.com/entries/icons/original/000/013/564/doge.jpg')
    time.sleep(5)
    #Retrieving from r/meme page
    link = "https://www.reddit.com/r/memes/top/?t=hour"
    headers = {'User-Agent': 'Mozilla/5.0'}
    r = requests.get(link, headers=headers)
    html_news = r.text
    news = BeautifulSoup(html_news, 'html.parser')
    attributes = {'class': "_1oQyIsiPHYt6nx7VOmd1sz"}
    print(r)

    for details in news.find("div", attrs=attributes):
        #title
        for title_tag in details.find_all("h3", class_= "_eYtD2XCVieq6emjKBH3m"):
            title = str(title_tag)
            title = title.replace('<h3 class="_eYtD2XCVieq6emjKBH3m">', "").replace('</h3>', "");
        try:
            #image
            for image_tag in details.find_all("img", attrs = {'alt' : "Post image"}):
                img = image_tag["src"]
        except:
            continue
        #URL Link
        for url_tag in details.find_all("a", attrs = {'data-click-id' : "body"}):
            url = url_tag["href"]

    #Notification for Mac
    try:
        pync.notify(title, title='MEME OF THE HOUR?!?!', contentImage=img, open="http://reddit.com" + url)
    except:
        pync.notify(title, title='MEME OF THE HOUR?!?!', open="http://reddit.com" + url)

    #Notification for Windows


#Starts the process
job()
schedule.every(1).hours.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)