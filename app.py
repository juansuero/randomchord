import requests
from bs4 import BeautifulSoup
import random
import streamlit as st
import webbrowser

def get_random_chord():
    url = "https://www.all-guitar-chords.com/chords/index"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    chords = soup.find_all('a', href=True)
    chord_links = [link['href'] for link in chords if 'chord' in link['href']]
    return random.choice(chord_links)

st.title("Random Guitar Chord Picker")

if st.button("Pick a Random Chord"):
    chord_link = get_random_chord()
    st.markdown(f"[Click here to see the chord]({chord_link})")
