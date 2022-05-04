from pandas import DataFrame
import streamlit as st
from google.oauth2 import service_account
from gsheetsdb import connect

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)


# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=600)
def run_query(query):
    rows = conn.execute(query)
    df = DataFrame(rows.fetchall())
    return df

sheet_names = ['Foundation Needs',
               'Purchased',
               'Monthly Costs',
               'Down-the-line extras',
               ]
sheet_dict = {f'sheet{i+1}': val for i, val in enumerate(sheet_names)}

def run():
    table_options = st.selectbox("Which table would you like to view?", 
                    tuple(sheet_dict.values())
                     
    )
    if table_options == sheet_names[0]:
        sheet_url = st.secrets["gsheets"]['sheet1']
        # Create Table One
        df = run_query(f'SELECT * FROM "{sheet_url}"')
        df['Cost'] = df['Cost'].replace("$","").astype(float).map('${:,.2f}'.format)
        df['Cumulative_Cost'] = df['Cumulative_Cost'].replace("$","").astype(float).map('${:,.2f}'.format)

        st.header(sheet_names[0])
        st.subheader("Data")
        st.write(df)
        st.subheader("Table")


    elif table_options == sheet_names[1]:
        sheet_url = st.secrets["gsheets"]['sheet2']
        # Create Table Two
        df = run_query(f'SELECT * FROM "{sheet_url}"')
        df['Cost'] = df['Cost'].replace("$","").astype(float).map('${:,.2f}'.format)
        df['Cumulative_Cost'] = df['Cumulative_Cost'].replace("$","").astype(float).map('${:,.2f}'.format)

        st.header(sheet_names[1])
        st.write(df)

    elif table_options == sheet_names[2]:
        sheet_url = st.secrets["gsheets"]['sheet3']
        # Create Table Three
        df = run_query(f'SELECT * FROM "{sheet_url}"')
        df['Cost'] = df['Cost'].replace("$","").astype(float).map('${:,.2f}'.format)
        df['Cumulative_Cost'] = df['Cumulative_Cost'].replace("$","").astype(float).map('${:,.2f}'.format)
        df['Frequency'] = df['Frequency'].astype(int)
        
        
        st.header(sheet_names[2])
        st.write(df)

    elif table_options == sheet_names[3]:
        sheet_url = st.secrets["gsheets"]['sheet4']
        # Create Table Three
        df = run_query(f'SELECT * FROM "{sheet_url}"')
        df['Cost'] = df['Cost'].replace("$","").astype(float).map('${:,.2f}'.format)
        df['Cumulative_Cost'] = df['Cumulative_Cost'].replace("$","").astype(float).map('${:,.2f}'.format)
        
        st.header(sheet_names[3])
        st.write(df)