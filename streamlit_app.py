import streamlit
streamlit.header('LIFE')
streamlit.title('Weed of life')
streamlit.text('YOU ONLY LIVE ONCE')
streamlit.text('lets celebrate LIFE')
streamlit.text('yaaaaa ----- hoooooooo******')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.dataframe(my_fruit_list)
