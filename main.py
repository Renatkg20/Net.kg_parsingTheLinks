import requests 
from bs4 import BeautifulSoup
import urllib3
import time
# This project created for studying purpose for developing parsing skills.

# Intrated the numbers of web pages. First review 77 pages. 
#Then save all links into the file links2.txt 
#After the saving identified links, the another step was get links of registrated web sites. 
for q in range(1, 78):
    url = f"https://www.net.kg/?pp=20&main_cat=&cat=&old_sort=&orient=&sort=&scroll={q}"
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    http = urllib3.PoolManager(timeout=10.0)
    res = (http.request('GET', url)).data
    soup = BeautifulSoup(res, "html.parser")
    soup = soup.find("div", {"id":"main_block"}).find_all("a", {"class":"nav"})
    with open("links2.txt", "a") as f:
         f.write(str(soup))
 

# Read the file links2.txt select titles saving it final links without tags.
with open("links2.txt", "r") as f2:
     t = f2.read()

soup = BeautifulSoup(t, "html.parser")
soup = soup.find_all("a")
for a in soup:
    print(a.get("title"))
    with open("final_links.txt", "a") as f3:
         links = a.get("title")
         f3.write(f"{links} \n")
         
#This part code made to avoid errors due to blocking the web server. 
try:
    def get_num_pages():
        try:
            for i in range(90):
                url = f"https://www.net.kg/?pp=20&main_cat=&cat=&old_sort=&orient=&sort=&scroll={i}"
                user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
                res = (requests.get(url, headers = user_agent, timeout = 15 ))
                if str(res) == "<Response [200]>":
                    with open("links.txt", "a") as file:
                        file.write(f"{url}\n")
                else:
                    break
        except requests.exceptions.ConnectionError:
               print("\n Переподключение к серверам Net.kg \n")
               time.sleep(30)
      
 

except requests.exceptions.ConnectionError:
       print("\n Переподключение к серверам Net.kg \n")
       time.sleep(30)
       print(get_num_pages())


#print(get_num_pages())

"""
with open("links.txt", "r") as file1:
     data_links = file1.read()
"""

# Function created for parsing each page of net.kg
def open_links(data_links):
    res1 = data_links.split("\n")
    links = []
    for i in res1:
        if i not in links and str(i) != "":
           links.append(i)
    
    user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
    try:
       for a in links: 
           url = i
           res = (requests.get(url, headers = user_agent, timeout = 6 )).content
           print (res)
    except requests.exceptions.MissingSchema:
        pass
        res1 = (requests.get(a, headers = user_agent, timeout = 10)).content
        soup = BeautifulSoup(res1, "html.parser")
        soup = soup.find("div", {"class":"navigation"}).find_all('a')
        for a in soup:
            print(a)

#print(open_links(data_links))

"""
$trigger = New-JobTrigger -AtStartup -RandomDelay 00:00:30

"""

