from pandas.core.frame import DataFrame
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image

st.title('STREAMLIT SAMPLER')
"""
'''python
st.title('STREAMLIT SAMPLER')
'''
"""

st.title('DataFrame')

df = pd.DataFrame({
    'No.1': [1, 2, 3, 4],
    'No.2': [10, 20, 30, 40]
})

st.write('DataFrame')
st.dataframe(df.style.highlight_max(axis=0))
"""
'''python
st.dataframe(df.style.highlight_max(axis=0))
'''
"""
st.write('Table')
st.table(df)
"""
'''python
st.table(df)
'''
"""

st.title('Graph')

df2 = DataFrame(
    np.random.rand(20, 3),
    columns=['a', 'b', 'c']
)
st.write('Line Chart')
st.line_chart(df2)
"""
'''python
st.line_chart(df)
'''
"""

st.write('Area Chart')
st.area_chart(df2)
"""
'''python
st.area_chart(df)
'''
"""


st.write('Bar Chart')
st.bar_chart(df2)
"""
'''python
st.bar_chart(df)
'''
"""

df3 = pd.DataFrame(
    np.random.rand(100, 2) / [50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.write('Map')
st.map(df3)
"""
'''python
st.map(df)
'''
"""

st.title('Layout')

st.write('expander')
expander = st.beta_expander('Title')
expander.write('Body')
"""
'''python
st.write('expander')
expander = st.beta_expander('Title')
expander.write('Body')
'''
"""

st.write('column')
left_column, center_column, right_column = st.beta_columns(3)
left_column.write('column1'), center_column.write(
    'column2'), right_column.write('column3')
"""
'''python
left_column, center_column, right_column = st.beta_columns(3)
left_column.write('column1'), center_column.write(
    'column2'), right_column.write('column3')
'''
"""

st.title('Widget')
st.write('image')
img = Image.open('icon.png')
st.image(img)
"""
'''python
st.write('image')
img = Image.open('icon.png')
st.image(img)
'''
"""

st.write('check box')

checked = st.checkbox('Check')
st.write('status:', checked)
"""
'''python
checked = st.checkbox('Check')
st.write('status:', checked)
'''
"""

st.write('select box')
option = st.selectbox(
    'Select Number',
    list(range(1, 11)),
)
'No.', option
"""
'''python
st.write('select box')
option = st.selectbox(
    'Select Number',
    list(range(1, 11)),
)
'No.', option
'''
"""

text = st.text_input('Input Text')
'text:', text
"""
'''python
text = st.text_input('Input Text')
'text:', text
'''
"""

st.write('slider')
slider_value = st.slider('Set Value', 0, 100, 50)
'Value:', slider_value
"""
'''python
st.write('slider')
slider_value = st.slider('Set Value', 0, 100, 50)
'Value:', slider_value
'''
"""

st.sidebar.title('Sidebar')
st.sidebar.write('Sidebar')
"""
'''python
st.line_chart(df)
'''
"""

st.title('Markdown')
"""
# header1
## header2
### header3
```python
print('markdown')
```
"""
