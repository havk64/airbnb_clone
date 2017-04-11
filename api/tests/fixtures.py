"""Fixtures for unit tests
"""
fixt_users = [
    {'first_name':'Alexandro', 'last_name':'de Oliveira',
     'email':'alexandro.oliveira@holbertonschool.com',
     'password':'123', 'is_admin':True},
    {'first_name':'Tony', 'last_name':'Stark',
     'email':'tony@stark.com', 'password':'456',
     'is_admin': False},
    {'first_name':'Jon', 'last_name':'Snow',
     'email':'jon@snow.com', 'password':'789'}
]

fixt_bad_req = {'first_name': 'Jon', 'last_name': 'Snow',
                'password': '321', 'is_admin': False}
fixt_dupl_email = {'first_name': 'Cris','last_name': 'Lamarc',
              'email': 'alexandro.oliveira@holbertonschool.com',
              'password': '654', 'is_admin': True}
fixt_states = [
    {'name': 'California'}, {'name': 'New York'}, {'name': 'Florida'},
    {'name':  'Massachusetts'}, {'name': 'Hawaii'}, {'name': 'District of Columbia'}
]

fixt_cities = [{'name': 'San Francisco'}, {'name': 'Sacramento'}, {'name': 'Berkeley'}]

lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Mauris nisl'\
' ligula, dictum eget sem vitae, tincidunt laoreet nulla. Proin ut condimentum'\
' augue, a volutpat mi. Cras sit amet nisi bibendum, ullamcorper orci non,'\
' posuere sem. Integer lacinia porta sapien, a luctus risus commodo nec.'\
' Morbi nec luctus mi. Maecenas nec molestie sapien. Nam id leo a augue bibendum' \
' rutrum id ut justo. In sed urna fermentum, cursus libero non, tempor tortor.'

fixt_places = [
    {'name': 'Adelaide Hotel', 'owner': 1, 'city': 1, 'description': lorem,
     'number_rooms': 4, 'number_bathrooms': 2, 'max_guest': 4, 'price_by_night':
     60, 'latitude': 37.77, 'longitude': 122.41},
    {'name': 'HI Sacramento', 'owner': 2, 'city': 2, 'description': lorem,
     'number_rooms': 4, 'number_bathrooms': 2, 'max_guest': 4, 'price_by_night':
     60, 'latitude': 37.77, 'longitude': 122.41},
    {'name': 'Berkeley YMCA', 'owner': 3, 'city': 3, 'description': lorem,
     'number_rooms': 4, 'number_bathrooms': 2, 'max_guest': 4, 'price_by_night':
     50, 'latitude': 37.77, 'longitude': 122.41}
]

fixt_place_br = {'name': 'Adelaide Hotel', 'owner': 10, 'city': 10, 'description': lorem,
     'number_rooms': 4, 'number_bathrooms': 2, 'max_guest': 4, 'latitute': 37.77,
     'longitude': 122.41}

fixt_dupl_place = {'name': 'Adelaide Hotel', 'owner': 1, 'city': 1, 'description': lorem,
     'number_rooms': 4, 'number_bathrooms': 2, 'max_guest': 4, 'latitute': 37.77,
     'longitude': 122.41}
