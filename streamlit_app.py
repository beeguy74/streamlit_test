import streamlit as st

st.title('Hello World!')

if 'text' not in st.session_state:
    st.session_state.text = ""

if isinstance(st.session_state.sum, str):
    st.title(f'{st.session_state.sum}')

name = st.text_input(st.session_state.text)

if st.button('Submit'):
    st.write(f'Hello, {name}!')

st.session_state.text = name

