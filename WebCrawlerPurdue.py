from bs4 import BeautifulSoup
import pandas
import os
import selenium
from selenium import webdriver
import re

##Creates list of athlete names
athlete_email_list = pandas.read_excel('Athlete Email Sheet (Soto).xlsx', sheet_name = 'Appalachian State')
names_list = athlete_email_list['Student Athlete FULL Name'].tolist()
email_list = []

##Creates email list by iterating through name list and inputting into website
for i in range (0, 1):
    driver = webdriver.Chrome("C:/Users/DanSo/Downloads/chromedriver_win32/chromedriver.exe")
    driver.get('https://www.purdue.edu/directory/')

    #Selects and enters into input box
    first_name_input = driver.find_element_by_id('basicSearchInput')
    first_name_input.send_keys(names_list[i])
    enter_button = driver.find_element_by_id('glass')
    enter_button.click()

    #Finding emails using @ sign
    doc = driver.page_source
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

    if len(emails) == 0:
        continue
    else:
        #Gets emails and puts them into a list
        email_list.append(emails)

    #Closes the browser after adding the email
    driver.close()

df = pandas.DataFrame()
df['emails'] = email_list[0::1]
df.to_excel('Emails.xlsx', index = False)

    
