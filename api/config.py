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
    switch = {
        'production'    : {
            'debug'     : False,
            'host'      : '0.0.0.0',
            'port'      : 3000,
            'user'      : 'airbnb_user_prod',
            'db'        : 'airbnb_prod',
            'password'  : ENV.get('AIRBNB_DATABASE_PWD_PROD')
        },
        'development'   : {
            'debug'     : True,
            'host'      : 'localhost',
            'port'      : 3333,
            'user'      : 'airbnb_user_dev',
            'db'        : 'airbnb_dev',
            'password'  : ENV.get('AIRBNB_DATABASE_PWD_DEV')
        },
        'test'          : {
            'debug'     : False,
            'host'      : 'localhost',
            'port'      : 5555,
            'user'      : 'airbnb_user_test',
            'db'        : 'airbnb_test',
            'password'  : ENV.get('AIRBNB_DATABASE_PWD_TEST')
        }
    }
    return switch.get(env)

options = setenv(ENV['AIRBNB_ENV'])

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
