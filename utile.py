import requests
from requests.auth import HTTPBasicAuth
import json
import os
import getpass
from jiracon import Jiraconn
from otobocon import OtoboConnector

# Clé du projet Jira
# project_id = Jiraconn.project_key
# Initialisation de l'instance jira
# jira = Jiraconn.jira_connexion(Jiraconn)
# Listes de ticket à utiliser
# list = Jiraconn.list_de_tickets(jira, project_id)
#jql = Jiraconn.jql
username = "jean-paul.andrei"
password = "Balma003!!"

connector = OtoboConnector(username, password)
# Connexion à otobo
otobo = connector.login()

# # Création d'un ticket dans otobo
# connector.create_ticket(otobo, ticket_title, ticket_body)

# # Déconnexion à otobo
# connector.logout()

# # Différentes méthode d'intégration dans jira , list
# Jiraconn.get_one_ticket(jira, list)
# Jiraconn.create_issue(jira, project_id)
# Jiraconn.update_number1_ticket(jira, list)

# Jiraconn.add_new_comment(jira, "FGDCASOPSU-4129")