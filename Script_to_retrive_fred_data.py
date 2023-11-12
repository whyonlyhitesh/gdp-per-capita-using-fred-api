import pandas as pd
import matplotlib.pyplot as plt
from fredapi import Fred

# For viewing the graph in certain character. 
plt.style.use("ggplot") 

# For displaying all the columns and rows
pd.options.display.max_rows = 500 
pd.options.display.max_columns = 500 

# Reading/Importing from Fred_API_KEY.txt
with open('Fred_API_KEY.txt') as f:
    fred_key = f.read()

fred = Fred(api_key=fred_key)

# Input from user, what to search
search_input = input("What do you want to search in Fred: ")
# Adding Filters
num_filter = input("Do you want to add filters to your search (If yes then type True, if not then type anything else): ")

if num_filter == "True" :
    num_filter = tuple(input("Write the filters you want to apply, minimun number of filters = 2. In the format of space-separated words: ").split())
    sp_search = fred.search(search_input, order_by="title", filter=num_filter)
else :
    print("You haven't selected any filters")
    sp_search = fred.search(search_input, order_by="title")

# Printing output of search

print(sp_search)

if str(sp_search) == "None" :
    print("Your search did not produce any results. Could you please provide more details or try different keywords?")
    exit
else :
    title_from_user = input("Input the Series ID/ID of data that you want to work on: ")
    data_from_user = fred.get_series(series_id=title_from_user)
    data_from_user.plot(figsize=(16, 9), title=title_from_user, lw=2)
    plt.show() 
