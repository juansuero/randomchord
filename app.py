import requests
from bs4 import BeautifulSoup
import random
import streamlit as st

def get_random_chord():
    try:
        base_url = "https://www.all-guitar-chords.com"
        index_url = f"{base_url}/chords/index"

        response = requests.get(index_url)
        response.raise_for_status()

        soup = BeautifulSoup(response.content, 'html.parser')
        chords = soup.find_all('a', href=True)
        chord_links = [link['href'] for link in chords if 'chord' in link['href']]

        random_chord_link = random.choice(chord_links)
        full_url = random_chord_link  # Removed base_url here as per user correction

        chord_page = requests.get(full_url)
        chord_page.raise_for_status()

        chord_soup = BeautifulSoup(chord_page.content, 'html.parser')

        chord_name = chord_soup.find('h1').get_text(strip=True)

        img_tag = chord_soup.find('img', {'src': True})
        img_url = f"{base_url}{img_tag['src']}" if img_tag else None

        return chord_name, img_url, full_url

    except requests.exceptions.RequestException as e:
        st.error(f"Error fetching data: {e}")
        return None, None, None

st.title("Random Guitar Chord Picker")

if st.button("Pick a Random Chord"):
    chord_name, img_url, chord_link = get_random_chord()
    if chord_name and img_url:
        st.subheader(chord_name)
        st.image(img_url, caption=chord_name)
        st.markdown(f"[View all variations on the website]({chord_link})")
    else:
        st.error("Could not fetch a chord at this time.")

