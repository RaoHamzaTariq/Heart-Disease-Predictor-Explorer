import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 

def show_explore_page():
    st.title("Explore the Heart Disease Data")
    st.write("""### Unleash the transformative insights and patterns""")

    df = pd.read_csv('heart_disease_data.csv')

    st.write("### Preview the dataset")
    st.dataframe(df)

    st.write("### Number of Patients by target and sex")
    fig, ax = plt.subplots()
    sns.barplot(x='target', y='age',hue = 'sex', data=df, ax=ax)
    ax.set_title('Bar Plot')
    plt.xlabel('0=No Heart Disease, 1=Heart Disease') 
    plt.ylabel("Age")
    st.pyplot(fig)

    st.write("### Age vs Heart Rate")
    # Finding Patterns in Data Using Scatter Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    # Scatter plot with red points for target=1 and green points for target=0
    sns.scatterplot(x='age', y='thalach', hue='target', data=df, palette={0: 'green', 1: 'red'}, ax=ax)
    # Customize plot
    ax.set_xlabel('Age')
    ax.set_ylabel('Heart Rate')
    ax.legend(['No Heart Problem', 'Heart Problem'])
    # Display the plot using Streamlit
    st.pyplot(fig)

    st.write("### Age and Thalach Distribution")
    # Create subplots with two histograms side by side
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
    sns.histplot(df['age'], bins=20, kde=True, color='blue',ax=ax1)
    # Customize plot
    ax1.set_xlabel('Age')
    ax1.set_ylabel('Frequency')
    sns.histplot(df['age'], bins=20, kde=True, color='red',ax=ax2)
    # Customize plot
    ax2.set_xlabel('Thalach')
    ax2.set_ylabel('Frequency')
    st.pyplot(fig)


    st.write("### Chest Pain vs Heart Disease")
    # Create a crosstab and plot it using Seaborn
    ct = pd.crosstab(df['cp'], df['target'])
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=ct.index, y=ct[1], color='red', label='Heart Problem')
    sns.barplot(x=ct.index, y=ct[0], color='green', label='No Heart Problem')
    # Customize plot
    ax.set_xlabel('Chest Pain Type')
    ax.set_ylabel('Counts')
    ax.legend(['No Heart Problem', 'Heart Problem'])
    # Display the plot using Streamlit
    st.pyplot(fig)

    st.write("### Correlation between columns")
    cor_map = df.corr()
    home,room = plt.subplots(figsize=(10,10))
    sns.heatmap(cor_map, annot=True, linewidths=0.5, fmt='0.2f')
    st.pyplot(home)

