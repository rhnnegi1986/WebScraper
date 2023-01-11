# -*- coding: utf-8 -*-
"""
Created on Fri Nov 19 15:59:57 2021

@author: rhnne
"""

import pandas as pd
import numpy as np
import string
import selenium
import io
from selenium import  webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from  actions import  Actions
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webelement import WebElement
from random import randint
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import ElementNotInteractableException
from selenium.common.exceptions import WebDriverException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.common.exceptions import NoSuchFrameException
from selenium.webdriver.common import keys
import time
from requests import get
import re
import sys
from itertools import chain
from itertools import zip_longest
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import urllib
import ssl
import urllib.request as urlrq
import certifi
import nltk
import requests 
import csv
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pytesseract 
from PIL import Image
import os
from urllib.parse import urlparse
import json
import os.path
import stat
import subprocess
import sys
from urllib import request
from io import StringIO
#%%


ssl._create_default_https_context = ssl._create_unverified_context
time_start = time.time()
s= Service(ChromeDriverManager().install())
chrome_options = Options()
chrome_options.binary_location = "C:\Program Files\Google\Chrome\Application\chrome.exe"
driver = webdriver.Chrome(executable_path=("C:\webdriver\chromedriver_win32 (2)\chromedriver.exe"),service=s)
driver.get("https://www.puppyfind.com/for_sale_state/?state=MI&page=1&state=MI&order_by=new&sid=d87f8m42u6p4ofiifaj3jfpl86&back=")


path = os.getcwd()
opener = urllib.request.build_opener()
Breed_Name = []
Sex = []
Price = []
Business_Name = []
City = []
State = []
Phone_Number = []
Website = []
start = 1
stop = 2700
step = 1
count = 0
pages = np.arange(start,stop,step)
all_links = []
more_data_button = []
condition = True
All_Data = []

# Petfinder_Data = ("Breed_Name" + "\t" + "Sex" + "\t" + "Price" + "\t" + "Business_Name" + "Owner_Name" + "\t" + "City" + "\t" + "State" + "\t" + "Phone_Number" + "\n")
# PetFinder_Outfile = open("D:\\Puppy_Finder.txt","w")
# PetFinder_Outfile.write(Petfinder_Data + "\n")
# PetFinder_Outfile.close()





while condition:
    next_page_btn = driver.find_elements(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/form/table[4]/tbody/tr/td/a')
    if len(next_page_btn) < 0:
        break
    else:
        Titles = len(WebDriverWait(driver,2).until(EC.presence_of_all_elements_located((By.LINK_TEXT,"More info"))))
        for ilink in range(Titles):
            link = driver.find_elements(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/form/table[3]/tbody/tr/td[3]/table/tbody/tr[1]/td[1]/a/b')[ilink]
            link.click()
            time.sleep(2)
            with open("D:\\Puppy_Finder.txt","a") as file:
                try:
                    Brd = driver.find_element(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/table[3]/tbody/tr[3]/td[2]').text
                    Breed_Name.append(Brd)                    
                    sx = driver.find_element(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/table[3]/tbody/tr[4]/td[2]').text 
                    Sex.append(sx)
                    pr = driver.find_element(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/table[3]/tbody/tr[9]/td[2]').text
                    Price.append(pr)
                    Business = driver.find_element(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/table[3]/tbody/tr[16]/td/b').text
                    Business_Name.append(Business)
                    Cty = driver.find_element(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/table[3]/tbody/tr[18]/td/a[1]').text
                    City.append(Cty)
                    Sta = driver.find_element(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/table[3]/tbody/tr[18]/td/a[2]').text
                    State.append(Sta)            
                    src = driver.find_element(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/table[3]/tbody/tr[19]/td/img').get_attribute('src')                    
                    urllib.request.urlretrieve(src,r"D:\Machine_Learning\Image\Phone.png")                    
                    pytesseract.pytesseract.tesseract_cmd = r"C:\Users\rhnne\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"
                    img = Image.open(r"D:\Machine_Learning\Image\Phone.png")
                    text = pytesseract.image_to_string(img, lang='eng')
                    Phone_Number.append(text)                
                    
                        
                except(NoSuchElementException,StaleElementReferenceException,IndexError,TypeError):
                    pass
                driver.back()
                time.sleep(1)                
                driver.find_element(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/form/table[3]/tbody') 
    
        element = driver.find_element(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/form/table[4]/tbody/tr/td/a[11]')
        ##driver.find_element(By.XPATH,'//*[@id="container"]/div[3]/div/div[2]/form/table[4]') 
        time.sleep(1)
        element.click()
        time.sleep(2)
        continue
    break
Petfinder_Data = ("Breed_Name" + "\t" + "Sex" + "\t" + "Price" + "\t" + "Business_Name" +  "\t" + "City" + "\t" + "State" + "\t" + "Phone_Number" + "\n")
PetFinder_Outfile = open("D:\\Puppy_Finder_Data.txt","w")
PetFinder_Outfile.write(Petfinder_Data + "\n")
PetFinder_Outfile.close()
with open("D:\\Puppy_Finder_Data.txt","a") as file:
    for A,B,C,D,E,F,G in zip_longest(Breed_Name,Sex,Price,Business_Name,City,State,Phone_Number):
        file.write(str(A) + "\t" + str(B) + "\t" + str(C) + "\t" + str(D) + "\t" + str(E) + "\t" + str(F) + "\t" + str(G) + "\n")
                        
                                       
                                 
                    
                    # driver.get(element_to_hover)                  
                    # time.sleep(2)                    
                    # stars_count = driver.find_element(By.XPATH,'/html/body/img')
                    # stars_count.click()
                    # el = driver.find_element(By.TAG_NAME,'img')
                    # hover_action = ActionChains(driver).move_to_element(el)
                    # hover_action.perform()
                    # hover_action.
                
                 
                  
                    
                   
                    
                    
                    # ele = driver.find_element(By.CSS_SELECTOR,"#container > div.full.content > div > div.main > table:nth-child(9) > tbody > tr:nth-child(19) > td > img")
                    # time.sleep(2)
                    # ele.click()
                  
                   
                    
                    
                    # # file.write(Tel)
                    # # f = open(r'D:\\Machine_Learning\image\image.txt', 'r',encoding="utf-8")
                    
                    # Tel_text = pytesseract.image_to_data(ele,lang=None,config='')
                    # Phone_Number.append(Tel_text)

                    ##f = open('', 'r')
                   ## print(f)
                    
                
                
       

    
    
    ##next_page = 
   
          
            
    
    
   
    
   
        
   
    
        
    
        
    
    
    
        
        
                
           
            
        
    
            
    
            
               
             
        
        
    
    
    

    
                  
       
         
      
      
    
        
        
        
        
   
   
       
        
    
        
        
    
           
        
           
        
        
        
        
    
    
        
        
            
        
        
            
                
        
   
    
 
        
       
      
            
        
        
            
                # 
            
                
        
    
        
   
        
        
        
            
            
            
    
    

     

    
         
             
            
    
     
   

    
    
    
    
 
                      
                        
                    
                   
        
        
        
                       
    
      
                
      

    
        
              
           
        
        
                       
            
            
      
        
        
    
    

    
            
    


    
    



    
    
   
    
                
    

    
          
            
                
            
         
        
            
        
    
    
     
         
     
              
         
    
            
                
         
            
                    
                    
                
               
            
    
          
                
                
                
            
        
                
                
                  
               
                
                
                
            
        
        
        
    
        
        
    
            
    
        
    
        
   
    
            
            
        
        
       
        
   
    

        
        
   
        
                
    

          
            
    

        
    
        
    
        
            
            
            
            
       
                                       
        
        
    
   
    
    
    
   
                        
            
   
    
       
        
       
                
        
    
            
            
        
        
            
        

            
            
        
            
        
            
     
     
    
 

    
    
    


     
    
    
    
        
            
        
        
       
        
        
                   
            
         
   

                
                











            
                     
                     


       
   
       
         
      
      
   
       
   
   
   
       
                
      
   
   
                   
             
       
       
       
     
       

      
       
           
       
       
       
       
       
        
              
       

        
        
            
            
        
       
            
        
            
        
 
        
#%%        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
       
    
                 
                       
        
        
    
        
                           
            
   
           
               
                           
        
           
            
    

    # 
    
            
       
        
   
    
   
        
        
        
        
        
        
       
    
        
        
          




    
         
        
        
            
            
        
                
       
            
       
                    
        
                    
                    
                
    
        
        
        
            
            
    
    
     
    
        
    
       
            
        
        
    
    
    
            
            
               
            
          
                
          
        
            
        
        
            
                 
                    
                 
          
        
            
        
               
            
                
            
        
        
       
                
              
            
                
        
                 

                
                              
            
        
        
        

    






































        
           
        
        
            
   
    
   
    
    


  
    
       
        
                
         
        
   
       
              
        
   
    
        
        
    
        
       
        
        
        
 
                
               
                
        
        
    
        
    
    
        
                

       
    
    
    
            
    
            
         
            
       
    
    
        

       
        
        
    
                
            
            
    
        
        
       
            
            
            
        
            
        
    
  
     
    
         
     
     
         
         
          
            
                                  
                
              
                  
                
       
               
                





































        
             
        
     
     


                    
                
        
        
            
       
      