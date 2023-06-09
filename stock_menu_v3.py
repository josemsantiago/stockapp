# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:57:11 2021

@author: D99003734
"""
from datetime import datetime
from stock_class import Stock, DailyData
from account_class import Traditional, Robo
import matplotlib.pyplot as plt
import csv


def add_stock(stock_list):
    option = ""
    while option != "0":
        print("Add Stock ---")
        symbol = input("Enter Ticker Symbol: ").upper()
        name = input("Enter Company Name: ").capitalize()
        shares = float(input("Enter Number of Shares: "))
        new_stock = Stock(symbol, name, shares)
        stock_list.append(new_stock)
        option = input(
            "Stock Added. Press Enter to add another stock or 0 to stop adding stocks.")

# Remove stock and all daily data


def delete_stock(stock_list):
    print("Delete Stock ---")
    print("Stock List : [", end=" ")
    for stock in stock_list:
        print(stock.symbol, end=" ")
    print("]")
    symbol = input("Which stock do you want to delete? ").upper()
    found = False
    i = 0
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            stock_list.pop(i)
            break
        i += 1
    if found:
        print("Deleted {}".format(symbol))
    else:
        print("Symbol Not Found")
    input("Press Enter to continue***")

# List stocks being tracked


def list_stocks(stock_list):
    print("Stock List ---")
    print("{:<10s} {:<20s} {:<10s}".format("Symbol", "Name", "Shares"))
    print("{:<10s} {:<20s} {:<10s}".format("------", "----", "------"))
    for stock in stock_list:
        symbol = stock.symbol
        name = str(stock.name)
        shares = str(stock.shares)
        print("{:<10s} {:<20s} {:<10s}".format(symbol, name, shares))
    input("Press Enter to continue***")

    # Add Daily Stock Data


def add_stock_data(stock_list):
    print("Add Daily Stock Data ----")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol, " ", end="")
    print("]")
    symbol = input("Which stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        print("Ready to add data for: ", symbol)
        print("Enter Data Separated by Commas - Do Not use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(date, float(price), float(volume))

            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
        print("Date Entry Complete")
    else:
        print("Symbol Not Found ***")
    _ = input("Press Enter to Continue ***")


def investment_type(stock_list):
    print("Investment Account ---")
    balance = float(input("What is your initial balance: "))
    number = input("What is your account number: ")
    acct = input("Do you want a Traditional (t) or Robo (r) account: ")
    if acct.lower() == "r":
        years = float(input("How many years until retirement: "))
        robo_acct = Robo(balance, number, years)
        print("Your investment return is ", robo_acct.investment_return())
        print("\n\n")
    elif acct.lower() == "t":
        trad_acct = Traditional(balance, number)
        temp_list = []
        print("Choose stocks from the list below: ")
        while True:
            print("Stock List: [", end="")
            for stock in stock_list:
                print(stock.symbol, " ", end="")
            print("]")
            symbol = input(
                "Which stock do you want to purchase, 0 to quit: ").upper()
            if symbol == "0":
                break
            shares = float(input("How many shares do you want to buy?: "))
            found = False
            for stock in stock_list:
                if stock.symbol == symbol:
                    found = True
                    current_stock = stock
            if found == True:
                current_stock.shares += shares
                temp_list.append(current_stock)
                print("Bought ", shares, "of", symbol)
            else:
                print("Symbol Not Found ***")
        trad_acct.add_stock(temp_list)


# Function to create stock chart


def display_stock_chart(stock_list, symbol):
    date = []
    price = []
    volume = []
    company = ""
    for stock in stock_list:
        if stock.symbol == symbol:
            company = stock.name
            for dailyData in stock.DataList:
                date.append(dailyData.date)
                price.append(dailyData.close)
                volume.append(dailyData.volume)
    plt.plot(date, price)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(company)
    plt.show()


def display_chart(stock_list):
    print("Stock Chart--")
    print("Stock List: [", end="")
    for stock in stock_list:
        print(stock.symbol, " ", end="")
    print("]")
    symbol = input("Pick stock for chart: ").upper()
    found = False

    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found:
        display_stock_chart(stock_list, current_stock.symbol)
    else:
        print("Symbol not found")
        _ = input("Press enter to continue")


def import_stock_csv(stock_list):
    print("\nAdd historical data to a stock in the stock list\nStock list : [", end = "" )
    for stock in stock_list:
        print(stock.symbol, " ", end="")
    print("]")
    symbol = input("Enter stock symbol: ").upper()
    filename = input("Enter the file name: ")
    for stock in stock_list:
        if stock.symbol == symbol:
            with open(filename,newline='') as stockdata:
                datareader = csv.reader(stockdata)
                next(datareader)
                for row in datareader:
                    daily_data = DailyData(str(row[0]),float(row[4]),float(row[6]))
                    stock.add_data(daily_data)
    display_report(stock_list)


def display_report(stock_list):
    print("Stock report ----")
    for stock in stock_list: 
        print(f"Report for: {stock.symbol}, {stock.name} ")
        print(f"Share: {stock.shares}")
        count =0
        price_total = 0
        volume_total = 0
        low_price = 9999999.99
        high_price = 0
        low_volume = 9999999999
        high_volume = 0
        for daily_data in stock.DataList: 
            count +=1
            price_total += daily_data.close
            volume_total += daily_data.volume
            if daily_data.close < low_price: 
                low_price = daily_data.close
            if daily_data.close > high_price:
                high_price = daily_data.close
            if daily_data.volume < low_volume:
                low_volume = daily_data.volume
            if daily_data.volume > high_volume:
                high_volume = daily_data.volume
            price_change = high_price - low_price
            print(daily_data.date,daily_data.close,daily_data.volume)

        if count > 0: 
            print(f"Summary ----")
            print(f"Low Price: ${low_price:,.2f}")
            print(f"High Price: ${high_price:,.2f}")
            print(f"Average Price: ${(price_total/count):,.2f}")
            print(f"Low Volume: {low_volume}")
            print(f"High Volumen Price: {high_volume}")
            print(f"Change in price: {price_change:,.2f}")
            print(f"Profit/Loss: ${(price_change*stock.shares):,.2f}")
        else: 
            print("****No daily history")
        print("\n\n\n")
    print("---Report Complete---")
    _=input=("Press Enter to continue")
        
def main_menu(stock_list):
    option = ""
    while True:
        print("Stock Analyzer ---")
        print("1 - Add Stock")
        print("2 - Delete Stock")
        print("3 - List stocks")
        print("4 - Add Daily Stock Data (Date, Price, Volume)")
        print("5 - Show Chart")
        print("6 - Investor Type")
        print("7 - Load Data")
        print("0 - Exit Program")
        option = input("Enter Menu Option: ")
        if option == "0":
            print("Goodbye")
            break

        if option == "1":
            add_stock(stock_list)
        elif option == "2":
            delete_stock(stock_list)
        elif option == "3":
            list_stocks(stock_list)
        elif option == "4":
            add_stock_data(stock_list)
        elif option == "5":
            display_chart(stock_list)
        elif option == "6":
            investment_type(stock_list)
        elif option == "7":
            import_stock_csv(stock_list)
        else:

            print("Goodbye")

# Begin program


def main():
    stock_list = []
    main_menu(stock_list)


# Program Starts Here
if __name__ == "__main__":
    # execute only if run as a stand-alone script
    main()
