import psycopg2
import sys
import pprint

def main():
	#Define our connection string
	conn_string = "host='localhost' dbname='test' user='michaelboegner' password=''"

	# print the connection string we will use to connect
	print("Connecting to database\n	->%s %", conn_string)

	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)

	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print("Connected!\n")
	cursor.execute("INSERT INTO weather VALUES ('San Francisco', 46, 50, 0.25, '1994-11-27');")
	cursor.execute("SELECT * FROM weather")

	records = cursor.fetchall()
	pprint.pprint(records)

if __name__ == "__main__":
	main()