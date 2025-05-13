import pandas as pd
import matplotlib.pyplot as plt

class StatsGenerator:
    def __init__(self, data_file='./data/Patient_data.csv'):
        self.data_file = data_file

    def generate(self):
        df = pd.read_csv(self.data_file)
        df['Age'].hist()
        plt.title('Patient Age Distribution')
        plt.xlabel('Age')
        plt.ylabel('Count')
        plt.tight_layout()
        plt.savefig('./data/age_distribution.png')
        plt.close()
