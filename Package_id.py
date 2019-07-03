#import pandas 
import pandas as pd


# import Application names to be seached
d=pd.read_csv('users_installed_apps (2).csv')
s=list(d.iloc[:,0])


# Importing required libraries 
# Need to install libraries play_scraper
# Download Web-Driver for your pc
# Install Selenium

 
import re
import play_scraper as ps
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import time


# dict for storing application name and package name.
Applications={}

# add the path of web driver
browser = webdriver.Chrome('/home/deepak/.wdm/chromedriver/75.0.3770.90/linux64/chromedriver')



# list to store application not found on play store 
er=[]


for i in s:
    try:
        
        # open play store in your browser
        browser.get("https://play.google.com/store/apps")
        
        # Enter text to the search box on play store page
        inputElement = browser.find_element_by_id("gbqfq")
        inputElement.send_keys(str(i))
        inputElement.submit() 
        
        
        # Wait to load the page completely
        #Depends on Internet Speed (change delay accordingly).
        time.sleep(6)
        
        # click search button 
        browser.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[2]/div/div[2]/div/c-wiz/c-wiz[1]/c-wiz/div/div[2]/div[1]/c-wiz/div/div/div[1]/div/div/a').click()
        # Wait for page load
        time.sleep(6)
        
        # Find Application Name (to be matched with the name provided)
        # It helps to check whether application is there on play store
        txt=browser.find_element_by_xpath('//*[@id="fcxH9b"]/div[4]/c-wiz[3]/div/div[2]/div/div[1]/div/c-wiz[1]/c-wiz[1]/div/div[2]/div/div[1]/c-wiz[1]/h1/span').text
        
        # Find current URL for the page
        url=browser.current_url
        
        
        # Find package name from the url
        k = re.search('id=',str(url))
        a1 = k.span()[1]
        st = url[46:]
        temp = re.search('hl=',str(st))
        if temp! = None:
            st = st[:-6]
        ck = re.search(i,txt,re.IGNORECASE)
        if ck! = None:
            print(st)
            print(txt)
            Applications[txt] = st
    except:        
        er.append(i)




