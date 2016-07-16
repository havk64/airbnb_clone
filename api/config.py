"""
 ===----Config------------------------------------------------------------------------===
	Airbnb Clone Project, config file.
	Isolating environments in Python: Development/Production/Test.
 ===----------------------------------------------------------------------------------===
"""
from os import environ

ENV = environ
if 'AIRBNB_ENV' not in ENV:
    raise Exception("Environment variable AIRBNB_ENV not set\n"
                    "Expected to be 'development', 'production', or 'test'")

def setenv(env):
    options = {}
    if env['AIRBNB_ENV'] == 'production':
        options['debug']    = False
        options['host']     = '0.0.0.0'
        options['port']     = 3000
        options['user']     = 'airbnb_user_prod'
        options['db']       = 'airbnb_prod'
        options['password'] = ENV.get('AIRBNB_DATABASE_PWD_PROD')
    elif env['AIRBNB_ENV'] == 'development':
        options['debug']    = True
        options['host']     = 'localhost'
        options['port']     = 3333
        options['user']     = 'airbnb_user_dev'
        options['db']       = 'airbnb_dev'
        options['password'] = ENV.get('AIRBNB_DATABASE_PWD_DEV')
    else:
        options['debug']    = False
        options['host']     = 'localhost'
        options['port']     = 5555
        options['user']     = 'airbnb_user_test'
        options['db']       = 'airbnb_test'
        options['password'] = ENV.get('AIRBNB_DATABASE_PWD_TEST')

    return options


options = setenv(ENV)

DEBUG   = options['debug']
HOST    = options['host']
PORT    = options['port']
DATABASE = {
    'host': '158.69.78.253',
    'user': options['user'],
    'database': options['db'],
    'port': 3306,
    'charset': 'utf8',
    'password': options['password']
}

# Testing the environment:
# print(DEBUG, HOST, PORT)
# print(DATABASE)
