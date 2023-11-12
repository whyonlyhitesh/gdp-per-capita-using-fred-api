# Timeline of GDP per capita using Fred API
import pandas as pd
import matplotlib.pyplot as plt
import plotly
import plotly.express as px
from fredapi import Fred

# For viewing the graph in certain character. 
plt.style.use("ggplot") 

# For displaying all the columns and rows
pd.options.display.max_rows = 500 
pd.options.display.max_columns = 500 

col_pal = plt.rcParams["axes.prop_cycle"].by_key()["color"] 

# Reading/Importing from Fred_API_KEY.txt
with open('Fred_API_KEY.txt') as f:
    fred_key = f.read()
fred = Fred(api_key=fred_key)

fred_search = fred.search("GDP", filter = ("frequency", "Annual"))
fred_query = fred_search.query('units == "Millions of 2017 U.S. Dollars"')
fred_query = fred_query.loc[fred_query["title"].str.contains("Real GDP at Constant National Prices for")]
fred_query['title'] = fred_query['title'].str.replace(r'Real GDP at Constant National Prices for ', '', regex=True)

fred_search_population = fred.search("Population, Total for", filter = ("frequency", "Annual"))
fred_query_population = fred_search_population.query('units == "Persons" and observation_end == "2022-01-01"')
fred_query_population = fred_search_population.loc[fred_search_population["notes"].str.contains("Total population is based on the de facto")]
fred_query_population['title'] = fred_query_population['title'].str.replace(r'Population, Total for ', '', regex=True)

fred_combo = pd.merge(fred_query, fred_query_population, how='inner', left_on='title', right_on='title')
fred_combo = fred_combo[['id_x', 'id_y', 'title', 'frequency_x', 'units_x', 'units_y']]

fred_combo

all_result = []
for get_id in range(0,21,1) :
  result = fred.get_series(fred_combo.loc[get_id,"id_x"])
  # Naming the columns as index
  result = result.to_frame(name=fred_combo.loc[get_id,"title"])
  all_result.append(result)
gdp_result = pd.concat(all_result, axis=1)
gdp_result = gdp_result.reset_index()

all_result = []
for get_id in range(0,21,1) :
  result = fred.get_series(fred_combo.loc[get_id,"id_y"])
  # Naming the columns as index
  result = result.to_frame(name=fred_combo.loc[get_id,"title"])
  all_result.append(result)
population_result = pd.concat(all_result, axis=1)
population_result = population_result.reset_index()

gdp_result = gdp_result.drop([0,1,2,3,4,5,6,7,8,9])
population_result = population_result.drop([60,61,62])

gdp_result.set_index('index', inplace=True)
population_result.set_index('index', inplace=True)

gdp_per_capita = gdp_result.div(population_result).reset_index()
gdp_per_capita = gdp_per_capita.set_index(["index"])

# Line graph of GDP/Capita vs Year
figure1 = px.line(gdp_per_capita, title="GDP(in million USD) per capita")
plotly.offline.plot(figure1, filename='gdp_per_capita_line.html')

# Bar chart GDP/Capita of 2019
data = gdp_per_capita.loc[gdp_per_capita.index == '2019-01-01'].T \
    .sort_values('2019-01-01') \
    .plot(kind='bar', figsize=(16, 12), width=1, edgecolor='Orange',
          title='GDP(in million USD) per Capita, Jan 2019')
data.legend().remove()
data.set_xlabel('% GDP(in million USD)/Capita')
plt.show()