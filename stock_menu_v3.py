# -*- coding: utf-8 -*-
"""
Created on Mon Aug 30 22:57:11 2021

@author: D99003734
"""
from datetime import datetime
from stock_class import Stock, DailyData
# from account_class import  Traditional, Robo
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
    print("Stock List: [",end="")
    for stock in stock_list:
        print(stock.symbol," ",end="")
    print("]")
    symbol = input("Which stock do you want to use?: ").upper()
    found = False
    for stock in stock_list:
        if stock.symbol == symbol:
            found = True
            current_stock = stock
    if found == True:
        print("Ready to add data for: ",symbol)
        print("Enter Data Separated by Commas - Do Not use Spaces")
        print("Enter a Blank Line to Quit")
        print("Enter Date,Price,Volume")
        print("Example: 8/28/20,47.85,10550")
        data = input("Enter Date,Price,Volume: ")
        while data != "":
            date, price, volume = data.split(",")
            daily_data = DailyData(date,float(price),float(volume))
          
            current_stock.add_data(daily_data)
            data = input("Enter Date,Price,Volume: ")
        print("Date Entry Complete")
    else:
        print("Symbol Not Found ***")
    _ = input("Press Enter to Continue ***")



def investment_type(stock_list):
    print("This method is under construction")

# Function to create stock chart


def display_stock_chart(stock_list, symbol):
    print("This method is under construction")

# Display Chart


def display_chart(stock_list):
    print("This method is under construction")

 # Get price and volume history from Yahoo! Finance using CSV import.


def import_stock_csv(stock_list):
    print("This method is under construction")

    # Display Report


def display_report(stock_list):
    print("This method is under construction")


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