# File name: user.py
# Author: Elina Maunula
# Description: This file contains the class "UserManager"

class UserManager:
    users = [{'id': 1, 'username': 'test', 'password': 'test', 'is_vip':  False}]
    current_user = None

    @classmethod
    def create_user(cls, username, password):
        user = {'id': len(cls.users) + 1, 'username': username, 'password': password, 'is_vip': False}
        cls.users.append(user)
        return user

    @classmethod
    def authenticate_user(cls, username, password):
        for user in cls.users:
            if user['username'] == username and user['password'] == password:
                cls.current_user = user
                return user
        return None
    
    @classmethod
    def become_vip(cls, user_id):
        for user in cls.users:
            if user['id'] == user_id:
                user['is_vip'] = True
                break