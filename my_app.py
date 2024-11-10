import os
from flask import Flask, render_template

app = Flask(__name__)

# Access the API key from the environment
api_key = os.environ.get('AIzaSyCBYSMVysDyU_L-EF9xDLpC4vXU-UoKiAg')

@app.route('/')
def home():
    return render_template('index.html', page='home', api_key=api_key)

@app.route('/music')
def music():
    return render_template('index.html', page='music', api_key=api_key)

@app.route('/tour')
def tour():
    return render_template('index.html', page='tour', api_key=api_key)

@app.route('/videos')
def videos():
    return render_template('index.html', page='videos', api_key=api_key)

# Run the app
if __name__ == '__main__':
    # Use the PORT environment variable or default to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
