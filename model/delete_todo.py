from db.connect import get_connection
from db.utils import map_tuple_to_dict


def delete_todo(db_name, table_name, todo_id):
	db_connection = None
	deleted_todo = {}
	try:
		cursor, db_connection = get_connection(db_name)
		query = """DELETE FROM {} as t WHERE t.todo_id = {}""".format(table_name, todo_id)
		cursor.execute(query)
		result = cursor.fetchall()
		deleted_todo = map_tuple_to_dict(result)
		db_connection.commit()
		cursor.close()
		
	except Exception as e:
		print(e)

	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")
	
	return deleted_todo
