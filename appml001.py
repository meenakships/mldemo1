#import libraries
import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
#matplotlib.use('Agg')
import seaborn as sns 

#Remove Warnings
st.balloons()
#st.set_option('deprecation.showPyplotGlobalUse', False)
st.title("Campus Placements")

#import dataset
df = pd.read_csv('campusrec.csv')
st.subheader("First Thirty")
cr = df.head(30)
#Display the table
st.table(cr)
#pairplot
st.subheader("Pairplot")
sns.pairplot(cr,hue='gender',palette='rainbow')
st.pyplot()
#Correation
st.subheader("Heatmap")
sns.heatmap(cr.corr(),cmap='coolwarm',annot=True)
st.pyplot()
#distplot
st.subheader("Distplot")
sns.distplot(cr['ssc_p'],kde=True)
st.pyplot()
st.subheader("Barplot")
sns.barplot(data=df,x='hsc_s',y='degree_p')
st.pyplot()
st.subheader("Jointplot")
sns.jointplot(x='etest_p',y='salary',data=df,kind='scatter',color='b')
st.pyplot()

# SIDE Bar
st.sidebar.header("Contents")
st.sidebar.text("This data gives a set of students and their degrees,marks and placement results.")