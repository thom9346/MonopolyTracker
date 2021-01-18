import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import re
import time

from win10toast import ToastNotifier

last_roll_checkmark = 1
has_shown_notification = False

def get_spins_since_4rolls(): 
    url = 'https://tracksino.com/monopoly'

    #opens connection, and basically downloads the whole page.
    uClient = uReq(url)
    page_html = uClient.read()
    uClient.close()

    page_soup = soup(page_html, "html.parser")

    whole_segment_4 = page_soup.find("div", {"class": "monopoly-seg-r4"})
    segemnt_4 = whole_segment_4.div.center.div.div

    div_cointaing_spins = soup.select_one(segemnt_4, "div:nth-of-type(2)").text

    spins_since_last_4roll = int(re.sub("[^0-9]", "", div_cointaing_spins))

    global last_roll_checkmark
    global has_shown_notification
    if(spins_since_last_4roll < last_roll_checkmark):
        print("writing to file...")
        f = open("spinstogetrolls.txt", "a")
        f.write("\n 4 rolls after: " + str(last_roll_checkmark))
        f.close()
        if(has_shown_notification == True):
            toast.show_toast("4 rolls hit!", "4 rolls landed after " + str(last_roll_checkmark) + " spins.",duration=45,icon_path="monopolygame_monopolio_6962.ico")
            has_shown_notification = False

        last_roll_checkmark = -1


    last_roll_checkmark = spins_since_last_4roll

    if(spins_since_last_4roll > 205):
        print("Its over 205 rolls")
        print(spins_since_last_4roll)   

        if(has_shown_notification == False):
            toast.show_toast("Monopoly Time!","It has been " + str(spins_since_last_4roll) + " spins since last rolls.",duration=45,icon_path="monopolygame_monopolio_6962.ico")
            has_shown_notification = True

    else:         
     print("nothing happened.")
     print("lol" + str(last_roll_checkmark))


starttime = time.time()
toast = ToastNotifier()
while True:
    get_spins_since_4rolls()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))