from bs4 import BeautifulSoup
from urllib2 import urlopen

def make_soup(url):
    html = urlopen(url).read()
    # print html
    soup = BeautifulSoup(html, "lxml")
    span = [span.string for span in soup.findAll("span", "title")]
    for item in span:
        print item

soup = make_soup("http://dining.richmond.edu/locations/heilman/index.html") # where url is the url we're passing into the original function
