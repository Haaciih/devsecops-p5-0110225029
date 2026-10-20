# Simulasi in-memory database helper
USERS_TABLE = {
    "admin": "pbkdf2:sha256:dummyhashadmin",
    "user1": "pbkdf2:sha256:dummyhashuser1"
}

def get_user_record(username):
    return USERS_TABLE.get(username, None)