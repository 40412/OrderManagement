class UserManager:
    users = []

    @classmethod
    def create_user(cls, username, password):
        user = {'id': len(cls.users) + 1, 'username': username, 'password': password}
        cls.users.append(user)
        return user

    @classmethod
    def authenticate_user(cls, username, password):
        for user in cls.users:
            if user['username'] == username and user['password'] == password:
                return user
        return None
    
    @classmethod
    def become_vip(cls, user_id):
        for user in cls.users:
            if user['id'] == user_id:
                user['is_vip'] = True
                break