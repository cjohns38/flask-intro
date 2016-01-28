from app import db 
from models import User

# Insert data
db.session.add(User("cj", "cjohns38@gmail.com", "temp"))
db.session.add(User("admin", "ad@min.com", "admin"))

# Commit changes
db.session.commit()
