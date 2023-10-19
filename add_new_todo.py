from connect import get_connection

todo = {'title':'Learn Flask', 'description': 'Do Flask REST API to excercize',
	'status': 'todo', 'deadline': '2023/12/21'
}

def add_new_todo(db_name, table_name, new_todo):
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
		db_connection.commit()
		cursor.close()

	except Exception as e:
		print(e)

	finally:
		if db_connection:
			db_connection.close()
			print("Connection closed")


add_new_todo('todos', todo)


