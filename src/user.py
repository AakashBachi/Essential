import csv

class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

class Authenticator:
    def __init__(self, credentials_file='./data/Credentials.csv'):
        self.credentials_file = credentials_file

    def authenticate(self, username, password):
        with open(self.credentials_file, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['username'] == username and row['password'] == password:
                    return User(username, row['role'])
        return None
