import requests
import random
import string

from config import *


class Client:

    def __init__(self, *args):
        self.users = []
        self.base_path = 'http://localhost:8000'
        self.TOKEN, self.number_of_users, self.max_post_per_user, self.max_likes_per_user = args

    def start(self):
        # signups
        self.repeat(self.signup, self.number_of_users)
        # posts
        for user in self.users:
            number_of_posts = random.randrange(10)
            number = number_of_posts if number_of_posts < self.max_post_per_user else self.max_post_per_user
            self.login(user)
            self.repeat(self.post, number)
            self.logout()
        # likes
        for user in self.users:
            number_of_likes = random.randrange(10)
            number = number_of_likes if number_of_likes < self.max_likes_per_user else self.max_likes_per_user
            self.login(user)
            self.repeat(self.like, number)
            self.logout()

    def login(self, user):
        path = 'api-auth/login'
        client = requests.session()
        client.get(f"{self.base_path}/{path}/")
        csrftoken = client.cookies['csrftoken']
        data = {
            'csrfmiddlewaretoken': csrftoken,
            'username': user['username'],
            'password': user['password']
        }
        headers = dict(Referer=f"{self.base_path}/{path}")
        client.post(f"{self.base_path}/{path}/", data=data, headers=headers)

    def logout(self):
        path = 'api-auth/logout'
        self.get_requester(path)

    def random_string(self, size):
        chars = string.ascii_lowercase + string.digits
        return ''.join(
            random.choice(chars) for x in range(size)
        )

    def repeat(self, callback, number):
        while number > 0:
            response = callback()
            status = int(str(response.status_code)[:1])
            if status == 5:
                break
            if status == 2:
                number -= 1
            else:
                pass

    def signup(self):
        path = 'api/signup'
        data = {
            'username': f"{self.random_string(10)}",
            'password': f"{self.random_string(20)}"
        }
        response = self.post_requester(path, data)
        status = int(str(response.status_code)[:1])
        if status == 2:
            self.users.append(data)
        return response

    def post(self):
        path = 'api/posts'
        data = {
            'description': f"{self.random_string(100)}"
        }
        return self.post_requester(path, data)

    def like(self):
        random_post_number = random.randrange(3)
        path = f"api/posts/{random_post_number}/like"
        return self.post_requester(path)

    def get_requester(self, path=''):
        response = requests.get(f"{self.base_path}/{path}/")
        return response

    def post_requester(self, path='', data=None):
        response = requests.post(f"{self.base_path}/{path}/", data=data)
        return response


if __name__ == '__main__':
    params = [TOKEN, number_of_users, max_post_per_user, max_likes_per_user]
    client = Client(*params)
    client.start()
