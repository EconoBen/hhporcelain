import gspread_pandas
from pandas import DataFrame
import streamlit as st
from google.oauth2 import service_account
import json

key_dict = json.loads(st.secrets["textkey"])
creds = service_account.ServiceAccountCredentials.Credentials.from_service_account_info(key_dict)


def run():
    table_options = st.selectbox("Which table would you like to view?", 
                    ('Foundation needs'.capitalize(),
                     'Down-the-line extras'.capitalize(),
                     'Monthly Costs'.capitalize(),
                     'Purchased'.capitalize()
                     )
    )
    # Starting Budget
    id = '1XmLtn9rPnowNX1DAeMuHfRbU3g5SfLQp_5SBXMVtMr0'
    df = gspread_pandas.spread.Spread(id).sheet_to_df().reset_index()

    if table_options == 'Foundation needs'.capitalize():
        # Create Table One

        table_one_title = df.columns[0]
        tbl1_rows = [i for i, x in enumerate(df['Foundation Needs'].values) if len(set(x)) == 1][0]
        tbl_one_unformatted = df.iloc[:tbl1_rows, :1].values

        tbl_one_cols = tbl_one_unformatted[0][0]
        items = [lst[0][0].strip() for lst in tbl_one_unformatted[1:] if lst[0][0]]
        links = [lnk[0][1].strip() for lnk in tbl_one_unformatted[1:]][:len(items)]
        costs = [cst[0][2].strip() for cst in tbl_one_unformatted[1:]][:len(items)]
        tbl_one = DataFrame().from_dict({tbl_one_cols[0].capitalize(): items,
                                    tbl_one_cols[1].capitalize(): links,
                                    tbl_one_cols[2].capitalize(): costs})

        st.header(table_one_title.capitalize())
        st.write(tbl_one)
    elif table_options == 'Down-the-line extras'.capitalize():

        # Table Two
        tbl1_rows = [i for i, x in enumerate(df['Foundation Needs'].values) if len(set(x)) == 1][0]
        table_two_title = df.iloc[tbl1_rows:tbl1_rows+1,:1].values[0][0][0]
        tbl_two_unformatted = df.iloc[tbl1_rows+1:, :1].values

        tbl_two_cols = tbl_two_unformatted[0][0]
        items = [lst[0][0].strip() for lst in tbl_two_unformatted[1:] if lst[0][0]]
        links = [lnk[0][1].strip() for lnk in tbl_two_unformatted[1:]][:len(items)]
        costs = [cst[0][2].strip() for cst in tbl_two_unformatted[1:]][:len(items)]
        tbl_two = DataFrame().from_dict({tbl_two_cols[0].capitalize(): items,
                                        tbl_two_cols[1].capitalize(): links,
                                        tbl_two_cols[2].capitalize(): costs})

        st.header(table_two_title.capitalize())
        st.write(tbl_two)
    elif table_options == 'Monthly Costs'.capitalize():
        # Table Three

        tbl_three_title = df.columns[2]
        tbl_three_range = [ i for i, x in enumerate(df.iloc[:,2:3].values) if x == ''][0]
        tbl_three_unformatted = df.iloc[:tbl_three_range,2:5]
        tbl_three_cols = tbl_three_unformatted.iloc[:1,:].values[0]
        tbl_three_unformatted = tbl_three_unformatted.iloc[1:,].values

        items = [lst[0] for lst in tbl_three_unformatted if lst[0]]
        costs = [cst[1].strip() for cst in tbl_three_unformatted][:len(items)]
        freq = [lst[2] for lst in tbl_three_unformatted][:len(items)]
        tbl_three = DataFrame().from_dict({tbl_three_cols[0].capitalize(): items,
                                        tbl_three_cols[1].capitalize(): freq,
                                        tbl_three_cols[2].capitalize(): costs})

        st.header(tbl_three_title.capitalize())
        st.write(tbl_three)

    elif table_options == 'Purchased'.capitalize():
        # Table Four
        tbl_three_range = [ i for i, x in enumerate(df.iloc[:,2:3].values) if x == ''][0]
        tbl_four_range = [i+1 for i, x in enumerate(df.iloc[tbl_three_range:,-1:].values) if '$' in x[0]][1]
        tbl_four_unformatted = df.iloc[tbl_four_range:,2:]
        tbl_four_title = tbl_four_unformatted.iloc[:1,:].values[0][0]
        tbl_four_cols = list(set(tbl_four_unformatted.iloc[1:,].values[0]))

        items = [x[0] for x in tbl_four_unformatted.iloc[2:,].values]
        costs = [x[1] for x in tbl_four_unformatted.iloc[2:,2:].values]
        tbl_four = DataFrame().from_dict({tbl_four_cols[0].capitalize(): items,
                                        tbl_four_cols[1].capitalize(): costs
                                        })

        st.header(tbl_four_title.capitalize())
        st.write(tbl_four)