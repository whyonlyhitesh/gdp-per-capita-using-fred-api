# Timeline of GDP per capita using Fred API 

## Disclaimer
Please note that all the data used in this project belongs to the respective authors who have gathered and published it on Fred. I do not claim ownership of this data. My role was merely to utilize this publicly available data for the purpose of this project. All credit for the data collection and publication goes to the original authors. 

## Birth of this project ;)
A few days ago, I found myself contemplating the per capita GDP of various countries. My curiosity led me to the IMF website, but I was disappointed to find that their data only spanned from 1980 onwards. Determined to delve deeper, I turned to FRED to gather data and subsequently created a timeline of GDP per capita for 22 countries, ranging from 1960 to 2019. 
The 22 countries are: Australia, Bangladesh, Brazil, Canada, China, France, Germany, India, Italy, Japan, Malaysia, Mexico, Philippines, Republic of Korea, Russian Federation, Saudi Arabia, Thailand, Turkey, Ukraine, United Kingdom & United States
To assist others with similar interests, I wrote this Python code for retrieving data from Fred.

## Prerequisits
1) Install pandas, matplotlib, fredapi. 
    pip install pandas
    pip install matplotlib
    pip install fredapi
2) Fred API Key: After downloading Fred API key, paste the 32 digit key in the "Fred_API_KEY.txt" file. 
NOTE: The file should only contain the Fred API Key.

## Refrences
### FRED - Federal Reserve of Economic Data 
* Fred website (https://fred.stlouisfed.org/)
* Fred Twitter account @stlouisfed
### IMF Website
* Very beautiful website (https://www.imf.org/external/datamapper/NGDPDPC@WEO/OEMDC/ADVEC/WEOWORLD)

## License
This project uses the following license: MIT License (https://opensource.org/license/mit/)