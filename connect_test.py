import psycopg2

# db_host = "127.0.0.1"
db_host = "localhost"
db_port = 5432
db_name = "etoro"
db_username = "postgres"
db_password = "123456"

connection = psycopg2.connect(
    host=db_host,
    port=db_port,
    dbname=db_name,
    user=db_username,
    password=db_password
)

print(connection.closed)  # 0

print("I am connected. Wow. Really?")

connection.close()

print(connection.closed)  # 1