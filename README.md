# Flask Template Project

## Author: Mickey Zhang

### Purpose
This project serves as a Flask template designed for entrepreneurial software engineering course (CS321-422) at Colby College .

## Initial Setup

1. **Clone the Repository**
   After cloning or downloading the zip file, open the project in your preferred code editor.

2. **Secure Environment Variables**
   - I did something really silly and pushed my .env file into the public... NEVER DO THIS! You don't want random people viewing your secrets
   - This is to demonstrate an important lesson to learn immediately as well as helping you understand that there are many nuiances of building web applications. Now fix my mistake!
   - Locate `.gitignore` and add `.env` to the environments section to ensure sensitive data (e.g., API keys, secret keys) is not exposed on GitHub.

3. **Setting Up Virtual Environment**
   - Create a virtual environment named `venv`:
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       source venv\Scripts\activate
       ```
     - On macOS/Linux:
       ```bash
       source venv/bin/activate
       ```
   - You should see `(venv)` above your terminal prompt.

4. **Install Dependencies**
   Run the following command to install dependencies listed in `requirements.txt`:
   ```bash
   pip install -r requirements.txt
   ```
5. **Explore Around the Application**
   Test out the app using:
   ```bash
   python app.py
   ```
   Or run some tests:
   ```bash
   ppython tests/run_tests.py
   ```
