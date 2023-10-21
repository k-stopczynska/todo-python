from db.connect import get_connection
from db.utils import map_tuple_to_dict

def add_new_todo(db_name, table_name, todo):
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

	except Exception as e:
		print(e)

	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")

	return todo


