import psycopg2

conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE Company (
     company_id INTEGER primary key,
    company_name VARCHAR(255),
    location VARCHAR(255)
)'''
cursor.execute(sql)
sql_command = """
INSERT INTO Company VALUES(01,"VALVO","Chennai")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO Company VALUES(02,"Mandis","Coimbatore")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO Company VALUES(03,"Bernad","Bangalore")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO Company VALUES(04,"Atlas","Hyderabad")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO Company VALUES(05,"Hp","Punjab")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO Company VALUES(06,"Adidas","Delhi")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO Company VALUES(07,"Rebook","Uttar Pradesh")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO Company VALUES(08,"KFC","Tamilnadu")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO Company VALUES(09,"Bag company","Kerala")
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO Company VALUES(10,"Mobile company","Odissa")
"""
cursor.execute(sql_command)


result = cursor.fetchall();
print(result)



conn.commit()

conn.close()
