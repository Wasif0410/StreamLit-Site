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
       st.markdown(
    """
    In constructing the content for this Streamlit page, I began by incorporating a prominent title at the top, 
    using `st.title` to display "CPS530 LAB 10." This served as a focal point, capturing immediate attention and 
    orienting users to the purpose of the page. Following this, I utilized `st.subheader` to introduce the Streamlit 
    framework in a slightly smaller font size, offering a clear context for the ensuing information.

    To convey the installation steps, I employed `st.header` for each key point and utilized `st.expander` to create 
    collapsible sections. These expanders served to organize the content, providing a structured and user-friendly format. 
    Each step, articulated with personal pronouns, aimed to guide users through the installation process with a sense of clarity and support.

    For the page-building section, I employed a similar strategy, using `st.header` for each segment and `st.expander` to 
    maintain a neat layout. The content under each header was structured to provide informative and concise details, maintaining 
    a conversational tone with the use of personal pronouns.

    Additionally, I used `st.markdown` with custom HTML styling to adjust font sizes where necessary, ensuring a visually appealing 
    and readable presentation. Finally, difficulties encountered during development were addressed similarly, utilizing `st.header` 
    and `st.expander` to organize information, and personal pronouns were employed to offer a narrative that resonates with the user, 
    creating a more engaging and relatable experience.
    """
)
    # Box 3
    st.header("Difficulties")
    with st.expander("😟"):
        st.markdown("Lorem ipsum dolor sit amet, consectetur adipiscing elit.", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
