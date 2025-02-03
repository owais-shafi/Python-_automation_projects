# -----method one did not work because they denied access------

# import requests
# from bs4 import BeautifulSoup as bs

# url = 'https://news.ycombinator.com/'
# response = requests.get(url, headers=headers, verify=False)  # Disable SSL verification

# if requests.status_codes == 200:
#     print("successfully fetched")
# else:
#     print("error in fetching")

# soup = bs(response.text,'html.parser')
 
# headlines = soup.find_all('a', class_='storylink')

# for headline in headlines:
#     print(headline)






# --------==============Method 2 did work================---------

# import requests
# from bs4 import BeautifulSoup as bs

# url = 'https://news.ycombinator.com/'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
# }

# try:
#     response = requests.get(url, headers=headers)
#     response.raise_for_status()
    
#     soup = bs(response.text, 'html.parser')
    
#     # Find all <span> tags with class "titleline"
#     title_spans = soup.find_all('span', class_='titleline')
    
#     for span in title_spans:
#         # The <a> tag inside each span contains the headline text
#         a_tag = span.find('a')
#         if a_tag:
#             print(a_tag.get_text(strip=True))

# except requests.exceptions.RequestException as e:
#     print(f"Error fetching the page: {e}")





# ----------method 3 works well with css selector-------------

import requests
from bs4 import BeautifulSoup as bs

url = 'https://news.ycombinator.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    
    soup = bs(response.text, 'html.parser')
    
    # Select all <a> tags that are inside a <span> with class "titleline"
    headline_links = soup.select('span.titleline a')
    
    for link in headline_links:
        # Print the text of each headline, stripping any extra whitespace
        print(link.get_text(strip=True))

except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")