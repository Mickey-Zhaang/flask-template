# Flask Template Project

## Author: Mickey Zhang

### Purpose

This project serves as a Flask template designed and summarized from entrepreneurial software engineering course sequence (CS321-422) at Colby College.
Thank you Prof. Al Madi for letting me into your sequence!

## Quick Start

### 1. Fork and Clone

```bash
# After forking, clone the repository locally
git clone <your-repo-url>
cd flask-template

# Setup virtual environment (venv)
python -m venv venv

source venv/Scripts/activate # Windows
# or
source venv/bin/activate # Mac
```

### 2. Environment Configuration

```bash
# Create environment file (or just manually rename .env.example to .env by right clicking)
cp .env.example .env

# ^^ very important, if you check .gitignore... Git will ignore any files specified
# Essentially anything you don't want the public seeing i.e. your OpenAI API key
```

### 3. Install Dependencies

```bash
# Install all dependencies
pip install -r requirements.txt
```

### 4. Run the Application

```bash
# Development server
python app.py

# Or with Flask CLI
flask run
```

Visit `http://localhost:5000` to see your app!

## Testing

```bash
# Run all tests
python test/run_tests.py

# Run linter
python test/run_lint.py

```
