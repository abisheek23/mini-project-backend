def create_user(username, password, is_admin=False):
    return {
        "username": username,
        "password": password,
        "is_admin": is_admin
    }

