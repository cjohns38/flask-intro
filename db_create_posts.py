from project import db 
from project.models import BlogPost

# Insert data
db.session.add(BlogPost("Blog post1", "First post"))
db.session.add(BlogPost("Blog post2", "Second post"))

# Commit changes
db.session.commit()
