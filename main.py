import requests
from bs4 import BeautifulSoup as bs

github_user = input('Input Github User:') #to take user name
url  = 'https://github.com/'+github_user #url + concatinating user name
r = requests.get(url) #url request
soup = bs(r.content, 'html.parser')# .content gives content of page
profile_image = soup.find('img',{'alt':'Avatar'})['src']
print(profile_image)