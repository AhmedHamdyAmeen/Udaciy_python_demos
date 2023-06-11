import psycopg2

conn = psycopg2.connect("dbname=test user=postgres password=postgres")

cursor = conn.cursor()

# Open a cursor to perform database operations
cur = conn.cursor()

# drop any existing todos table
cur.execute("DROP TABLE IF EXISTS todos;")

# (re)create the todos table
# (note: triple quotes allow multiline text in python)
cur.execute("""
  CREATE TABLE todos (
    id serial PRIMARY KEY,
    description VARCHAR NOT NULL
  );
""")


# -------> Insert Into DB <----------

data = {'id': 3, 'description': "Allah with Me"}

# Plan String
sql = "INSERT INTO todos (id, description) VALUES (1, 'description Here')"
sql2 = "INSERT INTO todos (id, description) VALUES (%s, %s)"  # templet Literal
sql3 = "INSERT INTO todos (id, description) VALUES (%(id)s, %(description)s)"

cur.execute(sql)
# string interpolation to compose SQL query:
# 1: Using %s, passing in a tuple as the 2nd argument in cursor.execute()
cur.execute(sql2, (2, "Description 2!"))
# 2: Using named string parameters %(foo)s, passing in a dictionary instead.
cur.execute(sql3, data)


# -------> Fetching From DB <----------
sql = "SELECT * FROM todos;"

cur.execute(sql)
result = cur.fetchall()
result2 = cur.fetchone()
result3 = cur.fetchmany(2)


print(result)  # "FetchAll: "
print(result2)  # "FetchNone: "
print(result3)  # "FetchMany: "


# commit, so it does the executions on the db and persists in the db
conn.commit()

cur.close()
conn.close()
