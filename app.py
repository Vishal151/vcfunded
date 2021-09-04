import streamlit as st
from vcfunded.lib import get_recent_funded, get_by_category

'# Discover recently funded start-ups'

'### Refresh the page to randomly find more!'

st.write(get_recent_funded())

st.write(get_by_category())
