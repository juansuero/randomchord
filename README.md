# Random Guitar Chord Picker

This is a simple Streamlit application that picks a random guitar chord from the website [All Guitar Chords](https://www.all-guitar-chords.com) and displays the chord name, diagram, and a link to view all variations on the website.

## Description

The application fetches a list of guitar chords from the All Guitar Chords website and randomly selects one. When the user clicks the "Pick a Random Chord" button, the chord name, diagram, and a link to view all variations are displayed.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/random-guitar-chord-picker.git
    cd random-guitar-chord-picker
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the Streamlit application:
    ```bash
    streamlit run chord_picker.py
    ```

2. Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

3. Click the "Pick a Random Chord" button to display a random guitar chord with its name, diagram, and link.

## Requirements

- Python 3.7+
- `requests`
- `beautifulsoup4`
- `streamlit`

## Files

- `chord_picker.py`: The main application script.
- `requirements.txt`: The list of dependencies.

## License

This project is licensed under the MIT License.
