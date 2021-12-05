# Importing Libraries & Modules
import requests
from tkinter import *
import tkinter as tk
from tkinter import ttk

# Creating Curerency Converter Class
class Currency_converer():
    def __init__(self, url):
        self.data = requests.get(url).json()
        self.currencies = self.data['rates']

        