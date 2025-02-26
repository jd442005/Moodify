# Moodify
# Moodify - AI-Powered Music Recommendation System

Moodify is an AI-driven web application that recommends music based on the user's facial expression detected from an uploaded image. It utilizes DeepFace for emotion analysis and the Spotify API to fetch relevant songs matching the detected mood.

## Features
- Upload an image and detect the dominant emotion.
- Get personalized song recommendations based on mood.
- View song details, including album covers and artist information.
- Simple, responsive UI built with HTML, CSS, and JavaScript.
- Flask-based backend for processing image analysis and fetching songs from the Spotify API.

## Project Structure
```
mood-music-recommender/
│── app.py                         # Main Flask application
│── requirements.txt                # Dependencies (Flask, OpenCV, DeepFace, etc.)
│── static/                         # Static assets (CSS, JS, images)
│   │── styles.css                  # Styling for the webpage
│   │── script.js                   # Handles frontend interactions
│   │── logo.png                    # Logo for the website
│── templates/                      # HTML templates
│   │── index.html                   # Main frontend page
│── uploads/                        # Stores user-uploaded images temporarily
│── models/                         # Contains model-related files
│   │── emotion_model.h5             # Pre-trained CNN model for emotion detection
│── utils/                          # Utility functions
│   │── mood_detection.py            # Handles image mood detection (DeepFace)
│   │── spotify_api.py               # Fetches song recommendations using Spotify API
│── config.py                        # Configurations (Spotify API keys, etc.)
│── README.md                        # Project documentation
│── .gitignore                       # Files to ignore in version control
```

## Installation & Setup
### Prerequisites
Ensure you have the following installed:
- Python 3.x
- Virtual Environment (optional but recommended)
- Flask
- DeepFace
- Spotify API credentials

### Steps to Run
1. **Clone the Repository**
   ```sh
   git clone https://github.com/your-username/moodify.git
   cd moodify
   ```
2. **Create a Virtual Environment (Optional but Recommended)**
   ```sh
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
4. **Set Up Configuration**
   - Update `config.py` with your Spotify API credentials:
   ```python
   SPOTIFY_API_URL = "https://api.spotify.com/v1"
   SPOTIFY_ACCESS_TOKEN = "your_access_token_here"
   ```
5. **Run the Application**
   ```sh
   python app.py
   ```
6. **Access the Web App**
   - Open `http://127.0.0.1:5000/` in your browser.

## Usage
1. Upload an image containing a human face.
2. The system detects the dominant emotion.
3. Based on the mood, the app fetches and displays recommended songs.

## Contribution
Feel free to fork the repository and contribute by submitting pull requests. Report issues and suggest improvements in the Issues section.

## License
This project is licensed under the MIT License.

## Contact
For inquiries or collaboration, reach out via kathalajaideep@gmail.com.

