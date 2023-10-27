import unittest
from config import credentials
from db.utils import get_db_credentials, map_tuple_to_dict


class TestUtils(unittest.TestCase):

	def test_get_db_credentials_real_credentials(self):
		self.assertEqual(get_db_credentials(credentials), ('root','Leonberger888','localhost') )

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
