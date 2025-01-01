import pandas as pd
import matplotlib.pyplot as plt
from colorama import Fore

print(Fore.RED+' _______  _       _________ _______  _______          _________ _______ _________ _______ ') 
print(Fore.RED+'(  ____ \( \      \__   __/(       )(  ___  )|\     /|\__   __/(  ____ \\__   __/(   ___  )')
print(Fore.CYAN+'| (    \/| (         ) (   | () () || (   ) || )   ( |   ) (   | (    \/   ) (   | (   ) |')
print(Fore.CYAN+'| |      | |         | |   | || || || (___) || |   | |   | |   | (_____    | |   | (___) |')
print(Fore.YELLOW+'| |      | |         | |   | |(_)| ||  ___  |( (   ) )   | |   (_____  )   | |   |  ___  |')
print(Fore.YELLOW+'| |      | |         | |   | |   | || (   ) | \ \_/ /    | |         ) |   | |   | (   ) |')
print(Fore.MAGENTA+'| (____/\| (____/\___) (___| )   ( || )   ( |  \   /  ___) (___/\____) |   | |   | )   ( |')
print(Fore.MAGENTA+'(_______/(_______/\_______/|/     \||/     \|   \_/   \_______/\_______)   )_(   |/     \|')

print(Fore.LIGHTGREEN_EX+'''
[01]Plot the mean temperature changes occurred over the past decade
[02]Plot the average temperature change for each year between 1967 and 2023
[03]Plot the five countries have the highest mean temperature change 1961 - 2023
[04]Plot the five countries have the lowest mean temperature change 1961 - 2023

''')
def Import_CSV():
    return pd.read_csv('ClimateChangeData.csv')
def HanddleMissingValue(df, method="fill"):
    if method == "fill":
        df['ISO2'] = df['ISO2'].fillna(0)
    elif method == "remove":
        df = df.dropna()
    return df

df1 = Import_CSV()
df1 = HanddleMissingValue(df1, method="fill")
df1 = HanddleMissingValue(df1, method="remove")
df1.to_csv('ClimateChangeData2.csv', index=False)

def Import_CSV2():
    return pd.read_csv('ClimateChangeData2.csv')
df2 = Import_CSV2()

def MeanTemp_Change_EachCountry(df):
    year=[str(year) for year in range(1961,2024)]
    if all(col in df.columns for col in year):
        df['Mean Temp. Change']=df[year].mean(axis=1)
        df.to_csv('ClimateChangeData2.csv', index=False)
MeanTemp_Change_EachCountry(df2)

def MeanTemp_Change_EachYear(df):
    year=[str(year) for year in range(1967,2024)]
    yearly_mean = df[year].mean(axis=0)
    df3=pd.DataFrame({
        'Year':yearly_mean.index,
        'Mean Temp. Change': yearly_mean.values
    })
    df3.to_csv('ClimateChangeData3.csv', index=False)

MeanTemp_Change_EachYear(df2)

def past_decade(df):
    year = [str(year) for year in range(2013, 2024)]
    df['Past Decade Mean Temp. Change'] = df[year].mean(axis=1)
    plt.figure(figsize=(18, 10))
    plt.bar(df['Country'], df['Past Decade Mean Temp. Change'], color='skyblue', width=0.9)
    plt.title('Mean Temperature Change (2013-2023)', fontsize=30, weight='bold')
    plt.xlabel('Country', fontsize=16)
    plt.ylabel('Mean Temp. Change (°C)', fontsize=16)
    plt.xticks(rotation=90, ha='right', fontsize=8)
    plt.yticks(fontsize=14)
    plt.tight_layout()
    plt.show()

def PlotMeanTempChangeYearly(df):
    year = [str(year) for year in range(1967, 2024)]
    yearly_mean = df[year].mean(axis=0)
    plt.figure(figsize=(10, 6))
    plt.plot(yearly_mean.index, yearly_mean.values, marker='o', color='green')
    plt.title('Average Temperature Change for Each Year (1967-2023)', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Average Temp. Change (°C)', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.tight_layout()
    plt.show()

def PlotTop5Countries(df):
    year = [str(year) for year in range(1961, 2024)]
    df_sorted = df[['Country', 'Mean Temp. Change']].sort_values(by='Mean Temp. Change', ascending=False)
    top_5_countries = df_sorted.head(5)
    df_top5 = df[df['Country'].isin(top_5_countries['Country'])]
    plt.figure(figsize=(12, 8))
    for country in top_5_countries['Country']:
        country_data = df_top5[df_top5['Country'] == country]
        plt.plot(year, country_data[year].values.T, label=country)
    plt.title('Temperature Change for Top 5 Countries (1961-2023)', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Temperature Change (°C)', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.legend(title='Countries')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

def PlotBottom5Countries(df):
    year = [str(year) for year in range(1961, 2024)]
    # Sort the data by mean temperature change in ascending order and get the bottom 5 countries
    df_sorted = df[['Country', 'Mean Temp. Change']].sort_values(by='Mean Temp. Change').head(5)
    bottom_5_countries = df_sorted['Country']
    
    df_bottom5 = df[df['Country'].isin(bottom_5_countries)]
    
    plt.figure(figsize=(12, 8))
    for country in bottom_5_countries:
        country_data = df_bottom5[df_bottom5['Country'] == country]
        plt.plot(year, country_data[year].values.T, label=country, marker='o')
    
    plt.title('Temperature Change for Bottom 5 Countries (1961-2023)', fontsize=14)
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Temperature Change (°C)', fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.legend(title='Countries')
    plt.tight_layout()
    plt.grid(True)
    plt.show()

while True:
    choice = input("Please select an option (1-5): ")
    
    if choice == '1':
        past_decade(df2)
    elif choice == '2':
        PlotMeanTempChangeYearly(df2)
    elif choice == '3':
        PlotTop5Countries(df2)
    elif choice == '4':
        PlotBottom5Countries(df2)
    elif choice == '5':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
