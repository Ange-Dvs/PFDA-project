# importing libaries needed for use within the functions
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def company_1_yr_plots (selected_companies, fullnames, colours, data):
        # lopping through only the companies listed as selected companies
        company1 = selected_companies[0]
        company2 = selected_companies[1]

        fullname1 = fullnames.get(company1)
        fullname2 = fullnames.get(company2)

        # filtering the data for the selected companies
        company_df1 = data['1y'][data['1y']['Company'] == company1].copy()
        company_df2 = data['1y'][data['1y']['Company'] == company2].copy()
        # fetching the colour for the companies
        color1 = colours.get(company1)
        color2 = colours.get(company2)

        # setting up the figure size
        plt.figure(figsize=(20, 10))

        # Subplot 1: Close Price Trends
        plt.subplot(2, 3, 1)
        plt.plot(company_df1['Close'], color=color1)
        plt.title(f'{fullname1} Close Price Trends')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.grid(True)

        # Subplot 2: Volatility Trends
        plt.subplot(2, 3, 2)
        company_df1['Volatility'] = (((company_df1['High'] - company_df1['Low']) / company_df1['Low']) * 100)
        plt.plot(company_df1['Volatility'], color=color1)
        plt.title(f'{fullname1} Volatility Trends')
        plt.xlabel('Date')
        plt.ylabel('Volatility (%)')
        plt.grid(True)

        # Subplot 3: Volume Trends
        plt.subplot(2, 3, 3)
        plt.plot(company_df1['Volume'], color=color1)
        plt.title(f'{fullname1} Volume Trends')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.grid(True)

        # Subplot 4: Close Price Trends
        plt.subplot(2, 3, 4)
        plt.plot(company_df2['Close'], color=color2)
        plt.title(f'{fullname2} Close Price Trends')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.grid(True)

        # Subplot 5: Volatility Trends
        plt.subplot(2, 3, 5)
        company_df2['Volatility'] = (((company_df2['High'] - company_df2['Low']) / company_df2['Low']) * 100)
        plt.plot(company_df2['Volatility'], color=color2)
        plt.title(f'{fullname2} Volatility Trends')
        plt.xlabel('Date')
        plt.ylabel('Volatility (%)')
        plt.grid(True)

        # Subplot 6: Volume Trends
        plt.subplot(2, 3, 6)
        plt.plot(company_df2['Volume'], color=color2)
        plt.title(f'{fullname2} Volume Trends')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.grid(True)
        
        # adding the main title
        plt.suptitle(f'1 year view of {fullname1} & {fullname2}', fontsize=20)
        plt.show()

def company_close_plots(selected_companies, timeframe, fullnames, data): 
    i = 0  # initializing the loop counter to start with the first company in the selected_companies list

    # extracting the data for the first company in the selected list for the specified timeframe
    company_df = data[timeframe][data[timeframe]['Company'] == selected_companies[i]].copy()

    # defining the text label for the plot title based on the selected timeframe
    if timeframe == '5y':
        time = '5 year'  
    else:
        time = '10 year'  

    plt.figure(figsize=(14, 6))  # setting the overall plot size for better readability

    # looping through the two selected companies to create side-by-side plots
    while i < 2: 
        # filtering the data for the current company in the loop
        company_df = data[timeframe][data[timeframe]['Company'] == selected_companies[i]].copy()

        # setting up subplot (1 row, 2 columns, current position i+1)
        plt.subplot(1, 2, (i + 1))

        # plotting the Close Price trend for the company
        plt.plot(company_df['Close'], label='Close Price', color='powderblue')

        # calculating and plotting the 50-Day Simple Moving Average (SMA) to smooth out short-term fluctuations
        company_df['SMA_50'] = company_df['Close'].rolling(window=50).mean()
        plt.plot(company_df['SMA_50'], label='50-Day SMA', linestyle='--', color='green')

        # calculating and plotting the 200-Day Simple Moving Average (SMA) for long-term trend analysis
        company_df['SMA_200'] = company_df['Close'].rolling(window=200).mean()
        plt.plot(company_df['SMA_200'], label='200-Day SMA', linestyle='--', color='orange')

        # plotting the Close Price again for emphasis on the main trend line
        plt.plot(company_df['Close'], color='powderblue')

        # adding a title, labels, enabling grid and showing the plot
        plt.title(f'{fullnames[selected_companies[i]]} - Close Prices ({time})', fontweight='bold')
        plt.xlabel('Date')  
        plt.ylabel('Close Price')  
        plt.grid(True) 

        i += 1  # moving to the next company in the loop

    # adding a legend, title, enabling grid and showing the plot
    plt.legend(framealpha=1.0, fontsize=12, ncols=3, bbox_to_anchor=(0.2, 1.2))
    plt.suptitle(f'{time} view of Close Prices for {fullnames[selected_companies[0]]} & {fullnames[selected_companies[1]]}', fontsize=20, y=1.10)
    plt.grid(True)  
    plt.show()


def company_volatility_plots(selected_companies, timeframe, fullnames, data, colours, rolling_window): 
    i = 0  # initializing the loop counter to start with the first company in the selected_companies list

    # defining the text label for the plot title based on the selected timeframe
    if timeframe == '5y':
        time = '5 year'  # if the timeframe is '5y', label it as '5 year'
    else:
        time = '10 year'  # otherwise, label it as '10 year'

    plt.figure(figsize=(12, 6))  # setting the plot size for better visualization

    # looping through the two selected companies to plot their rolling volatility
    while i < 2:
        # filtering the data for the current company in the loop
        company_df = data[timeframe][data[timeframe]['Company'] == selected_companies[i]].copy()

        # fetching the color assigned to the current company for consistent plot coloring
        colour = colours.get(selected_companies[i])

        # calculating the rolling volatility using the standard deviation of percentage changes in Close Price
        company_df['Rolling_Volatility'] = company_df['Close'].pct_change().rolling(window=rolling_window).std() * 100

        # plotting the rolling volatility trend for the company
        plt.plot(
            company_df['Rolling_Volatility'],
            label=f'{fullnames[selected_companies[i]]} Rolling Volatility ({rolling_window} days)',
            color=colour
        )

        # setting axis labels for clarity
        plt.xlabel('Date')  # x-axis label for time
        plt.ylabel('Volatility (%)')  # y-axis label for percentage volatility

        i += 1  # moving to the next company in the loop

    # adding a legend, title, labels, enabling grid and showing the plot
    plt.legend(framealpha=1.0, fontsize=12)
    plt.title(f'{fullnames[selected_companies[0]]} & {fullnames[selected_companies[1]]} - Rolling Volatility ({time})', fontweight='bold')
    plt.grid(True) 
    plt.show() 



def company_trading_volume_plots(selected_companies, timeframe, fullnames, data): 
    i = 0  # initializing the loop counter to start with the first company in the selected_companies list

    # defining the text label for the plot title based on the selected timeframe
    if timeframe == '5y':
        time = '5 year'  # if the timeframe is '5y', label it as '5 year'
    else:
        time = '10 year'  # otherwise, label it as '10 year'

    plt.figure(figsize=(14, 6))  # setting the overall figure size for better readability

    # looping through the two selected companies to create side-by-side volume plots
    while i < 2:
        # filtering the data for the current company in the loop
        company_df = data[timeframe][data[timeframe]['Company'] == selected_companies[i]].copy()

        # aligning the index to daily frequency to maintain consistent time intervals
        company_df = company_df.asfreq('D')

        # filling in any missing volume data using linear interpolation for smoother visualization
        company_df['Volume'] = company_df['Volume'].interpolate(method='linear', limit_direction='both')

        # creating a subplot for each company (1 row, 2 columns, current position i+1)
        plt.subplot(1, 2, (i + 1))

        # plotting the daily trading volume as a bar chart
        plt.bar(company_df.index, company_df['Volume'], alpha=1, label='Volume', width=1.0)

        # overlaying a 20-day rolling average line to highlight volume trends
        plt.plot(company_df['Volume'].rolling(window=20).mean(), color='green', label='20-Day Avg Volume')

        # adding a title for the individual subplot with the company's full name and timeframe
        plt.title(f'{fullnames[selected_companies[i]]} - Trading Volume ({time})', fontweight='bold')
        plt.xlabel('Date')  # setting the label for the x-axis
        plt.ylabel('Volume')  # setting the label for the y-axis
        plt.grid(True)  # enabling gridlines for better readability

        i += 1  # moving to the next company in the loop

    # adding a legend, overall title, enabling grid and showing the plot
    plt.legend(framealpha=1.0, fontsize=12, ncols=3, bbox_to_anchor=(0.3, 1.2))
    plt.suptitle(f'{time} view Trading Volume of {fullnames[selected_companies[0]]} & {fullnames[selected_companies[1]]}', fontsize=20, y=1.10)
    plt.grid(True) 
    plt.show() 

def company_cumulative_returns(selected_companies, timeframe, data, fullnames, colours):
    i = 0  # initializing the loop counter to start with the first company in the selected_companies list

    # defining the text label for the plot title based on the selected timeframe
    if timeframe == '5y':
        time = '5 year'  
    else:
        time = '10 year'  

    # looping through the two selected companies to plot their cumulative returns
    while i < 2:
        company1 = selected_companies[i]  # selecting the current company from the list

        # fetching the color assigned to the current company for consistent plot coloring
        color = colours.get(selected_companies[i])

        # filtering the data for the current company in the specified timeframe
        company_df = data[timeframe][data[timeframe]['Company'] == selected_companies[i]].copy()

        # calculating the cumulative returns: (1 + daily % change) cumulatively multiplied
        cumulative_returns1 = (1 + company_df['Close'].pct_change()).cumprod()

        # plotting the cumulative returns over time for the company
        plt.plot(cumulative_returns1, label=f'{company1} Cumulative Returns', color=color)

        i += 1  # moving to the next company in the loop

    # adding a legend, title, labels,enabling grid and showing the plot
    plt.title(f'{fullnames[selected_companies[0]]} & {fullnames[selected_companies[1]]} - Cumulative Returns ({time})')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.grid(True) 
    plt.legend() 
    plt.show()


def industry_close_prices_plot(data, time, colours): 
    # filtering the combinded data in the dataframe to just select the data for the 1-year timeframe
    filtered_df = data[data['Timeframe'] == time]

    # getting the full word for the relevant df used to use for the title in the plot
    if time == '1y':
        timeframe = '1 year'
    elif time == '5y':
        timeframe = '5 year'
    else:
        timeframe = '10 year'

    # creating a copy for plotting, so the original data remains unchanged
    plot_df = filtered_df.copy()
    
    # applying interpolation to handle missing values in the 'Close' column
    plot_df['Close'] = plot_df['Close'].interpolate(method='linear')  # Interpolating missing values based on the prior and following values entered

    # creating the plot
    plt.figure(figsize=(12, 6))

    # looping through each industry in the 1-year data by each unique value in the 'Industry' column
    for industry in plot_df['Industry'].unique():
        # filtering data for the specified industry
        industry_data = plot_df[plot_df['Industry'] == industry]
        
        # getting the colour from the colours dictionary specified for that industry
        color = colours.get(industry)

        # ploting the data using the datetime index
        plt.plot(industry_data.index, industry_data['Close'], label=industry, color=color)

    # customising the plot, title & labels
    plt.xlabel('Date')
    plt.ylabel('Mean Close Price')
    plt.title(f'Industry Performance Over {timeframe} (Mean Daily Close Price)')
    plt.legend()
    plt.grid(True)
    plt.show()

def company_stats(industry_dataframes, timeframe, ticker, value_to_check, year_to_check): 
    # filtering the stock data in 2024 and sort by date
    first_comp_2024_entry = industry_dataframes[timeframe][
        (industry_dataframes[timeframe]['Company'] == ticker) & 
        (industry_dataframes[timeframe].index >= pd.to_datetime(f'{year_to_check}-01-01'))
    ].sort_index().iloc[0]

    # displaying the first entry and closing price
    print(f'First {ticker} Entry in {year_to_check}:\n{first_comp_2024_entry}\n')
    print(f'First {ticker} {value_to_check} in {year_to_check}: {first_comp_2024_entry[value_to_check]:.2f}')
    # last entry for the company in 2024
    last_2024_entry = industry_dataframes[timeframe][
        (industry_dataframes[timeframe]['Company'] == ticker) & 
        (industry_dataframes[timeframe].index == industry_dataframes[timeframe][
            industry_dataframes[timeframe].index.year == year_to_check
        ].index.max())].sort_index().iloc[0]


    print(f'Last {ticker} Entry in {year_to_check}:\n', last_2024_entry)

    # latest entry for company along with the latest closing price
    latest_comp_entry = industry_dataframes[timeframe][
        (industry_dataframes[timeframe]['Company'] == ticker)
    ].sort_index().iloc[-1]

    # extracting the latest entry for the specified value to check
    latest_close_price = latest_comp_entry[value_to_check]

    print(f'Latest {ticker} Entry:\n{latest_comp_entry}\n')
    print(f'Latest {ticker} {value_to_check}: {latest_close_price:.2f}')

    print(f'Latest {ticker} Entry:\n', latest_comp_entry)

    # getting the max relevant value and its date for the company in 2024
    max_close_comp_2024 = industry_dataframes[timeframe][
        (industry_dataframes[timeframe]['Company'] == ticker) & 
        (industry_dataframes[timeframe].index.year == year_to_check)
    ][value_to_check].idxmax(), industry_dataframes[timeframe][
        (industry_dataframes[timeframe]['Company'] == ticker) & 
        (industry_dataframes[timeframe].index.year == year_to_check)
    ][value_to_check].max()

    # Second-highest closing price for company in 2024
    second_highest_close_comp_2024 = industry_dataframes[timeframe][
        (industry_dataframes[timeframe]['Company'] == ticker) & 
        (industry_dataframes[timeframe].index.year == year_to_check)
    ].sort_values(by=value_to_check, ascending=False).iloc[1]

       # Second-highest closing price for company in 2024
    third_highest_close_comp_2024 = industry_dataframes[timeframe][
        (industry_dataframes[timeframe]['Company'] == ticker) & 
        (industry_dataframes[timeframe].index.year == year_to_check)
    ].sort_values(by=value_to_check, ascending=False).iloc[3]

    second_highest_close_date = second_highest_close_comp_2024.name
    second_highest_close_value = second_highest_close_comp_2024[value_to_check]

    third_highest_close_date   = third_highest_close_comp_2024.name
    third_highest_close_value =   third_highest_close_comp_2024[value_to_check]

    print(f'Max {ticker} {value_to_check} in {year_to_check}: {max_close_comp_2024[1]:.2f} on {max_close_comp_2024[0].date()}')
    print(f'Second-Highest {value_to_check} for {ticker} in {year_to_check}: {second_highest_close_value:.2f} on {second_highest_close_date.date()}')
    print(f'Third -Highest {value_to_check} for {ticker} in {year_to_check}: {third_highest_close_value:.2f} on {third_highest_close_date.date()}\n')

    # getting the max closing price and its date for the company in 2024
    min_close_comp_2024 = industry_dataframes[timeframe][
        (industry_dataframes[timeframe]['Company'] == ticker) & 
        (industry_dataframes[timeframe].index.year == year_to_check)
    ][value_to_check].idxmin(), industry_dataframes[timeframe][
        (industry_dataframes[timeframe]['Company'] == ticker) & 
        (industry_dataframes[timeframe].index.year == year_to_check)
    ][value_to_check].min()

    print(f'Min {ticker} {value_to_check} in {year_to_check}: {min_close_comp_2024[1]:.2f} on {min_close_comp_2024[0].date()}')

def create_industry_returns_df(industries, industry_dataframes): 
    # restructuring the data to get the close prices based on the 'Close' prices for each company 
    company_returns = industry_dataframes['1y'].pivot_table(index=industry_dataframes['1y'].index, columns='Company', values='Close')

    # calculating the percentage change for the companies close prices row by row individually using the pivot table 
    company_returns = company_returns.pct_change().ffill()

    # converting the pivot table structure to have the pivot headers feed in as values in the rows with new overarching headers created
    company_returns_long = company_returns.stack().rename('Daily_Returns').reset_index() # converts the multiIndex of Date and Company back to columns

        
    # merging the data for the percentage change values to the 1y df based on 'Date' and 'Company' from company_returns_long 
    industry_dataframes['1y'] = industry_dataframes['1y'].reset_index()  # temporarily resetting the index in the orginal dataframe to a 'Date' column to use as a bases to merge the data
    industry_dataframes['1y'] = industry_dataframes['1y'].merge(
        company_returns_long,
        on=['Date', 'Company'],  # matching the rows based explicitly on values for company and date
        how='left' # keeping all data from the left df (industry_dataframes['1y']) in case of missing values from the company_returns_long dataset
    )

    
    # resetting the index back to a DatetimeIndex using the 'Date' column after merging
    industry_dataframes['1y'].set_index('Date', inplace=True)

    # creating mapping from companies to industries using the industries dictionary defined in the beginning of the notebook
    company_to_industry = {}
    for industry, companies in industries.items(): # cycling through the industries and companies in the dictionar
        for company in companies: 
            company_to_industry[company] = industry # looping through the companies individually and setting the pairing in the company_to_industry dictionary of teh company and correspending industry details

    # tranposing the company_returns dataset and using the company_to_industry dictionary to gourp the companies by industry
    grouped_returns = company_returns.T.groupby(company_to_industry)
    industry_mean_returns = grouped_returns.mean() # calculating the mean returns per industry using the grouped data
    industry_returns = industry_mean_returns.T # transposing back to the original format with the dates as rows

    return industry_returns

def company_5year_stats_with_sma(industry_dataframes, timeframe, ticker):
    # function used for generating high level data for the Close price & SMA plots to use for the analysis.
    
    # filtering the data for the selected company
    company_data = industry_dataframes[timeframe][
        industry_dataframes[timeframe]['Company'] == ticker
    ].sort_index()

    # calculating the 50-Day SMA if it doesn't exist
    if '50_SMA' not in company_data.columns:
        company_data['50_SMA'] = company_data['Close'].rolling(window=50).mean()

    # calculating the 200-Day SMA if it doesn't exist
    if '200_SMA' not in company_data.columns:
        company_data['200_SMA'] = company_data['Close'].rolling(window=200).mean()

    # Close Price Analysis 
    min_close_date = company_data['Close'].idxmin()
    min_close_value = company_data['Close'].min()

    max_close_date = company_data['Close'].idxmax()
    max_close_value = company_data['Close'].max()

    print(f'\n{ticker} Close Price (5 Years):')
    print(f'   - Minimum Close Price: {min_close_value:.2f} on {min_close_date.date()}')
    print(f'   - Maximum Close Price: {max_close_value:.2f} on {max_close_date.date()}')

    # 50-Day SMA Analysis
    min_sma50_date = company_data['50_SMA'].idxmin()
    min_sma50_value = company_data['50_SMA'].min()

    max_sma50_date = company_data['50_SMA'].idxmax()
    max_sma50_value = company_data['50_SMA'].max()

    print(f'\n{ticker} 50-Day SMA (5 Years):')
    print(f'   - Minimum 50-Day SMA: {min_sma50_value:.2f} on {min_sma50_date.date()}')
    print(f'   - Maximum 50-Day SMA: {max_sma50_value:.2f} on {max_sma50_date.date()}')

    # 200-Day SMA Analysis 
    min_sma200_date = company_data['200_SMA'].idxmin()
    min_sma200_value = company_data['200_SMA'].min()

    max_sma200_date = company_data['200_SMA'].idxmax()
    max_sma200_value = company_data['200_SMA'].max()

    print(f'\n{ticker} 200-Day SMA (5 Years):')
    print(f'   - Minimum 200-Day SMA: {min_sma200_value:.2f} on {min_sma200_date.date()}')
    print(f'   - Maximum 200-Day SMA: {max_sma200_value:.2f} on {max_sma200_date.date()}')