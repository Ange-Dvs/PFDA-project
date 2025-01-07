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
