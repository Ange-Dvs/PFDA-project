# importing libaries needed for use within the functions
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def company_1_yr_plots (selected_companies, industry, fullnames, colours, data):
    # Loop through only the selected companies
        company1 = selected_companies[0]
        company2 = selected_companies[1]

        fullname1 = fullnames.get(company1)
        fullname2 = fullnames.get(company2)

        # Filter the data for the selected company
        company_df1 = data['1y'][data['1y']['Company'] == company1].copy()
                # Filter the data for the selected company
        company_df2 = data['1y'][data['1y']['Company'] == company2].copy()
               # Fetch the color for the company
        color1 = colours.get(company1)
         # Fetch the color for the company
        color2 = colours.get(company2)

        # Set up the figure size
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

        # Subplot 1: Close Price Trends
        plt.subplot(2, 3, 4)
        plt.plot(company_df2['Close'], color=color2)
        plt.title(f'{fullname2} Close Price Trends')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.grid(True)

        # Subplot 2: Volatility Trends
        plt.subplot(2, 3, 5)
        company_df2['Volatility'] = (((company_df2['High'] - company_df2['Low']) / company_df2['Low']) * 100)
        plt.plot(company_df2['Volatility'], color=color2)
        plt.title(f'{fullname2} Volatility Trends')
        plt.xlabel('Date')
        plt.ylabel('Volatility (%)')
        plt.grid(True)

        # Subplot 3: Volume Trends
        plt.subplot(2, 3, 6)
        plt.plot(company_df2['Volume'], color=color2)
        plt.title(f'{fullname2} Volume Trends')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.grid(True)
        
        # Add the main title
        plt.suptitle(f'1 year view of {fullname1} & {fullname2}', fontsize=20)
        plt.show()

def company_close_plots(selected_companies, timeframe, fullnames, data): 
    i=0
    company_df = data[timeframe][data[timeframe]['Company'] == selected_companies[i]].copy()
    if timeframe == '5y':
        time = '5 year'
    else:
        time = '10 year'
    plt.figure(figsize=(14, 6))
    
    while i < 2: 
        company_df = data[timeframe][data[timeframe]['Company'] == selected_companies[i]].copy()
        plt.subplot(1,2,(i+1))
        plt.plot(company_df['Close'], label='Close Price', color='powderblue')
        # calculating and plotting Moving Averages
        company_df['SMA_50'] = company_df['Close'].rolling(window=50).mean()
        company_df['SMA_200'] = company_df['Close'].rolling(window=200).mean()
        plt.plot(company_df['SMA_50'], label='50-Day SMA', linestyle='--', color='green')
        plt.plot(company_df['SMA_200'], label='200-Day SMA', linestyle='--', color='orange')
        
        # plotting Close Prices
        plt.plot(company_df['Close'], color='powderblue')
        plt.title(f'{fullnames[selected_companies[i]]} - Close Prices ({time})', fontweight='bold')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.grid(True)
        i+=1

    plt.legend(framealpha=1.0, fontsize=12, ncols=3, bbox_to_anchor=(0.2,1.2))
    plt.suptitle(f'{time} view of Close Prices for {fullnames[selected_companies[0]]} & {fullnames[selected_companies[1]]}', fontsize=20, y=1.10)
    plt.grid(True)
    plt.show()

def company_volatility_plots(selected_companies, timeframe, fullnames, data, colours): 
    i=0
    if timeframe == '5y':
        time = '5 year'
    else:
        time = '10 year'
    plt.figure(figsize=(12, 6))
        
    while i < 2:
        company_df = data[timeframe][data[timeframe]['Company'] == selected_companies[i]].copy()
        colour = colours.get(selected_companies[i])
        # Calculate Rolling Volatility for the two companies
        company_df['Rolling_Volatility'] = company_df['Close'].pct_change().rolling(window=30).std() * 100
        plt.plot(company_df['Rolling_Volatility'], label=f'{fullnames[selected_companies[i]]}Rolling Volatility (30 days)', color=colour)
        plt.xlabel('Date')
        plt.ylabel('Volatility (%)')
        i+=1


    plt.legend(framealpha=1.0, fontsize=12)
    plt.title(f'{fullnames[selected_companies[0]]} & {fullnames[selected_companies[1]]} - Rolling Volatility ({time})', fontweight='bold')
    plt.grid(True)
    plt.show()


def company_trading_volume_plots(selected_companies, timeframe, fullnames, data): 
    i=0
    if timeframe == '5y':
        time = '5 year'
    else:
        time = '10 year'
    
    plt.figure(figsize=(14, 6))
    while i < 2:
        company_df = data[timeframe][data[timeframe]['Company'] == selected_companies[i]].copy()
        plt.subplot(1,2,(i+1))
        # Plot Volume
        plt.bar(company_df.index, company_df['Volume'], alpha=0.5, label='Volume')
        plt.plot(company_df['Volume'].rolling(window=20).mean(), color='green', label='20-Day Avg Volume')

        plt.title(f'{fullnames[selected_companies[i]]} - Trading Volume ({time})', fontweight='bold')
        plt.xlabel('Date')
        plt.ylabel('Volume')
        plt.grid(True)

        i += 1

    plt.legend(framealpha=1.0, fontsize=12, ncols=3, bbox_to_anchor=(0.3,1.2))
    plt.suptitle(f'{time} view Trading Volume of {fullnames[selected_companies[0]]} & {fullnames[selected_companies[1]]}', fontsize=20, y=1.10)
    plt.grid(True)
    plt.show()

def company_cumulative_returns(selected_companies, timeframe, data, fullnames, colours):
    i = 0
    if timeframe == '5y':
        time = '5 year'
    else:
        time = '10 year'
        
    while i < 2: 
            company1 = selected_companies[i]
                # Fetch the color for the company
            color = colours.get(selected_companies[i])


            company_df = data[timeframe][data[timeframe]['Company'] == selected_companies[i]].copy()
            # Normalize returns
            cumulative_returns1 = (1 + company_df['Close'].pct_change()).cumprod()
            plt.plot(cumulative_returns1, label=f'{company1} Cumulative Returns', color=color)
            i += 1

    plt.title(f'{fullnames[selected_companies[0]]} & {fullnames[selected_companies[1]]}- Cumulative Returns ({time})')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.grid(True)
    plt.legend()
    plt.show()

def industry_close_prices_plot(data, time, colours): 
    # filtering the combinded data in the dataframe to just select the data for the 1-year timeframe
    filtered_df = data[data['Timeframe'] == time]

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
    plt.title(f'Industry Performance Over {time} (Mean Daily Close Price)')
    plt.legend()
    plt.grid(True)
    plt.show()
 
def industry_close_SMA_plots(selected_industries, timeframe, data): 
    if timeframe == '5y':
        time = '5 year'
    else:
        time = '10 year'

    # dynamically determining the number of subplots based on the number of selected industries
    num_industries = len(selected_industries)
    plt.figure(figsize=(14, 6))

    for i, industry in enumerate(selected_industries): 
        # filtering the data for the selected industry
        industry_df = data[timeframe][data[timeframe]['Industry'] == industry].copy()

        # calculating the average close price for the industry
        industry_avg = industry_df.groupby('Date')['Close'].mean()
        
        # calculating the Moving Averages for the average close price
        industry_avg_SMA_50 = industry_avg.rolling(window=50).mean()
        industry_avg_SMA_200 = industry_avg.rolling(window=200).mean()

        # plotting the data
        plt.subplot(1, num_industries, i + 1)  # Adjust subplots dynamically
        plt.plot(industry_avg, label='Avg Close Price', color='powderblue')
        plt.plot(industry_avg_SMA_50, label='50-Day SMA', linestyle='--', color='green')
        plt.plot(industry_avg_SMA_200, label='200-Day SMA', linestyle='--', color='orange')

        # customising the plot, title & labels
        plt.title(f'{industry} - Avg Close Prices ({time})', fontweight='bold')
        plt.xlabel('Date')
        plt.ylabel('Close Price')
        plt.grid(True)
    
    plt.tight_layout()
    plt.suptitle(f'{time} Trends: Close Prices & Moving Averages', y=1.15, fontsize=24)
    plt.legend(framealpha=1.0, fontsize=12, ncols=3, bbox_to_anchor=(0.4, 1.15))
    plt.show()


def industry_monthly_return_trends(industry_dataframes, colours, industries_to_compare):

    # List to store processed industry DataFrames
    industry_daily_list = []

    # Loop through each industry to calculate daily returns and store in the list
    for industry in industries_to_compare:
        # Filtering for the current industry
        industry_df = industry_dataframes['5y'][industry_dataframes['5y']['Industry'] == industry].copy()

        # Resampling only numeric columns
        industry_numeric = industry_df.select_dtypes(include='number')
        industry_daily = industry_numeric.resample('D').mean()

        # Adding back the 'Industry' column
        industry_daily['Industry'] = industry

        # Calculating Daily Returns
        industry_daily['Daily_Returns'] = industry_daily['Close'].pct_change(fill_method=None)

        # Extracting the month for seasonality analysis
        industry_daily['Month'] = industry_daily.index.month

        # Appending the processed DataFrame to the list
        industry_daily_list.append(industry_daily)

    # --- Plotting the Side-by-Side Box Plots with Fixed Y-Axis Limits ---
    plt.figure(figsize=(18, 7))

    # Loop through the processed data for plotting
    for i, industry_daily in enumerate(industry_daily_list):
        # Create subplot for each industry
        plt.subplot(1, 2, i + 1)

        # Create the box plot
        sns.boxplot(data=industry_daily, x='Month', y='Daily_Returns', color=colours.get(industries_to_compare[i]))

        # Customize x-axis with month names
        plt.xticks(ticks=range(0, 12), labels=[
            'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
            'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
        ])

        # Add titles and labels
        plt.title(f'{industries_to_compare[i]}', fontsize=16)
        plt.xlabel('Month', fontsize=18, x=1.02)
        plt.ylabel('Daily Returns', fontsize=18)
        plt.ylim(-0.15, 0.15)  # Fixed y-axis limits for both plots
        plt.grid(axis='y', linestyle='--', alpha=0.7)

        # Hide y-ticks on the second plot but keep the grid
        if i == 1:
            plt.tick_params(axis='both', left=False, labelleft=False)
            plt.xlabel(None)
            plt.ylabel(None)

    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.suptitle('Monthly Return Trends (5-Year)', fontsize=20, y=1.03)

    # Show the combined plot
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

    print(f'Second-Highest {value_to_check} for {ticker} in {year_to_check}: {second_highest_close_value:.2f} on {second_highest_close_date.date()}')
    print(f'Third -Highest {value_to_check} for {ticker} in {year_to_check}: {third_highest_close_value:.2f} on {third_highest_close_date.date()}\n')


    print(f'Max {ticker} {value_to_check} in {year_to_check}: {max_close_comp_2024[1]:.2f} on {max_close_comp_2024[0].date()}')

    # getting the max closing price and its date for the company in 2024
    min_close_comp_2024 = industry_dataframes[timeframe][
        (industry_dataframes[timeframe]['Company'] == ticker) & 
        (industry_dataframes[timeframe].index.year == year_to_check)
    ][value_to_check].idxmin(), industry_dataframes[timeframe][
        (industry_dataframes[timeframe]['Company'] == ticker) & 
        (industry_dataframes[timeframe].index.year == year_to_check)
    ][value_to_check].min()

    print(f'Min {ticker} {value_to_check} in {year_to_check}: {min_close_comp_2024[1]:.2f} on {min_close_comp_2024[0].date()}')
