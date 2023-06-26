import streamlit as st
import numpy as np
import joblib as jb
from predict_cost import predict

st.set_page_config(page_title="Insurance App",page_icon="house_with_garden:")


st.title("Insurance App")


st.write("""
	###Fill in the details below
	""")



st.header("Age")
Age=st.slider('Select the age',0,100,30)

st.header("Salary")
Salary = st.number_input("Enter the salary earned in year(highest $50,000)",min_value=10,step=1000)


st.header("Country")
Country= st.selectbox("Select the contry where the person is located",("canada","nigeria" ,"usa"))


if Country== "canada":
	st.image("canada's flag.jpg",caption="canada",use_column_width=True)
	country_value =(1,0)


elif Country== "nigeria":
	st.image("Nigeria's flag.png",caption="nigeria",use_column_width=True)
	country_value =(0,1)


elif Country== "usa":
	st.image("america's flag.webp",caption="usa",use_column_width=True)
	country_value =(0,0)

input_data=np.array([[Age,Salary]+ list(country_value)]) 
if st.button("Predict Insurance Purchase"):
	cost=predict(input_data)
	st.subheader("Purchase Insurance")
	st.write(cost[0])
	if cost[0]==1:
		st.write("Purchase Insurance")
	else:
		st.write("iNSURANCE WAS NOT PURCHASED")
