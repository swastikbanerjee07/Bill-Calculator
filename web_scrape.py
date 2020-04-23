#import requests
#from lxml import html
#from bs4 import BeautifulSoup

#---------------------------------------------------------------------------
##result = requests.get("https://www.whitehouse.gov/briefings-statements/")
#print(result.status_code)

#print(result.headers)

##src=result.content
#print(src)

##soup = BeautifulSoup(src, 'lxml')

#links=soup.find_all("a")
#print(links)
  
#for link in links:
	#if "About" in link.text:
		#print(link)
		#print(link.attrs['href'])


##urls=[]
##for h2_tag in soup.find_all("h2"):
	##a_tag=h2_tag.find('a') 
	##urls.append(a_tag.attrs['href'])


##print(urls)
#---------------------------------------------------------------------------

from selenium import webdriver

driver = webdriver.Chrome('/home/justanotherlad/Desktop/chromedriver') 


def site_login():
	driver.get("https://www.tnebnet.org/awp/login")
	driver.find_element_by_id("userName").send_keys("")
	driver.find_element_by_id("password").send_keys("")
	driver.find_element_by_name("submit").click()

site_login()
