from bs4 import BeautifulSoup, Comment
import requests, re

URL = "https://www.google.com/shopping/product/11559963950601094589?q=dell+u2720q+australia&sxsrf=ALeKk03YfU8bDzL9JoalgdHWaqyStTBuDQ:1610873634120&biw=1920&bih=969&prds=epd:1039039642099595239,prmr:1&sa=X&ved=0ahUKEwjmzfL2y6LuAhXm4nMBHSIWDzIQ3q4ECMAF#online"
def make_soup(url):
    r = requests.get(url)
    soupdata = BeautifulSoup(r.text, 'lxml')
    return soupdata

soup = make_soup("https://www.google.com/shopping/product/11559963950601094589?q=dell+u2720q+australia&sxsrf=ALeKk03YfU8bDzL9JoalgdHWaqyStTBuDQ:1610873634120&biw=1920&bih=969&prds=epd:1039039642099595239,prmr:1&sa=X&ved=0ahUKEwjmzfL2y6LuAhXm4nMBHSIWDzIQ3q4ECMAF#online")

# get the comments
comments = soup.findAll(text=lambda text:isinstance(text, Comment))

# look for table with the id "team_stats"
# rx = re.compile(r'<table.+?id="sh-osd__online-sellers-grid".+?>[\s\S]+?</table>')
rx = re.compile(r'<table class="dOwBOc" id="sh-osd__online-sellers-grid".+?>[\s\S]+?</table>')

for comment in comments:
    try:
        table = rx.search(comment.string).group(0)
        print(table)
        # break the loop if found
        break
    except:
        pass