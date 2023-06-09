import pandas as pd
import numpy as np



class Mapping:
    # Lire le fichier Excel
    df = pd.read_excel('mapping.xlsx')

    def __init__(self, df):
        self.df = df
    
    def mapping_otobo_to_jira(self, df):
        # Accéder aux données dans le fichier Excel
        new_jira = np.array([])
        for index, row in df.iterrows():
            otobo_field = row['source Field']  # Nom du champ Otobo
            jira_field = row['direction Field']    # Nom du champ Jira

            jira_field = otobo_field
            new_jira = np.append(new_jira, jira_field)

        return new_jira.json()

    def mapping_jira_to_otobo(self, df):
        # Accéder aux données dans le fichier Excel
        new_otobo = np.array([])
        for index, row in df.iterrows():
            otobo_field = row['source Field']  # Nom du champ Otobo
            jira_field = row['direction Field']    # Nom du champ Jira

            otobo_field = jira_field
            new_otobo = np.append(new_otobo, otobo_field)

        return new_otobo.json()