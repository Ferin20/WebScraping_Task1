from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#To configure webdriver to use Chrome browser, we set the path to chromedriver
driver = webdriver.Chrome("C:\\Users\\rincy\\Downloads\\chromedriver_win32\\chromedriver")

#to open the url to linkedin
#driver.get("https://www.linkedin.com/jobs/jobs-in-kurla?trk=homepage-basic_intent-module-jobs&position=1&pageNum=0")
driver.get("https://in.linkedin.com/jobs/view/project-architect-at-a3-cube-architects-2719454202?refId=omAlyaoXlIMtuqQe3B4Jmw%3D%3D&trackingId=Qn3lBcynDrGJOJxDhCxeDw%3D%3D&position=1&pageNum=0&trk=public_jobs_jserp-result_search-card")

#to load the page content 
content = driver.page_source

#to extract data from the html or xml file
soup = BeautifulSoup(content, features="html.parser")

#lists to store the company description, location and job description for the selected company as well as any other desired company
description=[]
location=[]
jobDes=[]

#find the container that contains the required details
b=soup.find('div',attrs={'class':'top-card-layout__entity-info-container'})

#extract the company description within the container
des=b.find('span',attrs={'class':'topcard__flavor'})

#extract the company location within the container
loc=b.find('span',attrs={'class':'topcard__flavor topcard__flavor--bullet'})

#extract the job description from the page
c=soup.find('div',attrs={'class':'show-more-less-html__markup show-more-less-html__markup--clamp-after-5'})

#append the details acquired to the lists created before
#strip them to remove unnecessary spaces or tabs
description.append(des.text.strip())
location.append(loc.text.strip())
jobDes.append(c.text.strip())

#print the extractted contents
print("Description: ",description)
print("Location: ",location)
print("Job Description: ",jobDes)




