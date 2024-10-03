import streamlit as st

st.title('Hello World!')

if 'text' not in st.session_state:
    st.session_state.text = ""

if isinstance(st.session_state.text, str):
    st.title(f'{st.session_state.text}')

st.text_input(f"{st.session_state.text}")
st.button("Submit")

st.session_state.text = ""

