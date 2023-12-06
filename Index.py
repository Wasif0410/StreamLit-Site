# app.py
import streamlit as st
import random

def main():
    st.title("CPS530 LAB 10")
    st.subheader("Streamlit Framework")

    # Installlation
    st.header("Installation")
    with st.expander("Show"):
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

    # Box 2
    st.header("Page Building")
    with st.expander("Show"):
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")

    # Box 3
    st.header("Difficulties")
    with st.expander("Show"):
        st.write("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")


if __name__ == "__main__":
    main()
