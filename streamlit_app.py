import streamlit as st

st.title('Hello World!')

if 'text' not in st.session_state:
    st.session_state.text = ""

name = st.text_area(st.session_state.text)

if st.button('Submit'):
    st.write(f'Hello, {name}!')

st.session_state.text = name

