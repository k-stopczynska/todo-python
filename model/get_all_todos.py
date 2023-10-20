from db.connect import get_connection
from db.utils import map_tuple_to_dict

def get_all_todos(db_name, table_name):
	try:
		cursor, db_connection = get_connection(db_name)
		query = """SELECT * FROM {}""".format(table_name)
		cursor.execute(query)
		results = cursor.fetchall()
		todos = map_tuple_to_dict(results)
		cursor.close()
	except Exception as e:
		print(e)

	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")
	return todos