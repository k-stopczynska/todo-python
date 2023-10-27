from db.connect import get_connection


def create_db(db_name):
	try:
		cursor, db_connection = get_connection(db_name)
		cursor.execute(
			"CREATE DATABASE {} DEFAULT CHARACTER SET 'utf8'".format(db_name))
	except Exception as err:
		print("Failed creating database: {}".format(err))
		exit(1)


def create_and_use_db(db_name):
	try:
		cursor, db_connection = get_connection(db_name)
		cursor.execute("USE {}".format(db_name))
	except Exception as err:
		print("Database {} does not exist".format(db_name))
		create_db(db_name)
		print("Database {} created successfully.".format(db_name))
		db_connection.database = db_name
	print(f"you are now using {db_name} database")
	return f"you are now using {db_name} database"


