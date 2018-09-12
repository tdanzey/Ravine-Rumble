# Import packages
import pandas
import requests
import lxml

# Get page content
url = "https://archive.fantasysports.yahoo.com/nfl/2017/189499?lhst=sched#lhstsched"
html = requests.get(url).content
df_list = pandas.read_html(html)

# Pull relevant URLs
