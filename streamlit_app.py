import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Menu')

streamlit.text('🍟 Omega 3 & Blueberry Oatmeal')

streamlit.text('🥗 Kale, Spinach & Rocket Smoothie')

streamlit.text('🥚 Hard-Boiled Free Range Egg')

streamlit.text('🥑🧇 Avacado Toast')

streamlit.header(' 🍌🍓Build your own Fruit Smoothie 🥝🍇')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)

my_fruit_list = my_fruit_list.set_index('Fruit')
#lets put a pick list here so they can pick teh fruit they want to include
Streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))

#display teh table on teh page
streamlit.dataframe(my_fruit_list)

