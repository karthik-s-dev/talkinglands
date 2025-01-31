from dotenv import dotenv_values
config = {**dotenv_values(".env")}

try:
    db_url = config['DATABASE_URL']
    db_name = config['DATABASE_NAME']
except KeyError:
    print("Please check the '.env' file.")
    exit(1)


from mongoengine import connect
connect(host = db_url)