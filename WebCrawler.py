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
for i in range (0, len(names_list)-1):
    if type(names_list[i]) == str:
        first_name = names_list[i].split()[0]
        last_name = names_list[i].split()[1]
    else:
        continue
    driver = webdriver.Chrome("C:/Users/DanSo/Downloads/chromedriver_win32/chromedriver.exe")
    driver.get('https://search.appstate.edu/search.php?last=' + last_name + '&first=' + first_name + '&type=all')
    
    #Finding emails using @ sign
    doc = driver.page_source
    emails = re.findall(r'[\w\.-]+@[\w\.-]+', doc)

    #
    if len(emails) == 0:
        continue
    else:
        #Gets emails and puts them into a list
        df = pandas.DataFrame()
        email_list.append(emails)
        df['emails'] = email_list[0::1]
        df.to_excel('Emails2.xlsx', index = False)

    #Closes the browser after adding the email
    driver.close()


