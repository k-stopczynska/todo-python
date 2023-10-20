from db.connect import get_connection

def get_all_todos(db_name, table_name):
	try:
		cursor, db_connection = get_connection(db_name)
		query = """SELECT * FROM {}""".format(table_name)
		cursor.execute(query)
		results = cursor.fetchall()
		cursor.close()
	except Exception as e:
		print(e)

	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")
	return results