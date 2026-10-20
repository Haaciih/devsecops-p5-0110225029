from app.database import get_user_record

def verify_credentials(username, password):
    if not username or not password:
        return False
    user = get_user_record(username)
    if not user:
        return False
    # Simulasi autentikasi sederhana
    return True