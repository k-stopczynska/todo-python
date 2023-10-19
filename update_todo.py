from connect import get_connection

new_todo = {'title': 'Learn Django', 'description': 'Do Django REST API to excercize',
			'status': 'todo', 'deadline': '2023/12/21'
}

def update_todo(db_name, table_name, todo, todo_id):
	try:
		cursor, db_connection = get_connection(db_name)
		query = "UPDATE {} SET title=%s, description=%s, status=%s, deadline=%s WHERE todo_id=%s".format(table_name)
		cursor.execute(query, (todo['title'], todo['description'], todo['status'], todo['deadline'], todo_id))
		db_connection.commit()
		cursor.close()

	except Exception as e:
		print(e)

	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")


update_todo('todos', 'todo', new_todo, 1)


