from urllib.request import urlopen
import re

url = "http://olympus.realpython.org/profiles/aphrodite"

page = urlopen(url)
# page

html_bytes = page.read()
html = html_bytes.decode("utf-8")
# print(html)

title_index = html.find("<title>")
# title_index

start_index = title_index + len("<title>")
end_index = html.find("</title>")
title = html[start_index:end_index]