# Streamlit Deployment Guide - Smart Scheme Predictor

You now have a Python-powered version of your app! Streamlit is excellent for data-heavy apps and is very easy to share.

## 1. Run Locally (Testing)

To see the app on your computer:
1.  Open your terminal or command prompt.
2.  Install Streamlit:
    ```bash
    pip install streamlit
    ```
3.  Navigate to your folder:
    ```bash
    cd c:\Users\LIB\Desktop\netaji
    ```
4.  Run the app:
    ```bash
    python -m streamlit run streamlit_app.py
    ```

## 2. Deploy to the Web (Streamlit Cloud)

Streamlit offers a free hosting service called **Streamlit Community Cloud**.

### Step A: Push to GitHub
Streamlit Cloud works by connecting to your GitHub account.
1.  Create a new repository on [GitHub](https://github.com).
2.  Upload the following files from your `netaji` folder:
    - `streamlit_app.py`
    - `engine.py`
    - `schemes_data.py`
    - `requirements.txt`

### Step B: Connect to Streamlit
1.  Go to [share.streamlit.io](https://share.streamlit.io).
2.  Log in with your GitHub account.
3.  Click **"New app"**.
4.  Select your repository and the main file `streamlit_app.py`.
5.  Click **"Deploy!"**.

Your app will be live at a URL like `https://smart-scheme-predictor.streamlit.app`.
