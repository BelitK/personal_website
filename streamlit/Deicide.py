import streamlit as st
import pandas as pd
import json
import requests

st.title("Chain test !&!")

st.write("Insert data to chain")
username = st.text_input("Username")
data = st.text_input("Data to input")
workTime = round(st.number_input("Worked time"), 2)
choice = st.selectbox("run types", ["success", "failure", "canceled"])
clicked = st.button("send to chain")

if clicked:
    r = requests.get(
        f"http://api:1000/mine_block/{data}/{username}/{workTime}/{choice}"
    )
    st.json(json.loads(r.content))

"------------------------------"
"gonna add pending blocks for multi-worker type things"
# mine = st.button("click to mine")
# if mine:
#        r=requests.get(f"http://api:1000/mine_block")
#        st.json(json.loads(r.text))
"--------------------------------------------------------------"

st.write("Get chain and show")
get_chain = st.button("Get chain")
chain = []
if get_chain:
    chain = requests.get(f"http://api:1000/get_chain")
    st.json(json.loads(chain.content))

"--------------------------------------------------------------"

st.write("Find data with user")
usern = st.text_input("user to find")
find = st.button("click to find")

with st.spinner("Waitt"):
    if find:
        r = requests.get(f"http://api:1000/find_user/{usern}")
        st.json(json.loads(r.content))

"---------------------------------------------------"

st.write("find data with run type")

choice2 = st.selectbox("run types2", ["success", "failure", "canceled"])
find2 = st.button("click to find with type")

if find2:
    r = requests.get(f"http://api:1000/find_type/{choice2}")
    st.json(json.loads(r.content))

"------------------------------"

valid = st.button("click to validate chain")
if valid:
    r = requests.get(f"http://api:1000/validate")
    st.write(r.text)
"---------------------------------------"
st.write("Download chain")

chain2 = requests.get(f"http://api:1000/get_chain")


st.download_button(
    label="Download data as CSV",
    data=json.loads(chain2.content),
    file_name="chain.json",
    mime="text/json",
)
