import streamlit as st

if "role" not in st.session_state:
    st.session_state.role = None

ROLES = [None, "PC", "Professor", "Team"]

def login():
    st.header("Log in")
    role = st.selectbox("Choose your role", ROLES)

    if st.button("Log in"):
        st.session_state.role = role
        st.rerun()

def logout():
    st.header("Log out")

    if st.button("Log out"):
        st.session_state.role = None
        st.rerun()
    #st.session_state.role = None
    #st.rerun()

role = st.session_state.role
logout_page = st.Page(logout, title="Log out", icon=":material/logout:")
settings = st.Page("settings.py", title="Settings", icon=":material/settings:")

visualization = st.Page(
    "Visualization/visualization.py",
    title="Dashboard",
    icon=":material/help:",
    default=(role == "Requester"),
)


ml = st.Page(
    "ml/ml_analysis.py",
    title="Machine Learning",
    icon=":material/healing:",
    default=(role == "Responder"),
)
eda = st.Page(
    "EDA/eda.py",
    title="Exploratory Data Analysis",
    icon=":material/person_add:",
    default=(role == "Admin"),
)
account_pages = [logout_page, settings]
visualization_pages = [visualization]
ml_pages = [ml]
eda_pages = [eda]

st.title("Data Analytics ")
st.logo("images/horizontal_blue.png", icon_image="images/icon_blue.png")

page_dict = {}

if st.session_state.role in ["Professor", "Team"]:
    page_dict["EDA"] = eda_pages
if st.session_state.role in ["Professor", "Team", "PC"]:
    page_dict["Visualization"] = visualization_pages
if st.session_state.role in ["Professor", "Team"]:
    page_dict["Machine Learning"] = ml_pages

if len(page_dict) > 0:
    pg = st.navigation({"Accountt": account_pages} | page_dict)
else:
    pg = st.navigation([st.Page(login)])

pg.run()