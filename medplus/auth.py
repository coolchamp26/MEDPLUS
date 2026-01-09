import hashlib
from medplus.database import db

class Auth:
    @staticmethod
    def hash_password(password):
        return hashlib.sha256(password.encode()).hexdigest()

    @staticmethod
    def register(username, password, role='USER'):
        # Check if user exists
        existing = db.fetch_one("SELECT username FROM users WHERE username = ?", (username,))
        if existing:
            return False, "Username already exists."
        
        hashed_pw = Auth.hash_password(password)
        try:
            db.execute_query("INSERT INTO users (username, password_hash, role) VALUES (?, ?, ?)", 
                             (username, hashed_pw, role))
            return True, "Registration successful."
        except Exception as e:
            return False, f"Registration failed: {str(e)}"

    @staticmethod
    def login(username, password, role='USER'):
        user = db.fetch_one("SELECT password_hash, role FROM users WHERE username = ?", (username,))
        
        if not user:
            return False, "User not found."
        
        stored_hash, stored_role = user
        
        # Verify role (Admin trying to login as User or vice versa strictly? 
        # Original code had separate login screens. We can keep that logic or unify.
        # Let's enforce role check to match original logic)
        if stored_role != role:
            return False, f"Invalid role. This account is not a {role}."

        if Auth.hash_password(password) == stored_hash:
            return True, "Login successful."
        else:
            return False, "Invalid password."

auth = Auth()
