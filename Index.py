# app.py
import streamlit as st
import random

def main():
    st.title("CPS530 LAB 10")
    st.subheader("Streamlit Framework")

    # Installlation
    st.header("Installation")
    with st.expander("Show"):
        st.write(get_random_text())

    # Box 2
    st.header("Page Building")
    with st.expander("Show"):
        st.write(get_random_text())

    # Box 3
    st.header("Difficulties")
    with st.expander("Show"):
        st.write(get_random_text())

def get_random_text():
    # Generating random text
    paragraphs = ["Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
                  "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
                  "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris.",
                  "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur."]
    return random.choice(paragraphs)

if __name__ == "__main__":
    main()
