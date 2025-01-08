# importing libaries needed for use within the functions
import matplotlib.pyplot as plt

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
        plt.plot(company_df['Close'], label='Close Price', color='powderblue')
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

    # Add labels, title, and legend
    plt.xlabel('Date')
    plt.ylabel('Mean Close Price')
    plt.title(f'Industry Performance Over {time} (Mean Daily Close Price)')
    plt.legend()
    plt.grid(True)
    plt.show()