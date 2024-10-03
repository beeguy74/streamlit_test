import streamlit as st

st.title('Hello World!')


name = st.text_input('What is your name?')
if st.button('Submit'):
    st.write(f'Hello, {name}!')

    if st.button('Clear'):
        st.experimental_rerun()
