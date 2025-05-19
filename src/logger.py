import csv
from datetime import datetime

class UsageLogger:
    def __init__(self, log_file='./data/usage_log.csv'):
        self.log_file = log_file
        self.fields = ['username', 'role', 'timestamp', 'action']

    def log(self, username, role, action):
        with open(self.log_file, 'a', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=self.fields)
            if f.tell() == 0:
                writer.writeheader()
            writer.writerow({
                'username': username,
                'role': role,
                'timestamp': datetime.now().isoformat(),
                'action': action
            })
