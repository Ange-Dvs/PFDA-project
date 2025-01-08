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

def company_mid_term_close_plots(selected_companies, fullnames, data): 
    company1 = selected_companies[0]
    company2 = selected_companies[1]    
    
    company_df1 = data['5y'][data['5y']['Company'] == company1].copy()
    company_df2 = data['5y'][data['5y']['Company'] == company2].copy()
    plt.figure(figsize=(14, 6))
    
    plt.subplot(1,2,1)
    plt.plot(company_df1['Close'], label='Close Price', color='powderblue')

    # calculating and plotting Moving Averages
    company_df1['SMA_50'] = company_df1['Close'].rolling(window=50).mean()
    company_df1['SMA_200'] = company_df1['Close'].rolling(window=200).mean()
    plt.plot(company_df1['SMA_50'], label='50-Day SMA', linestyle='--', color='green')
    plt.plot(company_df1['SMA_200'], label='200-Day SMA', linestyle='--', color='orange')
    
    # plotting Close Prices
    plt.plot(company_df1['Close'], label='Close Price', color='powderblue')

    plt.title(f'{fullnames[company1]} - Close Prices (5-Year)', fontweight='bold')
    plt.xlabel('Date')
    plt.ylabel('Close Price')
    plt.grid(True)

    #repeating for company 2
    plt.subplot(1,2,2)
    plt.plot(company_df2['Close'], label='Close Price', color='powderblue')

  
    company_df2['SMA_50'] = company_df2['Close'].rolling(window=50).mean()
    company_df2['SMA_200'] = company_df2['Close'].rolling(window=200).mean()
    plt.plot(company_df2['SMA_50'], label='50-Day SMA', linestyle='--', color='green')
    plt.plot(company_df2['SMA_200'], label='200-Day SMA', linestyle='--', color='orange')
    
    plt.title(f'{fullnames[company2]} - Close Prices (5-Year)', fontweight='bold')
    plt.xlabel('Date')
    plt.grid(True)


    plt.legend(framealpha=1.0, fontsize=12, ncols=3, bbox_to_anchor=(0.2,1.2))
    plt.suptitle(f'5 year view of Close Prices for {fullnames[company1]} & {fullnames[company2]}', fontsize=20, y=1.10)
    plt.grid(True)
    plt.show()

    
def company_mid_term_volatility_plots(selected_companies, fullnames, data, colours): 
    company1 = selected_companies[0]
    company2 = selected_companies[1]    
    
    company_df1 = data['5y'][data['5y']['Company'] == company1].copy()
    company_df2 = data['5y'][data['5y']['Company'] == company2].copy()

    # fetching the colours for the companies
    colour1 = colours.get(company1)
    colour2 = colours.get(company2)


    plt.figure(figsize=(12, 6))
        
    # Calculate Rolling Volatility for the two companies
    company_df1['Rolling_Volatility'] = company_df1['Close'].pct_change().rolling(window=30).std() * 100
    company_df2['Rolling_Volatility'] = company_df2['Close'].pct_change().rolling(window=30).std() * 100
    
    # Plot Volatility
    plt.plot(company_df1['Rolling_Volatility'], label=f'{fullnames[company1]}Rolling Volatility (30 days)', color=colour1)
    plt.plot(company_df2['Rolling_Volatility'], label=f'{fullnames[company2]}Rolling Volatility (30 days)', color=colour2)


    plt.xlabel('Date')
    plt.ylabel('Volatility (%)')
    plt.legend(framealpha=1.0, fontsize=12)
    plt.title(f'{fullnames[company1]} & {fullnames[company2]} - Rolling Volatility (5-Year)', fontweight='bold')

    plt.grid(True)
    plt.show()

def company_mid_term_trading_volume_plots(selected_companies, fullnames, data): 
    company1 = selected_companies[0]
    company2 = selected_companies[1]    
    
    company_df1 = data['5y'][data['5y']['Company'] == company1].copy()
    company_df2 = data['5y'][data['5y']['Company'] == company2].copy()
    plt.figure(figsize=(14, 6))
    
    plt.subplot(1,2,1)
    # Plot Volume
    plt.bar(company_df1.index, company_df1['Volume'], alpha=0.5, label='Volume')
    plt.plot(company_df1['Volume'].rolling(window=20).mean(), color='green', label='20-Day Avg Volume')
    
    plt.title(f'{fullnames[company1]} - Trading Volume (5-Year)', fontweight='bold')
    plt.xlabel('Date')
    plt.ylabel('Volume')
    plt.grid(True)

    plt.subplot(1,2,2)
    plt.bar(company_df2.index, company_df2['Volume'], alpha=0.5, label='Volume')
    plt.plot(company_df2['Volume'].rolling(window=20).mean(), color='green', label='20-Day Avg Volume')
    
    plt.title(f'{fullnames[company2]} - Trading Volume (5-Year)', fontweight='bold')
    plt.xlabel('Date')
    plt.legend(framealpha=1.0, fontsize=12, ncols=3, bbox_to_anchor=(0.3,1.2))
    plt.suptitle(f'5 year view Trading Volume of {fullnames[company1]} & {fullnames[company2]}', fontsize=20, y=1.10)
    plt.grid(True)
    plt.show()

def company_cumulative_returns(selected_companies, timeframe, data, fullnames, colours):
    company1 = selected_companies[0]
    company2 = selected_companies[1]
    # Fetch the color for the company
    color1 = colours.get(company1)
    color2 = colours.get(company2)

    if timeframe == '5y':
        time = '5 year'
    else:
        time = '10 year'

    company_df1 = data[timeframe][data[timeframe]['Company'] == company1].copy()
    # Normalize returns
    cumulative_returns1 = (1 + company_df1['Close'].pct_change()).cumprod()
    plt.plot(cumulative_returns1, label=f'{company1} Cumulative Returns', color=color1)
    company_df2 = data[timeframe][data[timeframe]['Company'] == company2].copy()
    # Normalize returns
    cumulative_returns2 = (1 + company_df2['Close'].pct_change()).cumprod()
    plt.plot(cumulative_returns2, label=f'{company2} Cumulative Returns', color=color2)
    plt.title(f'{fullnames[company1]} & {fullnames[company2]}- Cumulative Returns ({time})')
    plt.xlabel('Date')
    plt.ylabel('Cumulative Returns')
    plt.grid(True)
    plt.legend()
    plt.show()