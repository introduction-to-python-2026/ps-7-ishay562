import yfinance as yf
import pandas as pd
from datetime import datetime
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import wb

TICKER = "NVDA"
ticker_data = yf.download(TICKER, start='2023-01-01', end=datetime.now().strftime('%Y-%m-%d'))
print(ticker_data.head())
first_two_cols_iloc = ticker_data.iloc[:, 0:2]
print("--- Result using .iloc[:, 0:2] ---")
print(first_two_cols_iloc)

data_without_date_index = ticker_data.iloc[:, 1].values
#display(data_without_date_index)
plt.hist(data_without_date_index, bins=20, edgecolor='black')

plt.xlabel(f"{TICKER} Close price")
plt.ylabel('days')
plt.title(f"Histogram of {TICKER} close price since 1/1/2023" )
#plt.figure(figsize=(10, 5))
#Add more x-axis ticks for better granularity
min_price = int(np.floor(data_without_date_index.min()))
max_price = int(np.ceil(data_without_date_index.max()))
plt.xticks(np.arange(min_price, max_price + 10, 10))
plt.show()
# --- 1. Define Parameters ---
population_indicator = 'SP.POP.TOTL'
country_code = 'ISR'
start_year = 2010
end_year = datetime.today().year

# --- 2. Fetch the Data ---
population_data = wb.download(
    indicator=population_indicator,
    country=country_code,
    start=start_year,
    end=end_year
).rename(columns={'SP.POP.TOTL': 'Population'})

# --- 3. Clean and Prepare Data ---
population_data = population_data.reset_index(level='country', drop=True)

# Sort by year in ascending order for positive correlation visualization
population_data = population_data.sort_index(ascending=True)


# --- 4. Create Scatter Plot ---
plt.figure(figsize=(10, 6))
plt.scatter(x=population_data.index, y=population_data['Population'])
plt.xlabel('Year')
plt.ylabel('Population') # Updated label
plt.title(f'Population of {country_code} from {start_year} to {end_year}')
plt.grid(True)

# Set y-axis limits
plt.ylim(7_500_000, 10_000_000)

# Disable scientific notation on the y-axis
plt.ticklabel_format(style='plain', axis='y')

# Removed: Format y-axis to display whole numbers
# def millions_formatter(x, pos):
#     return f'{int(x)}'
# formatter = mticker.FuncFormatter(millions_formatter)
# plt.gca().yaxis.set_major_formatter(formatter)

plt.show()
