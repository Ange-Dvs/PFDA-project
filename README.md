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

As an amateur in the world of investing this influx of investing related information and adds peaked my interest as a potential topic to dive into for the Programming for Data Analytics project. 

After landing on the final decision to use the stock market as a topic for analysis, I begin searching for a suitable dataset that would be able to provide the details required and give the option for expanding the timeframe and amount of data analysed. 

This is where ``yfinance`` came in, with a number of tutorials and summaries available online explaining the ``Python`` library. 

It is worth noting that ``yfinance`` is not officially supported by Yahoo so the data should not be used for real trading or commercial use.  
Put for the purpose of demonstrating some data analysis techniques learnt this module it fits well due to the large size of the data and the ability to look at the historical data.  


## Installation & Usage Instructions

### Software used
The software used for the creation of the assignment notebooks included VS Code, Python, Jupyter notebooks & GitHub. 

### Cloning repository from GitHub

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

### Install Dependencies
The requirments.txt file can be used to install the dependencies before running the project.
`pip install -r requirements.txt`

### Run the Notebook
1. Launch Jupyter Notebook on your system and navigate to ``stocks.ipynb`` file in the directory and open it.
2. Execute the cells sequentially, by clicking Run all. This will load the weather dataset, render the markdown cells and generate the plots.

If any errors occur, check your dependencies and ensure all libraries are installed correctly.

### Dependencies
The notebook uses the following Python libraries:

  - `yfinance`
  - `pandas`
  - `numpy`
  - `matplotlib`
  - `seaborn`

These can be installed via the requirements.txt file.

## Walkthrough of project steps

### myfunctions.py

The ``myfunctions.py`` file contains functions created to simplify and reuse code throughout the notebook to reduce clutter. 
The majority of functions are used to create the plots used in the notebook. 

#### Overview of functions within myfunctions.py

##### Company Performance Visualization
- ``company_1_yr_plots``: Generates multi-plot graphs displaying Close Price, Volatility, and Trading Volume trends for two selected companies over the past year.
- ``company_close_plots``: Compares Close Prices along with 50-day and 200-day Simple Moving Averages (SMA) for selected companies over 5 or 10 years.
- ``company_volatility_plots``: Plots rolling volatility to highlight stock price fluctuations over time.
- ``company_trading_volume_plots``: Visualizes trading volume trends with a 20-day moving average overlay.

##### Return and Performance Analysis

- ``company_cumulative_returns``: Displays cumulative returns to measure long-term company performance.
- ``create_industry_returns_df``: Calculates and organizes daily returns across industries for comparative analysis.

##### Industry Trend Analysis

- ``industry_close_prices_plot``: Visualizes industry-wide performance by plotting mean daily close prices across different industries.

##### Detailed Statistical Analysis
The following functions have been removed from the notebook after they were no longer needed. Note if using functions ensure the notebook has run it's in entirety first as some of the values used are created during the execution of the notebook. 

- ``company_stats``: Extracts and reports key statistics (first, latest, max, and min values) for a selected stock within a specified year.
- ``company_5year_stats_with_sma``: Provides a detailed breakdown of Close Prices and SMA (50-day and 200-day) trends for the past five years.

### stocks.ipynb

#### Project set-up 

1.**Importing Libraries and Custom Functions:**  
- Imports essential libraries for data manipulation, analysis, and visualization.
- Loads custom plotting and analysis functions from ``myfunctions.py``.

2.**Defining Industries and Companies:**  
- Maps industries to relevant company stock tickers.
- Provides full company names for better labelling in visualizations.

3.**Initializing DataFrames for Multiple Timeframes:**  
- Sets up empty DataFrames for storing historical stock data across different periods.

4.**Checking Data Availability:**  
- Checks if each company has 5 years of historical data available.
- Identifies data limitations for newer industries (e.g., Quantum Computing, EVs).

5.**Data Collection for Multiple Time Periods:**  
- Downloads historical stock data for each company over 1, 5, and 10 years.
- Skips unavailable data for newer industries.
- Adds industry, company, and timeframe labels for easy filtering.

6.**Data Cleaning and Validation:**  
- Checks for missing values in the datasets to ensure data quality.

7.**Time zone Standardization:**  
- Converts timestamps from the New York time zone to UTC for consistency in analysis.

8.**Defining Colour Schemes for Visualizations:**  
- Establishes consistent colour coding for industries and companies in all visualizations.

Once the data is cleaned the functions created in ``myfunctions.py`` are used throughout the project to help form the bases of the analysis. 

#### Industry-Wide Performance Analysis code within stocks.ipynb notebook

1.**Resampling Data for Industry Performance Analysis:** 

- Resamples daily close prices to calculate the mean close price for each industry across 1, 5, and 10-year timeframes.
- Prepares data for industry performance visualization.

2.**Plotting Industry Close Prices:**  
- Visualizes mean daily close prices across industries over a 1-year timeframe.
- Highlights industry-specific growth trends and market behaviours.

3.**Calculating Industry Volatility:**  
- Calculates daily volatility as a percentage for each industry using high and low stock prices.
- Prepares data for volatility trend analysis.

4.**Plotting Industry Volatility Trends:**  
- Visualizes rolling 30-day volatility trends to assess industry risk and market stability.
- Helps identify which industries experience higher or lower market volatility.

5.**Comparing Industry Averages (Close Price, Volatility, Volume):**
- Compares average Close Prices, Volatility, and Trading Volume across industries.
- Provides a clear overview of industry performance and risk levels.

6.**Bubble Chart: Close Price vs. Volume (Size = Volatility):**
- Visualizes the relationship between Close Price and Volume, with bubble size representing volatility.
- Offers a multidimensional view of market dynamics for each industry.

7.**Industry Correlation Analysis:**
- Measures the correlation between industries based on Close Prices.
- Helps identify industries that move together or inversely.

8.**Rolling Correlation of Daily Returns:**
- Analyses 90-day rolling correlations between industries' daily returns.
- Reveals how industry relationships evolve over time.

9.**Distribution of Daily Returns:**
- Displays the distribution of daily returns for each industry.
- Highlights volatility and the frequency of extreme price changes.

10.**Violin Plot of Daily Returns:**
- Combines distribution and volatility in a single violin plot for each industry.
- Illustrates how daily returns are distributed and how volatile they are.

## Libraries used

<font size="4"><b>yfinance</b></font>
        ``yfinance`` is a library in Python used for retrieving historical market data directly from Yahoo Finance.
It allows for the collection of financial data such as stock prices and trading volume which are utilized throughout the analysis.
It offers flexibility in selecting specific timeframes, multiple stock tickers, making it a valuable library for data analysis and visualization of the stock market.

> ``.Ticker`` (Function) -  used to access a specific company's stock data by providing its ticker symbol enabling the retrieval of historical prices and financial information.

<font size="4"><b>Pandas</b></font>   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`Pandas` is a library in Python used for data analysis which enables the use of two-dimensional tables called DataFrames.  
Within the assignments the ``Pandas`` library is used to read in the data from the various ``CSV`` files.  
It is also used to convert date information in the ``CSV`` file to a datetime series.

The following are methods used throughout the assignments from `Pandas`: 

> ``.concat`` (Function) - Combines multiple DataFrames or Series along a particular axis (rows or columns), allowing for efficient data merging and appending.

> ``.DataFrame`` (Function) - Creates a two-dimensional, tabular data structure with labelled axes (rows and columns).

> ``.to_datetime`` (Function) - Converts a string or other formats to a ``datetime`` object.  

> ``.to_numeric`` (Function) - Converts a Series to numeric types, coercing errors if specified.  

> ``.set_index`` (Method) - Sets a DataFrame column as the index.

> ``.resample`` (Method) - Resamples time-series data to a different frequency.  

> ``.mean`` (Method) - Calculates the mean of values along a DataFrame or Series axis.

> ``.Timestamp`` (Function) - Represents a specific point in time.

> ``.isna`` (Function) - Detects missing values in a Series or DataFrame.

> ``.rolling`` (Method) - Provides rolling window calculations for time-series data.

> ``.corr`` (Method) - Calculates the pairwise correlation between numerical columns in a DataFrame, measuring how strongly variables are related to each other.

> ``.groupby`` (Method) – Splits a DataFrame into groups based on the values in one or more columns, allowing for aggregation, transformation, or filtering of data within each group.

> ``.pivot_table`` (Method) – Creates a spreadsheet-style pivot table that allows for summarizing and aggregating data by specifying index (rows), columns, and values, with customizable aggregation functions.

> ``.unique`` (Method) – Returns the unique values from a Series or DataFrame column, eliminating any duplicates.

> ``.agg`` (Method) – Allows the application of one or multiple aggregation functions (like mean, sum, min, max) to a DataFrame or Series for summarizing data.

> ``.keys`` (Method) – Returns the keys (column labels for DataFrames or index labels for Series) of a pandas object, similar to how it works with Python dictionaries.

> ``.cumsum`` (Method) – Calculates the cumulative sum of a Series or DataFrame along a specified axis. Each value is added to the sum of all previous values, making it useful for tracking cumulative totals over time, such as cumulative returns in stock analysis.

> ``.stack`` (Method) – Reshapes a DataFrame by pivoting columns into rows, turning wide-format data into a long-format. This is helpful for converting hierarchical columns into a more analysis-friendly structure.

> ``.pct_change`` (Method) – Computes the percentage change between the current and previous element in a Series or DataFrame. It’s commonly used in financial analysis to measure daily, monthly, or yearly growth or decline in data like stock prices.

<font size="4"><b>Matplotlib.pyplot</b></font>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The ``Matplotlib.pyplot`` library is used for visual representation of the dataset.
This library enables the creation of many types of plots including line plots, pie charts and bar charts which are generated throughout the assignments.  
There is a high-level of customisation possible with options to switch up the colour, markers, legend, labels and titles of the plots.

The following are methods used from `Matplotlib.pyplot`: 

> ``.legend`` (Function) - Adds a legend to a plot to label the data.

> ``.title`` (Function) - Add a title to a plot, the title can be customised to alter how the font looks (weight and size) and location on the plot.

> ``.show`` (Function) - Used after the plot has been created to show the plot.

> ``.grid`` (Function) - Can be used to add or remove gridlines from the plot to enhance readability of the plot. 

> ``.bar`` (Function) - Create a bar chart to display categorical data.

> ``.hist`` (Function) -  Creates a histogram to visualize the distribution of data.

> ``.plot`` (Function) - Create a line plot by default. It can also be adapted for a variety of visualizations by adjusting its parameters.

> ``.subplot`` (Function) - Supports the creation of multiple plots in one figure. The number of plots which can be displayed is controlled by values entered for the number of columns and rows required. 

> ``.xticks`` & ``.yticks`` (Function) - Offers the ability to change the default tick settings on the x and y axes including the possibility to change the position of the ticks on the plot borders or remove the ticks completely.

> ``.xlabel`` & ``.ylabel`` (Function) - Sets the heading for the axes and allows customisation of the font with the possibility to change the style, font and location of the labels.

> ``.ylim`` (Function) - Sets limit of the y-axis. This is useful when it's needed to overwrite the default value or range for the axes.

> ``.figtext`` (Function) - Adds text to plots.

> ``.figure`` (Function) - Create a new figure object, holding all elements of a plot, such as axes, titles, legends, and other visual elements. The size of the figure can also be specified within the ``.figure`` function.

> ``.tight_layout`` (Function) - Automatically adjusts subplot spacing to prevent overlap.

> ``.show`` (Function) -  Displays the current plot or figure.

<font size="4"><b>Seaborn</b></font>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;``Seaborn`` is used for advanced data visualization and statistical analysis.
This library builds on ``Matplotlib``, offering a more user-friendly interface and aesthetically pleasing default styles for plots such as heatmaps, scatterplots, and boxplots.  
There is a high level of customization available, with options to easily manage colour palettes, adjust axes styling, add statistical annotations, and create visually appealing multi-plot grids.

> ``.violinplot`` (Function) - Creates a violin plot to visualize the distribution, probability density, and variability of data across different categories.

> ``.heatmap`` (Function) - Creates a heatmap to visualize data in a matrix format using colour gradients, often used to show correlations or patterns between variables.

<font size="4"><b>Default Python Functionality (Built-in or Standard Library)</b></font>  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;The built-in Python functionality and standard library provide tools for data manipulation and processing.
These features include operations like sorting, summing, and string manipulation, which are frequently applied throughout the assignments.
They offer a straightforward and efficient way to handle core programming tasks without requiring external libraries.

>``ennumerate`` (Function) - Adds a counter to an iterable, returning both the index and the value in a loop, making it easier to track positions while iterating.

>``.min`` (Function) - Returns the smallest value in an iterable or among arguments.

>``.max`` (Function) - Returns the largest value in an iterable or among arguments. 

>``.sum`` (Function) - Returns the sum of values in an iterable.  

>``.append`` (Method) - Adds an element to the end of a list.

>``.tolist`` (Method) - Converts an array-like object to a Python list.
built in

> ``.items`` (Method) - Iterates over DataFrame columns as key-value pairs.  

> ``.get`` (Method) -  Retrieves the value for a specified key from a dictionary. If the key does not exist, it returns None or a user-defined default value instead of raising an error..  

 References and Resources

During the creation of this project, various online resources and documentation were utilized to support stock data analysis, visualization, and market understanding. Below is a categorized summary of these references, along with brief explanations of their relevance to the project.

---

### **YFinance Documentation and Tutorials**

- **[10 Useful Functions in YFinance](https://medium.com/@kasperjuunge/yfinance-10-ways-to-get-stock-data-with-python-6677f49e8282)**  
  Provided insights into advanced features and useful functions within the `yfinance` package for stock data retrieval.

- **[YFinance Jupyter Notebook Tutorial](https://github.com/RaghavsScarletSplendour/YahooFinanceTutorial/blob/main/Yfinance_tutorial.ipynb)**  
  Guided the setup, installation, and basic usage of `yfinance` in Python notebooks.

- **[YFinance YouTube Tutorial](https://www.youtube.com/watch?v=3FG6ATh90IU)**  
  Offered a step-by-step video walkthrough of how to use `yfinance` for fetching and analysing stock data.

---
### **Data Visualization Techniques**

- **[Small Multiples for Line Charts](https://python-graph-gallery.com/125-small-multiples-for-line-chart/)**  
  Provided inspiration for creating multiple line charts with emphasis on specific data series.

- **[Using Dictionaries for Plot Colours](https://stackoverflow.com/questions/73077364/using-a-dictionary-to-plot-a-bar-plot-and-using-another-dictionary-to-give-each)**  
  Helped in dynamically assigning colours to plots based on industries or companies.

- **[Matplotlib Dates API](https://matplotlib.org/stable/api/dates_api.html)**  
  Guided the customization of date formatting and interval settings on plots.

---

### **Stock Market Concepts and Financial Metrics**

- **[Market Capitalization Explained](https://www.investopedia.com/investing/market-capitalization-defined/)**  
  Detailed the calculation and significance of market capitalization in evaluating companies.  

- **[Price-to-Earnings (P/E) Ratio](https://www.investopedia.com/terms/p/price-earningsratio.asp)**  
  Explained how to interpret P/E ratios in stock analysis.

- **[Dividend Yield](https://www.investopedia.com/terms/d/dividendyield.asp)**  
  Provided insights into how dividend yields reflect a company’s profitability.

- **[Understanding Volume Patterns](https://www.investopedia.com/articles/technical/02/010702.asp)**  
  Explained how trading volume can indicate market sentiment.

- **[Beta Volatility](https://www.investopedia.com/investing/beta-know-risk/)**  
  Covered how beta measures a stock’s volatility relative to the market.

---

### **Data Analysis and Manipulation**

- **[Pandas GroupBy Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html)**  
  Used for aggregating and analysing grouped data by industry or company.

- **[Interpolation Techniques](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.interpolate.html)**  
  Explained how to handle missing data, especially during non-trading days.

- **[Handling SettingWithCopyWarning](https://www.dataquest.io/blog/settingwithcopywarning/)**  
  Provided solutions to avoid unintended modifications in DataFrames.

- **[Pandas `.pct_change()` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pct_change.html)**  
  Explained how to calculate daily returns for stock data analysis.

- **[Pandas `.stack()` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.stack.html)**  
  Used for reshaping pivot tables into long-format DataFrames.

- **[Python `enumerate()` Function](https://docs.python.org/3/library/functions.html#enumerate)**  
  Applied for efficient looping with counters, especially in correlation analysis.

---

### **Statistical Analysis and Technical Indicators**

- **[Volatility Calculation in Python](https://medium.com/@polanitzer/volatility-calculation-in-python-estimate-the-annualized-volatility-of-historical-stock-prices-db937366a54d)**  
  Explained how to compute annualized volatility for stock prices.

- **[Simple Moving Average (SMA)](https://www.dummies.com/article/business-careers-money/personal-finance/investing/general-investing/how-to-calculate-simple-moving-average-in-trading-160018/)**  
  Described how to calculate and interpret SMAs for trend analysis.

- **[Pandas `.cumsum()` Documentation](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.cumsum.html)**  
  Applied for cumulative return calculations in the analysis.

---

### **Advanced Plotting and Statistical Visualization**

- **[Seaborn Boxplot Documentation](https://seaborn.pydata.org/archive/0.11/generated/seaborn.boxplot.html)**  
  Helped in visualizing data distribution and detecting outliers.

- **[Seaborn Violin Plot Documentation](https://seaborn.pydata.org/generated/seaborn.violinplot.html)**  
  Used for visualizing both data distribution and density.

---

### **Company and Market Data Resources**

- **[List of S&P 500 Companies](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)**  
  Used to verify stock symbols for major publicly traded companies.

- **[Investopedia – Interpolation](https://www.investopedia.com/terms/i/interpolation.asp)**  
  Clarified how interpolation is used to fill gaps in time-series data.

---

## **Practical Application of Resources**

- **Stock Data Collection:**  
  `yfinance` tutorials and documentation guided the setup and data fetching process.

- **Data Analysis:**  
  Pandas and financial metric resources were vital for analysing daily returns, volatility, and correlations.

- **Visualization:**  
  Plotting techniques and colour mapping resources ensured clear and consistent data visualizations.

- **Statistical Analysis:**  
  Financial indicators like SMA, P/E ratio, and beta volatility were used to interpret stock trends and risks.

--- 

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