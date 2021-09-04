import streamlit as st
from vcfunded.lib import get_recent_funded, get_by_category

'# Discover recently funded start-ups'

'### Refresh the page to randomly find more!'

st.write(get_recent_funded())

st.write(get_by_category())

st.write("If you're a developer you can access more from the related API, which contains 30K+ funded companies (and growing), and more metrics:" , "https://vc-funded-api.herokuapp.com/")