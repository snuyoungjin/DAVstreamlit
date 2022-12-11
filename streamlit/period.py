import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class PeriodDay:
    def __init__(self, df) -> None:
        self.df = df
        self.result = self.df[(self.df[self.df.columns[9]].str.contains('day', na=False))]
        self.unnamed = self.result["Name"].isnull().sum()
        self.Total = self.result["Name"].size

class PeriodWeek:
    def __init__(self, df) -> None:
        self.df = df
        self.result = self.df[(self.df[self.df.columns[9]].str.contains('week', na=False))]
        self.unnamed = self.result["Name"].isnull().sum()
        self.Total = self.result["Name"].size

class PeriodMonth:
    def __init__(self, df) -> None:
        self.df = df
        self.result = self.df[(self.df[self.df.columns[9]].str.contains('month', na=False))]
        self.unnamed = self.result["Name"].isnull().sum()
        self.Total = self.result["Name"].size

class PeriodYear:
    def __init__(self, df) -> None:
        self.df = df
        self.result = self.df[(self.df[self.df.columns[9]].str.contains('year', na=False))]
        self.unnamed = self.result["Name"].isnull().sum()
        self.Total = self.result["Name"].size
