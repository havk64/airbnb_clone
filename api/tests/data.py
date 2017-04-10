"""Data collection for tests
"""
users = [
    {'first_name':'Alexandro', 'last_name':'de Oliveira',
     'email':'alexandro.oliveira@holbertonschool.com',
     'password':'123', 'is_admin':True},
    {'first_name':'Tony', 'last_name':'Stark',
     'email':'tony@stark.com', 'password':'456',
     'is_admin': False},
    {'first_name':'Jon', 'last_name':'Snow',
     'email':'jon@snow.com', 'password':'789'}
]

user_bad_req = {'first_name': 'Jon', 'last_name': 'Snow',
                'password': '321', 'is_admin': False}
dupl_email = {'first_name': 'Cris','last_name': 'Lamarc',
              'email': 'alexandro.oliveira@holbertonschool.com',
              'password': '654', 'is_admin': True}
states = [
    {}
]
