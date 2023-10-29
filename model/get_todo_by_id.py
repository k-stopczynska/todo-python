from db.connect import get_connection
from db.utils import map_tuple_to_dict, TableNotExist

def get_todo_by_id(db_name, table_name, todo_id):
	try:
		cursor, db_connection = get_connection(db_name)
		query = """SELECT * FROM {} as t WHERE t.todo_id = {}""".format(table_name, todo_id)
		cursor.execute(query)
		result = cursor.fetchall()
		todo = map_tuple_to_dict(result)
		cursor.close()

	except AttributeError as e:
		print(e)

	except Exception as e:
		print(e)
		raise TableNotExist
		
	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")

	return todo