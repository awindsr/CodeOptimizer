import subprocess
import os

# Set environment variable for Streamlit to find the correct port
os.environ['PORT'] = os.getenv('PORT', '8888')

# Run Streamlit app
subprocess.run(['streamlit', 'run', 'app.py'])
