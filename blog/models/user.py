from sqlalchemy import Column, String, Integer, Boolean
from flask_login import UserMixin
from blog.models.database import db

class User(db.Model, UserMixin):
    id = Column(Integer, primary_key=True)
    username = Column(String(00), unique=True, nullable=True)
    is_staff = Column(Boolean, nullable=False, default=False)

    def __repr__(self):
        return f'<User #{self.id} {self.username}'