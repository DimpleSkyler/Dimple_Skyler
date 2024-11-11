import os
from flask import Flask, render_template

app = Flask(__name__)

# Access the API key from the environment
api_key = os.environ.get('AIzaSyCBYSMVysDyU_L-EF9xDLpC4vXU-UoKiAg')

# Define path to the musics and videos directories
music_directory = os.path.join(app.root_path, 'static', 'musics')
video_directory = os.path.join(app.root_path, 'static', 'videos')

# Function to get all music tracks in the static/musics folder
def get_music_tracks():
    music_files = []
    for filename in os.listdir(music_directory):
        if filename.endswith('.mp3'):  # Filter for .mp3 files
            title = filename.split('.')[0]  # Use the filename without extension as title
            music_files.append({"title": title, "filename": filename})
    return music_files

# Function to get all video tracks in the static/videos folder
def get_video_tracks():
    video_files = []
    for filename in os.listdir(video_directory):
        if filename.endswith('.mp4'):  # Filter for .mp4 files
            title = filename.split('.')[0]  # Use the filename without extension as title
            video_files.append({"title": title, "filename": filename})
    return video_files

@app.route('/')
def home():
    return render_template('index.html', page='home', api_key=api_key)

@app.route('/music')
def music():
    # Get the list of music tracks dynamically
    music_tracks = get_music_tracks()
    return render_template('index.html', page='music', api_key=api_key, music_tracks=music_tracks)

@app.route('/tour')
def tour():
    return render_template('index.html', page='tour', api_key=api_key)

@app.route('/videos')
def videos():
    # Get the list of video tracks dynamically
    video_tracks = get_video_tracks()
    return render_template('index.html', page='videos', api_key=api_key, video_tracks=video_tracks)

# Run the app
if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
