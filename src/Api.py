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
        report = ""
        for user in self.users.json():
            count = 0
            for post in self.posts.json():
                if post['userId'] == user['id']:
                    count += 1
            report += f'{user["name"]} napisał(a) {count} postów\n'
        return report

    def not_unique_posts(self) -> list:
        # posts_doubled = self.posts.json() + self.posts.json()
        # posts_doubled = posts_doubled[:150]
        unique_values = list({post['title']: post for post in self.posts.json()}.values())
        duplications = [post for post in unique_values if self.posts.json().count(post) > 1]
        return duplications

    def closest_user(self):
        report = {}
        for user1 in self.users.json():
            user1_geo = user1['address']['geo']
            data = {}
            for user2 in self.users.json():
                user2_geo = user2['address']['geo']
                lon1, lat1, lon2, lat2 = map(radians, map(float,
                                                          [user1_geo['lat'],
                                                           user1_geo['lng'],
                                                           user2_geo['lat'],
                                                           user2_geo['lng']]))

                # haversine formula
                dlon = lon2 - lon1
                dlat = lat2 - lat1
                a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
                c = 2 * asin(sqrt(a))
                r = 6371  # in km
                if user1['name'] != user2['name']:
                    data[user2['name']] = c * r
            report[user1['name']] = min(data, key=data.get)
            # report += f'Najbliżej użytkownika {user1["name"]} mieszka {min(data, key=data.get)}\n'
        return report
        # print(sorted(data, key=data.get))


Api = Api()
Api.set_posts()
Api.set_users()

print(Api.count_posts_by_users())
print(Api.not_unique_posts())
print(Api.closest_user())
