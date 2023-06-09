import requests

class OtoboConnector:

    base_url = "https://fgdc-ux.imfr.cgi.com/"

    def __init__(self, username, password):
        self.base_url = "https://fgdc-ux.imfr.cgi.com/"
        self.username = username
        self.password = password
        self.session = requests.Session()

    def login(self):
        login_url = self.base_url + '/otrs/public.pl?Action=Login'
        login_data = {
            'User': self.username,
            'Password': self.password,
        }
        response = self.session.post(login_url, data=login_data)
        if response.status_code == 200:
            print("Logged in successfully.")
        else:
            print("Login failed.")

    def create_ticket(self, subject, message):
        create_ticket_url = self.base_url + '/otobo/nph-genericinterface.pl/Webservice/testCreationTicket/Ticket'
        print(create_ticket_url)
        ticket_data = {
            'Queue':'Raw',
            'Subject': subject,
            'Body': message,
        }
        response = self.session.post(create_ticket_url, data=ticket_data)
        if response.status_code == 200:
            print("Ticket created successfully.")
        else:
            print("Failed to create ticket.")

    def logout(self):
        logout_url = self.base_url + '/otobo/public.pl?Action=Logout'
        response = self.session.get(logout_url)
        if response.status_code == 200:
            print("Logged out successfully.")
        else:
            print("Logout failed.")
