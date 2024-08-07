<h1 align="center" id="title">Code Optimizer</h1>

<p align="center"><img src="https://socialify.git.ci/awindsr/CodeOptimizer/image?language=1&amp;name=1&amp;owner=1&amp;stargazers=1&amp;theme=Auto" alt="project-image"></p>

<p id="description">The Code Optimizer app helps developers enhance their code by providing recommendations for improving efficiency readability and adherence to best practices. It uses the Gemini model for analysis and converts feedback into a structured JSON format with Pathway.</p>

<h2>🚀 Demo</h2>

[https://codeoptimizr.streamlit.app/](https://codeoptimizr.streamlit.app/)

<h2>Project Screenshots:</h2>

<img src="https://i.postimg.cc/SQ9sB98R/Screenshot-2024-08-07-182927.png" alt="project-screenshot" width="1980" height="1080/">

  
  
<h2>🧐 Features</h2>

Here're some of the project's best features:

*   Pathway Integration: Utilizes Pathway to handle JSON conversion and save recommendations in a JSON Lines format.
*   JSON Feedback: Converts feedback into a structured JSON format for easy understanding and application.
*   Gemini Model Integration: Uses the Gemini model to analyze and provide feedback on code.
*   Code Analysis: Provides detailed recommendations to improve code efficiency and readability.

## Getting Started

To get started with the Code Optimizer app, follow these steps:

### Prerequisites

- Python 3.7 or higher
- `pip` for package management
- `.env` file with your Google API key

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/awindsr/CodeOptimizer.git
   cd CodeOptimizer

   ```
2. Install the required packages:
    ```
      pip install -r requirements.txt
    ```
3. Set up environment variables:
   ```
      GOOGLE_API_KEY=your_google_api_key_here
    ```
4. Run the app:
    ```
      streamlit run app.py
    ```

