from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import SQLAlchemyError

# Base and Engine Configuration
Base = declarative_base()
engine = create_engine("mysql+mysqlconnector://root:yourpassword@localhost/example_db", echo=False)

SessionLocal = sessionmaker(bind=engine)

# Declarative User Model Definition
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, username='{self.username}', email='{self.email}')>"

# Database Initialization, Table Creation, and Sessions
def init_db():
    """Create all tables defined in the models."""
    Base.metadata.create_all(bind=engine)

def create_user(session, username, email):
    """Safely create a new user using ORM objects."""
    if not username or not email:
        print("Username and email are required.")
        return
    
    try:
        new_user = User(username=username, email=email)
        session.add(new_user)
        session.commit()
        print(f"User '{username}' created successfully with ORM.")
    except SQLAlchemyError as e:
        session.rollback()
        print(f"Error creating user: {e}")

def get_user_by_username(session, username):
    """Query a user by username using the ORM session."""
    try:
        return session.query(User).filter_by(username=username).first()
    except SQLAlchemyError as e:
        print(f"Error querying user: {e}")
        return None

if __name__ == "__main__":
    init_db()
    db_session = SessionLocal()
    create_user(db_session, "keffalyssa", "keffalyssak@gmail.com")
    user = get_user_by_username(db_session, "keffalyssa")
    print(user)
    db_session.close()
