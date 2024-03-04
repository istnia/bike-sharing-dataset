import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency

sns.set(style='dark')

#Helper function
def create_sum_season_df(hour_df):
    sum_season_df = hour_df.groupby(["season", "yr"])["cnt"].sum().reset_index()
    return sum_season_df

def create_sum_monthly_df(hour_df):
    sum_monthly_df = hour_df.groupby(["mnth", "yr"])["cnt"].sum().reset_index()
    return sum_monthly_df    

# Load clean data
all_df = pd.read_csv("https://raw.githubusercontent.com/istnia/bike-sharing-dataset/main/hour.csv")

# Prepare dataframe
sum_season_df = create_sum_season_df(all_df)
sum_monthly_df = create_sum_monthly_df(all_df)


st.header("Bike Sharing Dashboard :sparkles:")

# Create Visualization of bike renters by season in 2011
st.subheader("Seasonal Perform of Bike Renters in 2011")
fig, ax = plt.subplots(figsize=(15, 5))
data_2011 = sum_season_df[sum_season_df["yr"]==0] 
sns.barplot(
    y="cnt", 
    x="season",
    data=data_2011,
    ax=ax
)
season_label = ["Spring", "Summer", "Fall", "Winter"]
ax.set_xticks(range(len(season_label)), labels=season_label)
ax.set_title("Number of Bike Renters by Season in 2011", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis="x", labelsize=12)
st.pyplot(fig)

# Create Visualization of bike renters by month in 2011
st.subheader("Monthly Perform of Bike Renters in 2011")

fig, ax = plt.subplots(figsize=(15, 5))
data_2011 = sum_monthly_df[sum_monthly_df["yr"]==0] 
sns.barplot(
    y="cnt", 
    x="mnth",
    data=data_2011,
    ax=ax
)
month_label = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
ax.set_xticks(range(len(month_label)), labels=month_label)
ax.set_title("Number of Bike Renters by Month in 2011", loc="center", fontsize=15)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis="x", labelsize=12)
st.pyplot(fig)

  

