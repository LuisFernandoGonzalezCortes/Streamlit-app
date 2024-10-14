import streamlit as st

st.header("Settings")
st.write(f"You are logged in as {st.session_state.role}.")
st.title("⚙️ Settings")
st.write("Adjust your preferences here.")


# Initialize dark mode state if not set
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False  # Default to light mode

# CSS for light and dark modes
def get_css(dark_mode):
    if dark_mode:
        return """
        <style>
            body {
                background-color: #0E1117;
                color: #FAFAFA;
            }
            .stButton>button {
                background-color: #1F1F1F;
                color: white;
                border: 1px solid #FAFAFA;
            }
            .stTextInput>div>input {
                background-color: #262626;
                color: white;
            }
            .block-container {
                background-color: #0E1117;
            }
        </style>
        """
    else:
        return """
        <style>
            body {
                background-color: #FFFFFF;
                color: black;
            }
            .stButton>button {
                background-color: #F0F2F6;
                color: black;
                border: 1px solid black;
            }
            .stTextInput>div>input {
                background-color: #FFF;
                color: black;
            }
            .block-container {
                background-color: #FFFFFF;
            }
        </style>
        """

# Toggle dark mode with a checkbox
st.sidebar.title("Theme Settings")
toggle = st.sidebar.checkbox("Enable Dark Mode", value=st.session_state.dark_mode)

# Update session state and apply CSS
st.session_state.dark_mode = toggle
st.markdown(get_css(st.session_state.dark_mode), unsafe_allow_html=True)

# App content
st.title("🌞 Light/Dark Mode Toggle with Streamlit")
st.write("Switch between light and dark themes using the checkbox in the sidebar.")

# Example input to demonstrate theming effects
user_input = st.text_input("Enter some text:")
st.write(f"You entered: {user_input}")
st.button("Click me")

