import requests
from bs4 import BeautifulSoup
import csv

######## SCRAPING QUOTES FROM THE HOMEPAGE #################3
# res = requests.get("http://quotes.toscrape.com/")
# soup = BeautifulSoup(res.text,"html.parser")

# ## Finding the Page Length
# length = len(soup.select(".text"))
# ## Scraping All the Quotes with author name
# for i in range(0,length):
#     quote = soup.select(".text")[i].get_text().strip()
#     author = soup.select('.author')[i].get_text().strip()
#     print(quote)
#     print(author)


########  SCRAPING QUOTES FROM ALL THE PAGES

page = 10 ## Number of Pages you want to scrape
for i in range(0,page):
    res = requests.get(f"http://quotes.toscrape.com/page/{i}/")
    soup = BeautifulSoup(res.text,"html.parser")

    ### Finding the Page Length
    length = len(soup.select(".text"))
    ### Scraping All the Quotes with author name
    for j in range(0,length):
        quote = soup.select(".text")[j].get_text().strip()
        quote = quote.replace("\u2032"," ")
        author = soup.select('.author')[j].get_text().strip()
        with open('quote.csv','a',newline='') as f:
            writer = csv.writer(f)
            writer.writerow([quote,author])
print("Done!")