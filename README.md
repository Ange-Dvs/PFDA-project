# PFDA-project
Repository for Semester 2 Programming for Data Analytics project.

## Overview
This project analyses stocks across different industries using the **yfinance** library. It focuses on key financial metrics like **close prices**, **volatility**, and **trading volume** to compare performance across sectors.

> Disclaimer: The contents of this notebook should not be used as financial advice


Within the notebook you can expect to see examples of: 
- Data cleaning
- Trend Analysis
- Risk Evaluation using volatility
- Data Visualisation using plots to visualise the dataset

### Choosing a topic & dataset  
In 2024, I noticed that seemingly out of nowhere I was receiving numerous adds for investing apps, financial education apps. More and more influencers on Instagram starting appearing in my recommendation.  

In parallel to this I was receiving a large amount of snippets of news to my inbox, from an investing app I had installed last year, discussing the upcoming US election.  

As an amateur in the world of in


https://algotrading101.com/learn/yfinance-guide/ - Explanation of yfinance
https://mayerkrebs.com/yfinance-library-the-definitive-guide/ - Summary of yfinace 

Point to consider yfinance is not officially supported by Yahoo so the data should not be used for real trading or commercial use. Put for the purpose of demonstrating some data analysis techniques learnt this module it fits well due to the large size of the data and the ability to look at the historical data.  

For each company, that data is fetched using yfinance and the following information extracted:
- Market Capitalisation (marketCap) – Total company value.
- Price-to-Earnings (P/E) Ratio (trailingPE) – Measures valuation relative to earnings.
- Dividend Yield (%) (dividendYield) – Annual return from dividends.

## Cloning repository from GitHub

1. Copy the following URL:
https://github.com/Ange-Dvs/PFDA-assignments.git

2. Open CMDER or if using VS Code open the terminal pane

3. Navigate to the folder where you want to clone the repository to on your machine and type git pull
``git clone https://github.com/Ange-Dvs/PFDA-assignments.git``

4. Set merge as the mode for the pull
``git config pull.rebase false``

5. Initiate the pull of the GitHub repository
``git pull``

6. If the pull has been successful, you should see 6 files pulled from GitHub. The ``readme.md``, the ``.gitignore`` file, the 4 assignments contained within individual Jupyter notebooks and two ``CSV`` files which were generated as a result of running the ``assignment_05_risk.ipynb`` notebook before the final push to GitHub.

## Software used
The software used for the creation of the assignment notebooks included VS Code, Python, Jupyter notebooks & GitHub. 

## Walkthrough of code

## Requirements

### Libraries used
Within the assignments various libraries are used including:
- Libraries:
  - `yfinance`
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`

### Install Dependencies
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
&nbsp;&nbsp;&nbsp;&nbsp;https://medium.com/@polanitzer/volatility-calculation-in-python-estimate-the-annualized-volatility-of-historical-stock-prices-db937366a54d#:~:text=37.6%25%20per%20annum.-,4.%20Volatility,-The%20volatility%20of 
&nbsp;&nbsp;&nbsp;&nbsp;Beta volatility - https://www.investopedia.com/investing/beta-know-risk/#:~:text=Beta%20is%20a%20measure%20of,has%20a%20beta%20above%201.0.
&nbsp;&nbsp;&nbsp;&nbsp;*Volatility* - measures that risk of investing in a stock based on the fluctuation in it's price over time. If a stock is described as high volatility, the stock price changes a lot, while low volatility means it's more stable.  
&nbsp;&nbsp;&nbsp;&nbsp;*Beta Volatility* - measures the relative risk of a stock compared to the overall market. It shows how sensitive a stock is to market movements.

- Grouping data: 
&nbsp;&nbsp;&nbsp;&nbsp;https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html

- Using a dictionary for colours in a plot:
&nbsp;&nbsp;&nbsp;&nbsp;https://stackoverflow.com/questions/73077364/using-a-dictionary-to-plot-a-bar-plot-and-using-another-dictionary-to-give-each

- ``SettingWithCopyWarning`` issue:
&nbsp;&nbsp;&nbsp;&nbsp;https://www.dataquest.io/blog/settingwithcopywarning/

- Understanding Volume patterns:
&nbsp;&nbsp;&nbsp;&nbsp;https://www.investopedia.com/articles/technical/02/010702.asp

- Understanding .pct_change():  
&nbsp;&nbsp;&nbsp;&nbsp;https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html  
&nbsp;&nbsp;&nbsp;&nbsp;https://www.w3schools.com/python/pandas/ref_df_pct_change.asp  
&nbsp;&nbsp;&nbsp;&nbsp;The ``.pct_change`` method is used to return the differences between a value, going row-by-row comparing with the previous row. It's used in the project to check the percentage change between the 'Close' columns from one day to the next. These results are then stored in a new column in the DataFrame called 'Daily_Returns'. These values are then used to assess if there are potentially any industries with similar patterns by comparing their daily returns based on percentage change instead of absolute values.

- Understanding .stack():  
&nbsp;&nbsp;&nbsp;&nbsp;Takes the headers in the pivot table and converts them into values in a row for the "Company" column.

- Understanding .enumerate():  
&nbsp;&nbsp;&nbsp;&nbsp;Works as a way to loop over objects while also keeping count for the loop. The function takes in two arguments, the sequence to be used for the loop and optionally the starting value for the loop. Using indexing enumerate adds the possibility to access key-pair information from a dictionary, this makes it possible to change values to be used in a loop after each iteration. It is used to loop through each column name in ``industry_returns.columns`` (e.g., 'Technology', 'Quantum Computing'). It tracks the index if a counter is defined (``i`` or ``j`` in the project) associated with each column, starting at 0.

- Understanding Boxplot:  
&nbsp;&nbsp;&nbsp;&nbsp;https://www.geeksforgeeks.org/boxplot-using-seaborn-in-python/
&nbsp;&nbsp;&nbsp;&nbsp;https://seaborn.pydata.org/archive/0.11/generated/seaborn.boxplot.html#:~:text=boxplot,-seaborn.&text=Draw%20a%20box%20plot%20to,levels%20of%20a%20categorical%20variable.
&nbsp;&nbsp;&nbsp;&nbsp;https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/statistics/data-presentation/box-and-whisker-plots.html
&nbsp;&nbsp;&nbsp;&nbsp;https://www.tableau.com/chart/what-is-box-and-whisker-plot

Understanding SMA: 
&nbsp;&nbsp;&nbsp;&nbsp;"A simple moving average (SMA) is a simple trading indicator to calculate and use. To calculate it, you add a number of prices together and then divide by the number of prices you added. An example makes the SMA clearer."
&nbsp;&nbsp;&nbsp;&nbsp;https://www.dummies.com/article/business-careers-money/personal-finance/investing/general-investing/how-to-calculate-simple-moving-average-in-trading-160018/

Understanding .cumsum():
&nbsp;&nbsp;&nbsp;&nbsp;https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumsum.html


### Description of common investing terminology

| **Column Name**    | **Description**                                                                 | **Unit**        | **Relevance to Analysis**                                                                                   |
|--------------------|---------------------------------------------------------------------------------|----------------|--------------------------------------------------------------------------------------------------------------|
| **Date (Index)**   | The trading date for the stock. Stored as a **DatetimeIndex**.                   | YYYY-MM-DD HH:MM:SS| Used for **time-series analysis**, rolling calculations, and **trend identification**.                       |
| **Open**           | The **price** of the stock when the market opened on for the trading day.   | USD ($)        | Provides insight into **market sentiment** at the start of each trading day.                                |
| **High**           | The **highest price** reached by the stock during the trading day.               | USD ($)        | Useful for identifying **intraday volatility** and **price fluctuations**.                                  |
| **Low**            | The **lowest price** reached by the stock during the trading day.                | USD ($)        | Complements the **High** value to assess **volatility**.                                                     |
| **Close**          | The **price** of the stock when the market closes on for the trading day. | USD ($)        | Primary metric for **trend analysis**, **returns**, and **correlation studies**.                             |
| **Volume**         | The **number of shares** traded during the day.                                  | Shares         | Measures **market activity**, **liquidity**, and **investor interest**.                                      |
| **Dividends**      | Cash payments made by companies to shareholders per share.                       | USD ($)        | Indicates **profit-sharing** practices and **stability**. |
| **Industry**       | The **sector classification** for the stock (e.g., Technology, Renewable Energy).| Text           | Allows for **grouped comparisons** between industries in performance and correlations.                        |
| **Company**        | The **ticker symbol** representing a specific company.                           | Text           | Enables **company-level filtering** and analysis.                                                            |
| **Timeframe**      | The **data range** selected for analysis (1y, 5y, 10y, etc.).                     | Text           | Provides **context** for comparisons between short-, mid-, and long-term performance.                        |
| **Volatility**     | The **percentage change** between the day’s high and low prices.                  | % (percent)    | Measures **risk** and **price fluctuations** for both **individual stocks** and **industries**.               |
| **Daily Returns**  | The **percentage change** in close price from the previous day.                   | % (percent)    | Evaluates **performance trends**, **correlations**, and **momentum shifts**.                               

##### Links copied from footnotes in GitHub for notebook  
[^1]: https://www.wallstreetzen.com/blog/investing-quotes/?utm_source=chatgpt.com#:~:text=%E2%80%9CInvesting%20is%20simple%2C%20but%20not%20easy.%E2%80%9D%20%E2%80%95%20Warren%20Buffett

[^2]: https://www.finra.org/media-center/newsreleases/2022/new-finra-foundation-research-examines-changing-investor-landscape?utm_source=chatgpt.com#:~:text=New%20investors.%20One%20in%20five%20investors%20have%20less%20than%20two%20years%20of%20experience.%20The%20percentage%20of%20investors%20who%20began%20investing%20in%20the%20two%20years%20prior%20to%20the%20study%20(21%20percent)%20is%20nearly%20as%20large%20as%20the%20percentage%20who%20began%20in%20the%20preceding%20eight%20years%20(25%20percent).

[^3]: https://www.diversitywoman.com/the-pros-and-cons-of-investing-apps

[^4]: https://www.statista.com/forecasts/1474143/global-ai-market-size 

[^5]: https://www.theguardian.com/environment/2024/nov/14/trump-clean-energy-climate-policies

[^6]: https://www.independent.co.uk/news/world/americas/us-politics/trump-musk-friendship-history-b2672224.html

[^7]: https://www.investopedia.com/what-trump-presidency-could-mean-for-electric-vehicles-tesla-musk-8743910

[^8]: https://www.networkworld.com/article/3607725/ibm-announces-50-fold-quantum-speed-improvement.html

[^9]: https://www.dwavesys.com/company/newsroom/press-release/d-wave-achieves-significant-milestone-with-calibration-of-4-400-qubit-advantage2-processor/

[^10]: https://fortune.com/2025/01/09/nvidia-ceo-jensen-huang-tanks-quantum-computing-stocks/