import psycopg2

conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='127.0.0.1', port= '5432'
)

conn.autocommit = True

cursor = conn.cursor()

cursor.execute('''SELECT * from Company where company_id='3' ''')
result = cursor.fetchall();
print(result)
cursor.execute('''SELECT * from User_table where user_id='5' ''')


result1 = cursor.fetchall();
print(result1)

conn.commit()


conn.close()