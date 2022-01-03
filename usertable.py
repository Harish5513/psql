import psycopg2

conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()

sql = '''CREATE TABLE User_table (
    user_id INTEGER,
    user_name VARCHAR(255),
    company_id INTEGER references Company(company_id),
    joining_date date,
    primary key(user_id),
)'''
cursor.execute(sql)
sql_command = """
INSERT INTO User_table(user_id,user_name,company_id,joining_date) VALUES(01,'Ajay',1,'2018-02-01')
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO User_table(user_id,user_name,company_id,joining_date) VALUES(02,'Balu',2,'2017-03-03')
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO User_table(user_id,user_name,company_id,joining_date) VALUES(03,'Chitra',3,'2019-05-15')
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO User_table(user_id,user_name,company_id,joining_date) VALUES(04,'Guna',4,'2020-04-03')
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO User_table(user_id,user_name,company_id,joining_date) VALUES(05,'Naveen',5,'2021-05-10')
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO User_table(user_id,user_name,company_id,joining_date) VALUES(06,'Mano',6,'2017-08-02')
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO User_table(user_id,user_name,company_id,joining_date) VALUES(07,'Laila',7,'2019-04-02')
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO User_table(user_id,user_name,company_id,joining_date) VALUES(08,'Manish',8,'2018-06-15')
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO User_table(user_id,user_name,company_id,joining_date) VALUES(09,'Arul',9,'2019-07-02')
"""
cursor.execute(sql_command)

sql_command = """
INSERT INTO User_table(user_id,user_name,company_id,joining_date) VALUES(10,'Priya',10,'2020-02-01')
"""
cursor.execute(sql_command)


result = cursor.fetchall();
print(result)



conn.commit()

conn.close()






