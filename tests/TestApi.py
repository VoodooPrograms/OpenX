import unittest

from src.Api import Api


class TestApi(unittest.TestCase):

    def setUp(self):
        self.api = Api

    def test_set_posts(self):
        self.api.set_posts()
        self.assertIsNotNone(self.api.posts)
        self.assertEqual(self.api.posts.status_code, 200)

    def test_set_users(self):
        self.api.set_users()
        self.assertIsNotNone(self.api.users)
        self.assertEqual(self.api.users.status_code, 200)

    def test_count_posts_by_users(self):
        result = self.api.count_posts_by_users()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)

    def test_not_unique_posts(self):
        result = self.api.not_unique_posts()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)

    def test_closest_user(self):
        result = self.api.closest_user()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, dict)
