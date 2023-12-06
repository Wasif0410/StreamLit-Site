# app.py
import streamlit as st

def main():
    st.title("CPS530 LAB 10")
    st.subheader("Streamlit Framework")

    # Installlation
    st.header("Installation")
    with st.expander("STEPS"):
        st.markdown("""
            1. **Installed Python:**
               - Downloaded Python from the official website.
               - Followed the installation instructions for the operating system.
            
            2. **Created a Virtual Environment:**
               - Used the terminal to create a virtual environment using the following commands:
                 ```bash
                 pip install virtualenv
                 python -m venv myenv
                 myenv\\Scripts\\activate  # On Windows
                 ```
            
            3. **Installed Streamlit:**
               - Activated the virtual environment.
               - Ran the command `pip install streamlit` to install Streamlit.
            
            4. **Created a Streamlit App File:**
               - Used a text editor to create a Python file (e.g., `app.py`).
               - Added basic Streamlit code to the file.
            
            5. **Ran Streamlit App Locally:**
               - Navigated to the directory containing `app.py` in the terminal.
               - Executed the command `streamlit run app.py`.
               - Opened a web browser and accessed the app at `http://localhost:8501`.
            
            6. **Shared Streamlit App (Optional):**
               - Deployed the app to a cloud platform like Streamlit Sharing or Heroku. Deployment steps varied based on the chosen platform.
        """, unsafe_allow_html=True)

    # Box 2
    st.header("Page Building")
    with st.expander("😁"):
        st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=True)

    # Box 3
    st.header("Difficulties")
    with st.expander("😟"):
        st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
