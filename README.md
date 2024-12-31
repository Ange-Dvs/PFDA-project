# PFDA-project
Repository for Semester 2 Programming for Data Analytics project

## Overview
This project analyses stocks across different industries using the **yfinance** library. It focuses on key financial metrics like **Market Capitalisation**, **P/E Ratio**, and **Dividend Yield** to compare performance across sectors.

## Choosing a topic/dataset
https://algotrading101.com/learn/yfinance-guide/ - Explanation of yfinance
https://mayerkrebs.com/yfinance-library-the-definitive-guide/ - Summary of yfinace 

Point to consider yfinance is not officially supported by Yahoo so the data should not be used for real trading or commercial use. Put for the purpose of demonstrating some data analysis techniques learnt this module it fits well due to the large size of the data and the ability to look at the historical data.  

For each company, that data is fetched using yfinance and the following information extracted:
- Market Capitalisation (marketCap) – Total company value.
- Price-to-Earnings (P/E) Ratio (trailingPE) – Measures valuation relative to earnings.
- Dividend Yield (%) (dividendYield) – Annual return from dividends.

## Current Features
- Fetches stock data for selected companies in four industries:
  1. Technology
  2. Quantum Computing
  3. Electric Vehicles
  4. Renewable Energy
- Calculates and displays average metrics for each sector:
  - Market Capitalisation (in billions)
  - P/E Ratio
  - Dividend Yield (%)

## Future Plans
- **Data Cleaning**: Handle missing data
- **Trend Analysis**: Add historical performance metrics and seasonal trends
- **Risk Evaluation**: Calculate volatility
- **Visualisation**: Add plots to visualise the dataset

## Requirements
- Python
- Libraries:
  - `yfinance`
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`

## Install Dependencies
The requirments.txt file can be used to install the dependencies before running the project.
`pip install -r requirements.txt`

## Usage Instructions


## Tips for yfinace
https://medium.com/@kasperjuunge/yfinance-10-ways-to-get-stock-data-with-python-6677f49e8282 - 10 useful functions within yfinance
https://github.com/RaghavsScarletSplendour/YahooFinanceTutorial/blob/main/Yfinance_tutorial.ipynb - Jupyter notebook walking through installation and basic use of yfinance
https://www.youtube.com/watch?v=3FG6ATh90IU - YouTube tutorial for yfinance


- Small multiple line charts with one line highlighted for emphasis
https://python-graph-gallery.com/125-small-multiples-for-line-chart/

- List for companies in S&P 500 (used to see what symbol is used to reference a company)
https://en.wikipedia.org/wiki/List_of_S%26P_500_companies

## External links and resources
- Understanding market capitalisation and how it's calculated:  
&nbsp;&nbsp;&nbsp;&nbsp;https://www.investopedia.com/investing/market-capitalization-defined/ 
&nbsp;&nbsp;&nbsp;&nbsp;https://www.nerdwallet.com/article/investing/what-is-market-cap

- Understanding Price-to-Earnings ratios, the different types and how it's calculated: 
&nbsp;&nbsp;&nbsp;&nbsp;https://www.investopedia.com/terms/p/price-earningsratio.asp

- Understanding the dividends yield: 
&nbsp;&nbsp;&nbsp;&nbsp;https://www.investopedia.com/terms/d/dividendyield.asp

- Understanding interpolation: 
&nbsp;&nbsp;&nbsp;&nbsp;https://www.investopedia.com/terms/i/interpolation.asp 
&nbsp;&nbsp;&nbsp;&nbsp;https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html 
&nbsp;&nbsp;&nbsp;&nbsp;Interpolation is a technique used to fill in missing data, two related values are used to fill in the missing value.  In this project it will be used to fill in the gaps in data for days in which the New York stock exchange is not open.  This will help show a neater visual when plotting the data and fill in the NaN values. 

- Understanding volatility: 
&nbsp;&nbsp;&nbsp;&nbsp; https://medium.com/@polanitzer/volatility-calculation-in-python-estimate-the-annualized-volatility-of-historical-stock-prices-db937366a54d#:~:text=37.6%25%20per%20annum.-,4.%20Volatility,-The%20volatility%20of 
&nbsp;&nbsp;&nbsp;&nbsp; Beta volatility - https://www.investopedia.com/investing/beta-know-risk/#:~:text=Beta%20is%20a%20measure%20of,has%20a%20beta%20above%201.0.

- Grouping data: 
&nbsp;&nbsp;&nbsp;&nbsp; https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

- Using a dictionary for colours in a plot:
&nbsp;&nbsp;&nbsp;&nbsp; https://stackoverflow.com/questions/73077364/using-a-dictionary-to-plot-a-bar-plot-and-using-another-dictionary-to-give-each

- ``SettingWithCopyWarning`` issue:
&nbsp;&nbsp;&nbsp;&nbsp; https://www.dataquest.io/blog/settingwithcopywarning/

- Understanding Volume patterns:
&nbsp;&nbsp;&nbsp;&nbsp; https://www.investopedia.com/articles/technical/02/010702.asp