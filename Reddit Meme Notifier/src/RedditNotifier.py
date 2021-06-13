from bs4 import BeautifulSoup
import requests
import schedule
import time
import PickupLines as pl
import random
#Importing libraries based on Mac/Windows
try:
    import pync
except:
    from win10toast_click import ToastNotifier
    import webbrowser

def job():
    pickup_line = random.choice(pl.sentences)
    #Starting Up + Pickup Line!
    try:
        pync.notify('\n' + pickup_line, title='MEME OF THE HOUR?! STARTING UP!', contentImage='https://i.kym-cdn.com/entries/icons/original/000/013/564/doge.jpg')
        time.sleep(5)
    except:
        toaster = ToastNotifier()
        toaster.show_toast(
            "MEME OF THE HOUR?! STARTING UP!", # title
            '\n' + pickup_line, # messages
            duration=4, # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears
            icon_path="doge.ico"
            )
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
            url = "http://reddit.com" + url

    try:
        #Notification for Mac
        try:
            pync.notify(title, title='MEME OF THE HOUR?!?!', contentImage=img, open=url)
        except:
            pync.notify(title, title='MEME OF THE HOUR?!?!', open=url)

    except:
        def open_url():
            webbrowser.open_new(url)
        #Notification for Windows
        toaster = ToastNotifier()
        toaster.show_toast(
            title, # title
            "Click to open MEME! >>", # message
            duration=5, # for how many seconds toast should be visible; None = leave notification in Notification Center
            threaded=True, # True = run other code in parallel; False = code execution will wait till notification disappears
            callback_on_click=open_url,
            icon_path="doge.ico"
        )

#Starts the process
job()

schedule.every(1).hours.do(job)
while True:
    schedule.run_pending()
    time.sleep(1)