# app.py
import streamlit as st

def main():
    st.title("Simple Streamlit Page with X's")

    num_paragraphs = st.slider("Number of Paragraphs:", min_value=1, max_value=10, value=5)

    for _ in range(num_paragraphs):
        st.write("X" * 100)

if __name__ == "__main__":
    main()
