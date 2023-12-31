from db.connect import get_connection
from db.utils import map_tuple_to_dict, TableNotExist

def add_new_todo(db_name, table_name, todo):
	db_connection = None
	try:
		cursor, db_connection = get_connection(db_name)
		query = """INSERT INTO todo ({}) VALUES ('{}', '{}', '{}', '{}')""".format(
            ', '.join(todo.keys()),
           	 	todo['title'],
            	todo['description'],
            	todo['status'],
            	todo['deadline'],
        	)
		cursor.execute(query)
		result = cursor.fetchall()
		todo = map_tuple_to_dict(result)
		db_connection.commit()
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


