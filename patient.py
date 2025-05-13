import csv
import uuid

class PatientDatabase:
    def __init__(self, filename='./data/Patient_data.csv'):
        self.filename = filename
        self.fields = ["Patient_ID", "Visit_ID", "Visit_time", "Visit_department",
                       "Gender", "Race", "Age", "Ethnicity", "Insurance", "Zip code",
                       "Chief complaint", "Note_ID", "Note_type"]

    def read_all(self):
        with open(self.filename, newline='') as f:
            return list(csv.DictReader(f))

    def write_all(self, data):
        with open(self.filename, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            writer.writeheader()
            writer.writerows(data)

    def add_patient(self, patient_info):
        patient_info['Visit_ID'] = str(uuid.uuid4())[:8]
        data = self.read_all()
        data.append(patient_info)
        self.write_all(data)

    def remove_patient(self, patient_id):
        data = self.read_all()
        filtered = [row for row in data if row['Patient_ID'] != patient_id]
        self.write_all(filtered)

    def retrieve_latest(self, patient_id):
        data = [row for row in self.read_all() if row['Patient_ID'] == patient_id]
        if not data:
            return None
        return max(data, key=lambda x: x['Visit_time'])

    def count_visits_by_date(self, date_str):
        return sum(1 for row in self.read_all() if row['Visit_time'] == date_str)
