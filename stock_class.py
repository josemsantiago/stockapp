# José Manuel Santiago Echevarria
# May 8th, 2023
# -*- coding: utf-8 -*-

class Stock:
    def __init__(self, symbol='', name='', shares=0):
        self.symbol = symbol
        self.name = name
        self.shares = shares
        self.DataList = []

    def add_data(self, stock_data):
        self.DataList.append(stock_data)


class DailyData:
    def __init__(self, date='', close='', volume=0):
        self.date = date
        self.close = close
        self.volume = volume

