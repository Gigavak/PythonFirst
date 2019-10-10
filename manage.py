import os
import psycopg2

DATABASE_URL = os.environ['postgres://szemsvpgvnldkv:903a030fa35ce27e441187812839c4bff0a11ee9d65135fadaf5492fbbb2c68e@ec2-174-129-241-114.compute-1.amazonaws.com:5432/denuo82q39ehts']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')