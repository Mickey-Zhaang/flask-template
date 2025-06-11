# Flask Template Project

## Author: Mickey Zhang

### Purpose

This project serves as a Flask template designed and summarized from entrepreneurial software engineering course sequence (CS321-422) at Colby College.
Thank you Prof. Al Madi for letting me into your sequence!

## Initial Setup

1. **Fork the Repository** to make it your own!

   - After forking, clone and open the project in your preferred code editor.

2. **Secure Environment Variables**

   - I did something really silly and pushed my .env file into the public... NEVER DO THIS! You don't want random people viewing your secrets
   - This is to demonstrate an important lesson to learn immediately as well as helping you understand that there are many nuiances of building web applications. Now fix my mistake!
   - Locate `.gitignore` and add `.env` to the file to ensure sensitive data (e.g., API keys, secret keys) is not exposed on GitHub.
   - Finally run in your terminal
     ```bash
     git rm --cached .env
     ```
     In the case you ever accidently push any sensitive information, this removes the reference from Git's history.

3. **Setting Up Virtual Environment**

   - Create a virtual environment and name it `venv` (could be anything):
     ```bash
     python -m venv venv
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       source venv/Scripts/activate
       ```
     - On macOS/Linux:
       ```bash
       source venv\bin\activate
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
   python tests/run_tests.py
   ```

## Next Steps

1. Start **hosting your website** on a cloud hosting service like [Heroku](https://www.heroku.com/):
   - Your Procfile is already set up!
2. Start building things!
   - Q&A Bot with OpenAI API
   - Weather App
   - etc...
