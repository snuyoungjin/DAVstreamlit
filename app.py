view = [100,150,30]
view
import streamlit as st
st.write('# Youtube view')
st.bar_chart(view)
import pandas as pd
st.write('## sview')
sview = pd.Series(view)
sview