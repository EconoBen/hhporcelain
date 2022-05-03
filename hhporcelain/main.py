import report 
import streamlit as st

# Generate sidebar elements
def generate_sidebar_elements():
    pages = {
        "Home": report,
    }

    st.sidebar.title("Navigation")
    selection = st.sidebar.radio("Go to", list(pages.keys()))

    st.sidebar.title("HHPorcelain!")
    st.sidebar.info(
        "\n\n:book: [Spreadsheet](https://docs.google.com/spreadsheets/d/1XmLtn9rPnowNX1DAeMuHfRbU3g5SfLQp_5SBXMVtMr0/edit#gid=0)"
    )

    page = pages[selection]
    page.run()


if __name__ == "__main__":
    generate_sidebar_elements()