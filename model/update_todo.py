from db.connect import get_connection
from db.utils import map_tuple_to_dict


def update_todo_db(db_name, table_name, todo, todo_id):
	try:
		cursor, db_connection = get_connection(db_name)
		query = "UPDATE {} SET title=%s, description=%s, status=%s, deadline=%s WHERE todo_id=%s".format(table_name)
		cursor.execute(query, (todo['title'], todo['description'], todo['status'], todo['deadline'], todo_id))
		print(todo_id)
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
