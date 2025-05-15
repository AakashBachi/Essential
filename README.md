
# Hospital Patient Management System

This is a hospital data management system built using Python. It provides functionality for user authentication, patient record management, visit tracking, and note-taking. The project has been flattened to remove the 'src' folder for simplicity.

## Project Structure

```
Aak/
├── data/                     # CSV data files
│   ├── Patient_data.csv
│   ├── Notes.csv
│   ├── Credentials.csv
│   └── usage_log.csv
│
├── user.py                   # user management
├── ui.py                     # GUI / interface
├── patient.py                # patient management
├── notes.py                  # notes management
├── stats.py                  # statistics & reports
├── logger.py                 # logging functions
│
├── UML.pdf                   # UML diagram of the system
├── main.py                   # Main entry point for the program
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Features

- User login system (Admin, Nurse, Clinician)
- Add, retrieve, and remove patient records
- View patient notes by date
- Count patient visits by date
- Simple usage logging (`usage_log.csv`)

##  Requirements

- Python 3.8+
- Packages listed in `requirements.txt`

##  Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Aak.git
cd Aak
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate     # macOS/Linux
venv\Scripts\activate      # Windows
```

3. Install required dependencies:
```bash
pip install -r requirements.txt
```

##  How to Run

1. Make sure your `data/` folder contains:
   - `Patient_data.csv`
   - `Notes.csv`
   - `Credentials.csv`
   - `usage_log.csv`

2. Run the main program:
```bash
python main.py
```

3. Follow on-screen prompts for login and available actions.

##  User Roles

| Role | Capabilities |
|------|--------------|
| Admin | View logs, manage patients |
| Nurse | Add, retrieve, remove patients, view patient notes |
| Clinician | View patient notes, count visits |

##  UML Diagram

See `UML.pdf` for the full class structure and relationships.
