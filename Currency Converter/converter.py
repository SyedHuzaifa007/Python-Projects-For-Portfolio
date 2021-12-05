# Importing Libraries & Modules
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Creating Currency Converter Class
class Currency_converer():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

# Creating Converter Method
def convert(self, from_currency, to_currency, amount):
    initial_amount = amount
    if from_currency != 'USD':
        amount = amount / self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 4)
        return amount
        
