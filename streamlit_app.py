import streamlit
import pandas

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

streamlit.title('My parents new healthy diner')

streamlit.header('Breakfast Menu')

streamlit.write('🥣 Omega 3 & Blueberry Oatmeal')
streamlit.write('🥗 Kale, Spinach & Rocket Smoothie')
streamlit.write('🐔 Hard-Bolied Free-Range Egg')
streamlit.write('🥑🍞 Avocado Toast')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

streamlit.dataframe(my_fruit_list)
