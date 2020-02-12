import requests
import random

from config import *


class Client:

    def __init__(self, *args):
        self.base_path = 'http://localhost:8000'
        self.TOKEN, self.number_of_users, self.max_post_per_user, self.max_likes_per_user = args

    def start(self):
        self.repeat(self.signup, self.number_of_users)
        self.repeat(self.post, self.max_post_per_user)
        self.repeat(self.like, self.max_likes_per_user)

    def login(self):
        path = 'api-auth'

    def repeat(self, callback, number):
        while number > 0:
            callback()
            number -= 1

    def signup(self):
        path = 'api/signup'
        data = {
            'username': 'oleg.shepel_test@gmail.com',
            'password': 'test'
        }
        self.post_requester(path, data)

    def post(self):
        path = 'api/posts'
        data = {
            'description': 'some text'
        }
        self.post_requester(path, data)

    def like(self):
        random_post_number = random.randrange(10000)
        path = f"api/posts/{random_post_number}/like"
        self.get_requester(path)

    def get_requester(self, path=''):
        response = requests.get(f"{self.base_path}/{path}/")

    def post_requester(self, path='', data={}):
        response = requests.post(f"{self.base_path}/{path}/", data=data)


if __name__ == '__main__':
    params = [TOKEN, number_of_users, max_post_per_user, max_likes_per_user]
    client = Client(*params)
    client.start()
