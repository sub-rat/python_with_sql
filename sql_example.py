import sqlite3

# connection
sqlConn = sqlite3.connect("my_db.db")
print("Database connected")


cursor = sqlConn.cursor()
print("Database initialized")

# end

# user
# |  id  |  name   |  gender   |
# |  1   |   x     |    male   |  


# occupation
# |  id  |  name   | 
# |  1   |   E     |  
# |  2   |   O     |  


# create table
sql_create_table = """
    CREATE TABLE IF NOT EXISTS user(
        id INTEGER PRIMARY KEY,
        name varchar(100),
        gender char(1)
    );
"""

sqlConn.execute(sql_create_table)
print("Table Created")


# writing data to database table
# sql_command = """
#     INSERT INTO user VALUES(2,"Ram", "M");
# """
# cursor.execute(sql_command)

# sql_command = """
#     INSERT INTO user VALUES(3,"Sita", "F");
# """
# cursor.execute(sql_command)

# sqlConn.commit()


# Reading data from database
read_query =  """
    SELECT * FROM user WHERE gender='M' and name like '%m%';
"""

cursor.execute(read_query)
data = cursor.fetchall()
print(data)

