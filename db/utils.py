import logging
from config import credentials


def get_db_credentials(credentials):
	try:
		user = credentials['user']
		password = credentials['password']
		host = credentials['host']
		if user and password and host:
			return user, password, host
		else:
			raise ValueError
	except ValueError as e:
		print(f"Error reading credentials: {e}")
		raise e
	except Exception as e:
		logging.exception(f"Unexpected error occurred: {e}")
		raise e


def map_tuple_to_dict(collection):
	data = []
	for tuple in collection:
		data.append({
			'todo_id': tuple[0],
			'title': tuple[1],
		 	'description': tuple[2],
		 	'status': tuple[3],
		 	'deadline': tuple[4]})
	return data

