from selenium import webdriver
import time
import pandas as pd

tweet_count = 0

from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--headless")
browser = webdriver.Chrome(options=chrome_options)
veri = "covid19"
browser.get("https://twitter.com/search?q="+veri+"%20lang%3Aen&src=typed_query&f=live")
time.sleep(2)

tweets = []
tweet = browser.find_elements("xpath", "//div[@data-testid='tweetText']")
time.sleep(2)
for i in tweet:
    tweets.append(i.text)
    tweet_count += 1

sayac = 0
last = browser.execute_script("return document.documentElement.scrollHeight") #We are taking the mouse scrolling height
while True: #loop
    if sayac > 10 : #if the counter is more than 10, the program is terminated.
        break
    browser.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)") #We're scrolling so we can access the tweets below.
    new = browser.execute_script("return document.documentElement.scrollHeight") #we get the new length we need to scroll with the mouse
    if last == new : #If our translation is the same as the old translation, if nothing has changed, the program closes because there are no tweets left.
        break
    last = new
    sayac += 1
    tweet = browser.find_elements("xpath", "//div[@data-testid='tweetText']") #scraping tweets from the page which in front of us
    time.sleep(2) #2 seconds waiting
    for i in tweet: #for each tweet that we scraped
        tweets.append(i.text) #adding that tweet to list
        tweet_count += 1 #adding 1 to tweet_count

tweets_dataframe = pd.DataFrame(tweets, columns=['tweet'])
