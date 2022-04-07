import pandas as pd
import streamlit as st

# Page Title
st.set_page_config(page_title='GA Alarms & Disabled Cells')
st.title(':bar_chart: GA Alarms & Disabled Cells ')
st.subheader("Specific Problem Details")

# importing the excel table into df
df = pd.read_excel("C:/Users/mm598h/Downloads/SpecificProblem_04062022.xlsx")

# Create a list of possible values and multiselect menu with them in it.
st.sidebar.header("Please Filter Here: ")

GeoOwner = st.sidebar.multiselect(
    'Select Geo Owner',
    options = df["Primary_Engineer"].unique()
)

tac = st.sidebar.multiselect(
    'Select Tracking Area Code (TAC)',
    options = df["tac"].unique(),
    default = df["tac"].loc[df['Primary_Engineer'].isin(GeoOwner)].unique()
)

specificproblem = st.sidebar.multiselect(
    'Select the specific problem',
    options = df["specificProblem"].unique(),
    default = df["specificProblem"].unique()
)

NodeID = st.sidebar.multiselect(
    'Select the node ID',
    options = df["NodeId"].unique(),
    default = df["NodeId"].unique()
)

df_selection = df.query(
    "Primary_Engineer== @GeoOwner & tac == @tac & NodeId == @NodeID & specificProblem == @specificproblem"
    )
st.dataframe(df_selection)
