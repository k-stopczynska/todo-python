import unittest
import datetime
import mysql.connector
from db.utils import get_db_credentials, map_tuple_to_dict, TableNotExist
from model.get_all_todos import get_all_todos
from model.get_todos_by_status import get_todos_by_status
from model.get_todo_by_id import get_todo_by_id
from model.add_new_todo import add_new_todo
from model.update_todo import update_todo_db
from model.delete_todo import delete_todo

class TestUtils(unittest.TestCase):

	def test_get_db_credentials_real_credentials(self):
		credentials = {'user': 'root', 'password': 'blabla', 'host': 'localhost'}
		self.assertEqual(get_db_credentials(credentials), ('root', 'blabla', 'localhost'))

	def test_get_db_credentials_fake_credentials(self):
		fake_credentials = {'host': '', 'user': '', 'password': ''}
		with self.assertRaises(ValueError):
			get_db_credentials(fake_credentials)

	def test_get_db_credentials_no_credentials(self):
		with self.assertRaises(Exception):
			get_db_credentials()

	def test_map_tuple_to_dict_correct_collection(self):
		collection = [('2', 'water plants', 'add some sanitizer to water', 'todo', '2023/10/31'), ('3', 'go for a walk', 'take the dog with you', 'in progress', '2023/10/27') ]
		self.assertEqual(map_tuple_to_dict(collection), [{
			'todo_id': '2',
			'title': 'water plants',
		 	'description': 'add some sanitizer to water',
		 	'status': 'todo',
		 	'deadline': '2023/10/31'}, {
			'todo_id': '3',
			'title': 'go for a walk',
		 	'description': 'take the dog with you',
		 	'status': 'in progress',
		 	'deadline': '2023/10/27'}])

	def test_map_tuple_to_dict_incorrect_collection_length(self):
		collection = [('2', 'water plants', 'add some sanitizer to water', 'todo'), ('3', 'go for a walk', 'take the dog with you', 'in progress', '2023/10/27') ]
		with self.assertRaises(IndexError):
			map_tuple_to_dict(collection)

	def test_map_tuple_to_dict_no_collection(self):
		with self.assertRaises(TypeError):
			map_tuple_to_dict()


class TestGetAllTodos(unittest.TestCase):
	def test_get_all_todos_correct_inputs(self):
		db_name = 'todos'
		table_name = 'todo'
		self.assertEqual(get_all_todos(db_name, table_name), [{
				'todo_id': 4,
				'title': 'do something',
				'description': 'do it quickly',
				'status': 'todo',
				'deadline': datetime.date(2023, 10, 31)
			},
			{
			'todo_id': 5,
			'title': 'do anything',
		 	'description': 'do it slowly',
		 	'status': 'done',
		 	'deadline': datetime.date(2023, 10, 27)}, {
			'todo_id': 6,
			'title': 'do nothing',
		 	'description': 'just do it',
		 	'status': 'pending',
		 	'deadline': datetime.date(2023, 11, 30)}])

	def test_get_all_todos_incorrect_inputs_wrong_table(self):
		db_name = 'todos'
		table_name = 'todoss'
		with self.assertRaises(TableNotExist):
			get_all_todos(db_name, table_name)

class TestGetTodosByStatus(unittest.TestCase):
	def test_get_todos_by_status_correct_inputs_todo(self):
		db_name = 'todos'
		table_name = 'todo'
		self.assertEqual(get_todos_by_status(db_name, table_name, 'todo'), [{
				'todo_id': 4,
				'title': 'do something',
				'description': 'do it quickly',
				'status': 'todo',
				'deadline': datetime.date(2023, 10, 31)
			}])

	def test_get_todos_by_status_correct_inputs_pending(self):
		db_name = 'todos'
		table_name = 'todo'
		self.assertEqual(get_todos_by_status(db_name, table_name, 'pending'),
							 [{
			'todo_id': 6,
			'title': 'do nothing',
		 	'description': 'just do it',
		 	'status': 'pending',
		 	'deadline': datetime.date(2023, 11, 30)}])

	def test_get_todos_by_status_correct_inputs_done(self):
		db_name = 'todos'
		table_name = 'todo'
		self.assertEqual(get_todos_by_status(db_name, table_name, 'done'),
							 [{
			'todo_id': 5,
			'title': 'do anything',
		 	'description': 'do it slowly',
		 	'status': 'done',
		 	'deadline': datetime.date(2023, 10, 27)}])

	def test_get_todos_by_status_incorrect_inputs_undefined_status_name(self):
		db_name = 'todos'
		table_name = 'todo'
		self.assertEqual(get_todos_by_status(db_name, table_name, 456), [])

	def test_get_todos_by_status_incorrect_inputs_wrong_table(self):
		db_name = 'todos'
		table_name = 'todoss'
		with self.assertRaises(TableNotExist):
			get_todos_by_status(db_name, table_name, 'pending')

	def test_get_todos_by_status_incorrect_inputs_status_name_variable(self):
		db_name = 'todos'
		table_name = 'todo'
		with self.assertRaises(NameError):
			get_todos_by_status(db_name, table_name, done)


class TestGetTodosById(unittest.TestCase):
	def test_get_todo_by_id_correct_input(self):
		db_name = 'todos'
		table_name = 'todo'
		self.assertEqual(get_todo_by_id(db_name, table_name, '4'), [{
				'todo_id': 4,
				'title': 'do something',
				'description': 'do it quickly',
				'status': 'todo',
				'deadline': datetime.date(2023, 10, 31)
			}])

	def test_get_todo_by_id_incorrect_input_undefined_id(self):
		db_name = 'todos'
		table_name = 'todo'
		self.assertEqual(get_todo_by_id(db_name, table_name, 456789456), [])

	def test_get_todo_by_id_incorrect_inputs_wrong_table(self):
		db_name = 'todos'
		table_name = 'todoss'
		with self.assertRaises(TableNotExist):
			get_todo_by_id(db_name, table_name, 6)

	def test_get_todos_by_id_incorrect_inputs_variable_id_id(self):
		db_name = 'todos'
		table_name = 'todo'
		self.assertEqual(get_todos_by_status(db_name, table_name, id), [])

	def test_get_todos_by_id_incorrect_inputs_variable_id(self):
		db_name = 'todos'
		table_name = 'todo'
		with self.assertRaises(NameError):
			get_todos_by_status(db_name, table_name, something)

class TestAddNewTodo(unittest.TestCase):
	def test_add_new_todo_correct_input(self):
		db_name = 'todos'
		table_name = 'todo'
		new_todo = {
			'title': 'test your code',
			'description': 'use unittest to test your code with negative inputs also',
			'status': 'in progress',
			'deadline': '2023-11-30'}
		self.assertEqual(add_new_todo(db_name, table_name, new_todo), {
				'title': 'test your code',
				'description': 'use unittest to test your code with negative inputs also',
				'status': 'in progress',
				'deadline': '2023-11-30'})

	def test_add_new_todo_incorrect_input_wrong_data_type(self):
		db_name = 'todos'
		table_name = 'todo'
		new_todo = ('test your code', 'use unittest', 'in review', '2023-11-30')
		with self.assertRaises(AttributeError) as err:
			add_new_todo(db_name, table_name, new_todo)
			self.assertEquals(str(err.exception),"'tuple' object has no attribute 'keys'")

	def test_add_new_todo_incorrect_input_wrong_data_type_inside(self):
		db_name = 'todos'
		table_name = 'todo'
		new_todo = {
			'title': 123456,
			'description': 'use unittest to test your code with negative inputs also',
			'status': 'in review',
			'deadline': '2023-11-30'}
		with self.assertRaises(Exception) as err:
			self.assertEquals(str(err.exception),"Data truncated for column 'status' at row 1")

	def test_add_new_todo_incorrect_inputs_wrong_table(self):
		db_name = 'todos'
		table_name = 'todoss'
		new_todo = {
			'title': 'test your code',
			'description': 'use unittest to test your code with negative inputs also',
			'status': 'in progress',
			'deadline': '2023-11-30'}
		with self.assertRaises(TableNotExist):
			add_new_todo(db_name, table_name, new_todo)


class TestUpdateTodo(unittest.TestCase):
	def test_update_todo_correct_input(self):
		db_name = 'todos'
		table_name = 'todo'
		updated_todo = {
				'todo_id': 4,
				'title': 'test your code',
				'description': 'use unittest to test your code with negative inputs also',
				'status': 'in progress',
				'deadline': '2023-11-30'}
		self.assertEqual(update_todo_db(db_name, table_name, updated_todo, 4), {
				'todo_id': 4,
				'title': 'test your code',
				'description': 'use unittest to test your code with negative inputs also',
				'status': 'in progress',
				'deadline': '2023-11-30'})

	def test_update_todo_incorrect_inputs_wrong_table(self):
		db_name = 'todos'
		table_name = 'todoss'
		updated_todo = {
			'title': 'test your code',
			'description': 'use unittest to test your code with negative inputs also',
			'status': 'in progress',
			'deadline': '2023-11-30'}
		with self.assertRaises(TableNotExist):
			update_todo_db(db_name, table_name, updated_todo, 6)




class TestDeleteTodo(unittest.TestCase):
	def test_delete_todo_correct_input(self):
		db_name = 'todos'
		table_name = 'todo'
		self.assertEqual(delete_todo(db_name, table_name, 4), [])

	def test_delete_todo_incorrect_inputs_wrong_table(self):
		db_name = 'todos'
		table_name = 'todoss'
		with self.assertRaises(TableNotExist):
			add_new_todo(db_name, table_name, 6)
