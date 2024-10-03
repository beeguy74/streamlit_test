import streamlit as st

st.title('Hello World!')

if 'text' not in st.session_state:
    st.session_state.text = ""

if isinstance(st.session_state.text, str):
    st.title(f'{st.session_state.text}')

test = ""

name = st.text_area(st.session_state.text)

if st.button('Submit'):
    st.write(f'Hello,!')

if st.button('Rerun'):
    st.session_state.text = ""
    st.rerun()

if (name):
    st.write(f'Hello its name !, {name}!')

if (test):
    st.write(f'Hello its test !, {test}!')

st.session_state.text = name

test = ""

