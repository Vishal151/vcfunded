import streamlit as st
from vcfunded.lib import get_recent_funded, get_by_category

st.sidebar.markdown('# Discover recently funded start-ups and scale-ups')
st.sidebar.image('https://hugelolcdn.com/hugereaction.com/i/4034.gif')
st.sidebar.write("If you're a developer you can access more from the related API, which contains 30K+ funded companies (and growing), and more metrics:" )
st.sidebar.write("https://vc-funded-api.herokuapp.com/")

'## Refresh the page to randomly find more!'

st.write(get_recent_funded())

st.write(get_by_category())
