from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#To configure webdriver to use Chrome browser, we set the path to chromedriver
driver = webdriver.Chrome("C:\\Users\\rincy\\Downloads\\chromedriver_win32\\chromedriver")

#to open the url to careerguide
driver.get("https://www.careerguide.com/career-options")

#to load the page content 
content = driver.page_source

#to extract data from the html or xml file
soup = BeautifulSoup(content, features="html.parser")

#to find the link for category: Design & Art within all the job types
for a in soup.findAll('div', attrs={'class':'col-md-4'}):
 b=a.find('a',href=True,attrs={'title':'Designing & Art'})
 if b!=None:
     break

#variable that holds the desired title found by the for loop
cat = b.text

#list to store all the sub-categories within the desired category found
subcat=[]

#to enlist all the sub-categories within the desired category found
l = a.find('ul',attrs={'class':'c-content-list-1 c-theme c-separator-dot'})
    
#to find the links to sub-categories 
for n in l:
    if n!= None:
        s=n.find('a',href=True)
        subcat.append(s.text)
    
print("\nCategory: ",cat)
print("\nSub-category: ",subcat)

#to create a dataframe with heading as the title of the category and list of sub-categories
df=pd.DataFrame({cat:subcat})
#convert the dataframe to csv file
df.to_csv('jobTypes.csv', index=False, encoding='utf-8')

