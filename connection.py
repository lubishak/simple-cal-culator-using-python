import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="Order_db",
    user="postgres",
    password="lindadahiru01",
    port=5432
    )





query ="CREATE TABLE Order (user_id, username, password, email, created_on, last_login) VALUES (1, 'lubishak', 'johndoe', 'g@gmail.com', '2021-06-10 00:00:00', '2021-06-10 00:00:00')"






CREATE DATABASE Order_db
res.execute(Order_db)
conn.commit()
conn.close()        
                
curr = conn.cursor()
response = curr.execute(query)
user = f"""INSERT INTO test1_db (3, ishaku) VALUES ({[0]},'{[1]}'); """
load_data_into_table(user)
res =curr.fetchall()
print(res)
res =conn.commit()
conn.close()
count = curr.rowcount

