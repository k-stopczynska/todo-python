import json
import logging


def get_db_credentials(config_file):
	try:
		with open(config_file) as reader:
			data = json.load(reader)
			user = data['user']
			password = data['password']
			host = data['host']
		if not user or not password or not host:
			print ('Invalid credentials in config file')
			raise ValueError('invalid credentials')
		return user, password, host
	except FileNotFoundError as e:
		print(f"The file '{config_file}' does not exist.")
		raise e
	except (KeyError, json.JSONDecodeError) as e:
		print(f"Error reading credentials from '{config_file}': {e}")
		raise e
	except Exception as e:
		logging.exception(f"Unexpected error occurred: {e}")
		raise e
