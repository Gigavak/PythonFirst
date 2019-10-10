import dj_database_url
import psycopg2

DATABASELINK = "postgres://szemsvpgvnldkv:903a030fa35ce27e441187812839c4bff0a11ee9d65135fadaf5492fbbb2c68e@ec2-174-129-241-114.compute-1.amazonaws.com:5432/denuo82q39ehts"


db_info = dj_database_url.config(default=DATABASELINK)
connection = psycopg2.connect(database=db_info.get('denuo82q39ehts'),
		    		user=db_info.get('szemsvpgvnldkv'),
		    		password=db_info.get('903a030fa35ce27e441187812839c4bff0a11ee9d65135fadaf5492fbbb2c68e'),
		    		host=db_info.get('ec2-174-129-241-114.compute-1.amazonaws.com'),
		    		port=db_info.get('5432'))
cursor = connection.cursor()