# Clinical Data Warehouse UI

This application is a role-based clinical data warehouse system built in Python using Tkinter. It allows hospital staff to manage patient records, access notes, and view statistics based on their role permissions.

---

## 🔧 Features

- **Role-Based Login System**
- **Add, Retrieve, Remove Patients**
- **Count Visits by Specific Date**
- **View Clinical Notes**
- **Generate Statistics Reports**
- **Log Every User Action**

---

## 👥 Roles and Permissions

| Role        | Permissions                                                 |
|-------------|-------------------------------------------------------------|
| Admin       | Count visits only                                           |
| Nurse       | Add, retrieve, remove patients; count visits; view notes    |
| Clinician   | Retrieve patients; view notes                               |
| Management  | Generate patient statistics only                            |

---

## 📁 Folder Structure

```
myt/
├── main.py                 # Entry point to launch the app
├── README.md               # Project documentation
├── requirements.txt        # List of dependencies
├── UML_Diagram.png         # Visual representation of system architecture
├── data/                   # All CSV data files
│   ├── Credentials.csv     # Username, password, and role
│   ├── Notes.csv           # Clinical notes
│   ├── Patient_data.csv    # Patient visit records
│   └── usage_log.csv       # Logged user actions
└── src/                    # Source code
    ├── logger.py           # Logs user actions
    ├── notes.py            # Handles notes-related functions
    ├── patient.py          # Handles patient data
    ├── stats.py            # Generates reports/statistics
    ├── ui.py               # Tkinter-based GUI
    └── user.py             # User authentication and role management
```

---

## 🚀 How to Run

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python main.py
```

The GUI will launch. Log in using credentials from `data/Credentials.csv`.

---

## 🔐 Sample Credentials

| Username   | Password   | Role       |
|------------|------------|------------|
| admin1     | adminpass  | Admin      |
| nurse1     | nursepass  | Nurse      |
| doc1       | docpass    | Clinician  |
| mgr1       | mgrpass    | Management |

You can modify or add more users in the `data/Credentials.csv` file.

---

## 📊 UML Diagram

Refer to `UML_Diagram.png` for the full class-level architecture of the system.

---

## 📝 Logging

Every action taken by users is logged in `data/usage_log.csv`.

---
