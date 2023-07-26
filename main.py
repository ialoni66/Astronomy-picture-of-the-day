import requests
import streamlit as st

API_KEY = 'QXQnR1wbwRIaG4jEjmOCUZQ6dZmea2VHQOadM0ZT'
url = 'https://api.nasa.gov/planetary/apod?api_key=QXQnR1wbwRIaG4jEjmOCUZQ6dZmea2VHQOadM0ZT'

# GET general API
request = requests.get(url)
APOD = request.json()

# GET image
hdurl = APOD['hdurl']
POD = requests.get(hdurl)
with open("image.jpg", "wb") as file:
    file.write(POD.content)

# product on Streamlit
st.title(APOD["title"])
st.image("image.jpg")
st.write(APOD["explanation"])




