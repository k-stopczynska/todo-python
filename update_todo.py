from connect import get_connection

new_todo = {'title':'Learn Django', 'description': 'Do Django REST API to excercize',
	'status': 'todo', 'deadline': '2023/12/21'
}

def update_todo(db_name, table_name, new_todo):
	try:
		cursor, db_connection = get_connection(db_name)
		query = """UPDATE todo as t ({}) SET ('{}', '{}', '{}', '{}') WHERE t.todo_id = 1""".format(
            ', '.join(new_todo.keys()),
           	 	new_todo['title'],
            	new_todo['description'],
            	new_todo['status'],
            	new_todo['deadline'],
        	)

		print(query)
		cursor.execute(query)
		db_connection.commit()
		cursor.close()

	except Exception as e:
		print(e)

	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")


update_todo('todos', 'todo', new_todo)


