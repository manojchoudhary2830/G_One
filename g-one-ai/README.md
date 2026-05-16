# G-ONE AI

## Ready To Launch

From the parent `g-one-ai-backend` folder, double-click:

- `launch_api.bat` to start the API server
- `launch_assistant.bat` to start the voice assistant

## Setup

```bash
python -m venv venv
```

### Activate

Windows:
```bash
venv\Scripts\activate
```

If you are using the existing virtual environment from the parent folder:
```bash
..\venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment

Rename `.env.example` to `.env`

Add your OpenAI API key.

### Run Assistant

```bash
python main.py
```

### Run API Server

From the parent `g-one-ai-backend` folder:
```bash
uvicorn api.server:app --reload
```

From this `g-one-ai` folder:
```bash
uvicorn api.server:app --reload
```
