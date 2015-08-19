
PROD = False

if PROD:
    # production
    BASE_STATIC_URL = '/'

else:
    # local development
    BASE_STATIC_URL = 'http://localhost:8888/'

