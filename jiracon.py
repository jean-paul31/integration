from jira import JIRA
from auth import auth
import os
    

class Jiraconn:

    """
    Cette classe gére l'instanciation de JIRA avec mon compte perso
    Il gére également les différentes instances sur JIRA


    """

    email = auth['JIRA_USERNAME']#input("Rentrer votre adresse mail : ")
    mdp = auth['JIRA_PASSWORD'] #getpass.getpass("Rentrer votre mot de passe : ")
    server = auth['JIRA_HOST']#input("Rentrer ici votre server fr/eu/ca/poc : ")
    project_key = "EUCRMTPAM"#input("Rentrer ici votre project key : ")
    # jql2 = input("Rentrer votre requête JQL : ")
    # jql = jql2.replace('"', '\\"')

    server1 = "https://proactionfr.ent.cgi.com/jira"
    server2 = "https://proactioneu.ent.cgi.com/jira"
    server3 = "https://proactionca.ent.cgi.com/jira"
    server4 = "https://proactioncapoc.ent.cgi.com/jira"

    if server == 'fr':
        server = server1
    elif server == 'eu':
        server = server2
    elif server == 'ca':
        server = server3
    elif server == 'poc':
        server = server4

    def __init__(self, email, mdp, server):
        """
            Initialise l'instance Jira
        ========================================================
            :param email: Email de connexion à jira
            :param mdp: Mot de passe de connexion à JIRA
            :param server: nom du serveur de l'instance JIRA
        """
        self.email = email 
        self.mdp = mdp
        self.server = server

    def jira_connexion(self):
        """
            Ce connecte à l'instance
        ==============================================
            :param: Utilise les variables de la classe

        """  
        options = {"server": self.server}
        jira = JIRA(options, basic_auth=(self.email, self.mdp))
        return jira

    def list_de_tickets(connect, key):
        """
            Récupére une liste de ticket en fonction d'une requete JQL prédéfinie
        =============================================================================
            :param connect: Instance de jira
            :param key: Clé du projet jira
        """
        # Récupération des tickets du projet
        issues = connect.search_issues(f"project = {key} AND issuetype = Enhancement AND \"External Ticket ID\" ~ \"DTSK*\" AND \"Number 1\" != 0", maxResults=False, fields="summary")#f"project={key} AND Effort is not EMPTY and \"Number 1\" is not EMPTY"
        # issues = connect.search_issues(jql)
        return issues

    def get_one_ticket(connect, keys):
        """
            Récupére le détaille de chaque tickets de la liste récupéré dans la méthode 'list_de_tickets'
        =================================================================================================
            :param connect: Instance de Jira
            :param Keys: Liste des tickets Jira
        """
        for key in keys:
            issue1 = connect.issue(key.key)
            print("key: " + issue1.key)
            print("Titre: " + issue1.fields.summary)
            if issue1.fields.description is None:
                print("description is empty")
            else:
                print("Description: " + issue1.fields.description)
            print("État: " + issue1.fields.status.name)
            print("Priorité: " + issue1.fields.priority.name)
            print("Type de ticket: " + issue1.fields.issuetype.name)        
            print("\n")
            print("|--------|TICKETS SUIVANT|-------|\n")
            print("\n")
            #return issue1
 
    def get_All_comments(connect, keys):
        """
            Récupére tous les commentaires de chaques tickets récupérés dans la méthode 'list_de_tickets'
        =================================================================================================
            :param connect: Instance de Jira
            :param Keys: Liste des tickets Jira
        """ 
        for key in keys:
            print(key.key)
            comments = connect.comments(key.key)
            for comment in comments:
                if comment.author is None: 
                    continue
                else:
                    print("\tAuthor : " + comment.author.name)
                if comment.created is None:
                    continue
                else:
                    print("\tCreated : " + comment.created)
                if comment.body is None:
                    continue
                else:
                    print("\tContent : " + comment.body)
            
            print("\n")

            print("|--------|TICKETS SUIVANT|-------|\n")

    def create_issue(connect, key):
        """
            Crée un ticket dans l'instance et le projet définit
        =============================================================================
            :param connect: Instance de jira
            :param key: Clé du projet jira
        """
        # Définition des champs du ticket
        issue_dict = {
            'project': {'key': key},
            'summary': 'titre du ticket en python',
            'description': 'description du ticket',
            'issuetype': {'name': 'Incident'},
        }

        # Création du ticket
        new_issue = connect.create_issue(fields=issue_dict)

        print("Le ticket est créé \n")

        # Ajout d'un commentaire
        connect.add_comment(new_issue, 'This is a comment.')

        print("Le commentaire est ajouté \n")

        # Ajout d'une pièce jointe
        # connect.add_attachment(new_issue, '/path/to/attachment')
    
    def add_new_comment(connect, key):
        connect.add_comment(key, 'Nouveau test', is_internal=True )
        print("peu etre que ca marche")

    def update_one_ticket(connect, key):
        """
            Update le le champs "effort" de un seul ticket
        =============================================================================
            :param connect: Instance de jira
            :param key: Issue key
        """
        # Récupérer le ticket à mettre à jour
        #ticket_id = 'FGDCASOPSU-4130'
        issue = connect.issue(key)
        new_value = issue.fields.customfield_10115 * 8.0
        issue.fields.customfield_10115 = new_value

        # Modifier le statut du ticket
        # transition_id = 11  # ID de la transition de statut à appliquer
        # connect.transition_issue(issue, transition_id)

        # Enregistrer les modifications
        issue.update(fields={"customfield_10115": new_value})

        print('La valeur du champ a été modifiée avec succès.')

    def update_transition_ticket(connect, key, idT):
        """
            Effectue la transition du ticket ciblé
        =============================================================================
            :param connect: Instance de jira
            :param key: Issue key
            :param idT: Id de la transition souhaité
        """
        # Récupérer le ticket à mettre à jour
        issue = connect.issue(key)
 
        # Modifier le statut du ticket
        transition_id = idT  # ID de la transition de statut à appliquer
        connect.transition_issue(issue, transition_id)

        # Enregistrer les modifications
        issue.update()

        print('La valeur du champ a été modifiée avec succès.')

    def update_number1_ticket(connect, keys):
        """
            Update le "number 1" de tous les tickets de la méthode list_de_tickets
        ===============================================================================================
            :param connect: Instance de jira
            :param keys: Liste d'Issue key
        """
        # Récupérer le ticket à mettre à jour
        #ticket_id = 'FGDCASOPSU-4130'
        for key in keys:
            issue = connect.issue(key.key)
            number_1 = issue.fields.customfield_11803 * 8.0
            issue.fields.customfield_11803 = number_1
            
            # Enregistrer les modifications
            issue.update(fields={"customfield_11803": number_1})

            print('La valeur du champ a été modifiée avec succès. ' + key.key)

    def update_effort_ticket(connect, keys):
        """
            Update les champs "effort" et "number 1" de tous les tickets de la méthode list_de_tickets
        ===============================================================================================
            :param connect: Instance de jira
            :param keys: Liste d'Issue key
        """
        # Récupérer le ticket à mettre à jour
        #ticket_id = 'FGDCASOPSU-4130'
        for key in keys:
            issue = connect.issue(key.key)
            effort = issue.fields.customfield_10224 * 8.0
            issue.fields.customfield_10224 = effort
            
            # Enregistrer les modifications
            issue.update(fields={"customfield_10224": effort})

            print('La valeur du champ a été modifiée avec succès. ' + key.key)