import psycopg2
conn = psycopg2.connect(dbname='denuo82q39ehts', user='szemsvpgvnldkv',
                        password='903a030fa35ce27e441187812839c4bff0a11ee9d65135fadaf5492fbbb2c68e', host='ec2-174-129-241-114.compute-1.amazonaws.com')
cursor = conn.cursor()

cursor.execute("""insert into users (name, id) values ('sssddas', 22) """)
records = cursor.fetchall()
cursor.close()
conn.close()





