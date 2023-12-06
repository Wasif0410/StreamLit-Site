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
        """, unsafe_allow_html=True)

    # Box 2
    st.header("Page Building")
    with st.expander("😁"):
       st.markdown(
    """
    In constructing the content for this Streamlit page, I began by incorporating a prominent title at the top, 
    using `st.title` to display "CPS530 LAB 10." This served as a focal point, capturing immediate attention and 
    orienting users to the purpose of the page. Following this, I utilized `st.subheader` to introduce the Streamlit 
    framework in a slightly smaller font size, offering a clear context for the ensuing information.

    To convey the installation steps, I employed `st.header` for each key point and utilized `st.expander` to create 
    collapsible sections. These expanders served to organize the content, providing a structured and user-friendly format. 

    For the page-building section, I employed a similar strategy, using `st.header` for each segment and `st.expander` to 
    maintain a neat layout.

    Additionally, I used `st.markdown` with custom HTML styling to adjust font sizes where necessary, ensuring a visually appealing 
    and readable presentation.
    """
)
    # Box 3
    st.header("Difficulties")
    with st.expander("😟"):
        st.markdown("""
        In the installation process for Streamlit, I faced a setback when the `pip install` command repeatedly failed. 
        Upon investigation, I discovered the issue stemmed from using an outdated Python version incompatible with Streamlit's requirements. 
        To resolve this, I upgraded my Python version, successfully overcoming the installation hurdle and emphasizing the importance of version compatibility in the development workflow.
        """)



if __name__ == "__main__":
    main()
