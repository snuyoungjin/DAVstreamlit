import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import period
from statsmodels.stats.proportion import proportions_ztest

data = pd.read_csv('Austin_Animal_Center_Outcomes.csv')
df = pd.DataFrame(data)
checkData = []
st.markdown("""
<style>
.font-20 {
    font-size:20px !important;
}
</style>
""", unsafe_allow_html=True)

def main_page():
    st.markdown("# Austin animal center(Taxes) data")
    st.sidebar.markdown("# Main data")
    df
    checkData.append(df.columns[0])
    checkData.append(df.columns[1])
    for i in df.columns[2:]:
        checkColumn = st.checkbox(i)
        if checkColumn:
            checkData.append(i)
    st.markdown("# Filtering by colums")
    df[checkData]
    st.markdown("# Summary")
    df.columns[9]

def page2():
    st.sidebar.markdown("# day/week/month/year")
    st.markdown('# Protection Period')
    periodFilter = st.radio(
        "Filtered by protection periods",
        ('Under 1 week', '1 week ~ 1 month', '1 month ~ 1 year', 'Over 1 year')
    )
    period_day = period.PeriodDay(df)
    period_week = period.PeriodWeek(df)
    period_month = period.PeriodMonth(df)
    period_year = period.PeriodYear(df)
    if periodFilter == 'Under 1 week':    
        st.dataframe(period_day.result)
        st.write(f'<p class = "font-20">name unknowned : {period_day.unnamed} per {period_day.Total} - {"%.2f%%" % (period_day.unnamed / period_day.Total * 100.0)}</p>', unsafe_allow_html=True)
    elif periodFilter == '1 week ~ 1 month':
        st.dataframe(period_week.result)
        st.write(f'<p class = "font-20">name unknowned : {period_week.unnamed} / {period_week.Total} - {"%.2f%%" % (period_week.unnamed / period_week.Total * 100.0)}</p>', unsafe_allow_html=True)
    elif periodFilter == '1 month ~ 1 year':
        st.dataframe(period_month.result)
        st.write(f'<p class = "font-20">name unknowned : {period_month.unnamed} / {period_month.Total} - {"%.2f%%" % (period_month.unnamed / period_month.Total * 100.0)}</p>', unsafe_allow_html=True)
    else:
        st.dataframe(period_year.result)
        st.write(f'<p class = "font-20">name unknowned : {period_year.unnamed} / {period_year.Total} - {"%.2f%%" % (period_year.unnamed / period_year.Total * 100.0)}</p>', unsafe_allow_html=True)
    
    st.markdown('# name-unknown ratio(%)')
    periodChartBar = pd.DataFrame(
        [period_day.unnamed / period_day.Total * 100.0,
        period_week.unnamed / period_week.Total * 100.0,
        period_month.unnamed / period_month.Total * 100.0,
        period_year.unnamed / period_year.Total * 100.0]
    )
    periodChartBar.index = ['1. Under 1 week',
    '2. 1 week ~ 1 month',
    '3. 1 month ~ 1 year',
    '4. Over 1 year']
    st.bar_chart(periodChartBar)

def page3():
    st.markdown("# Page 3 🎉")
    st.sidebar.markdown("# Page 3 🎉")

def page4():
    st.markdown("# Page 4")
    st.sidebar.markdown("# Page 4")

page_names_to_funcs = {
    "Main Page": main_page,
    "Page 2": page2,
    "Page 3": page3,
    "Page 4": page4
}

selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
page_names_to_funcs[selected_page]()