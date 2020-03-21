import requests
from math import radians, cos, sin, asin, sqrt


class Api:
    posts_url = 'https://jsonplaceholder.typicode.com/posts'
    users_url = 'https://jsonplaceholder.typicode.com/users'

    def __init__(self):
        self.posts = None
        self.users = None

    def set_posts(self):
        self.posts = requests.get(self.posts_url)

    def set_users(self):
        self.users = requests.get(self.users_url)

    def count_posts_by_users(self) -> str:
        pass

    def not_unique_posts(self) -> list:
        pass

    def closest_user(self):
        pass


Api = Api()
Api.set_posts()
Api.set_users()

