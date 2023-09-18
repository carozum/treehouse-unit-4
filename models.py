from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a variable called engine and set it equal to create_engine(). Use create_engine to create a SQLite database called users.db and set echo to True
engine = create_engine('sqlite:///users.db', echo=False)

# creates a session
Session = sessionmaker(bind=engine)
session = Session()


# create the model class called User, and it takes Base as an argument (it inherits from Base).
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return f"<User:(name = {self.name}, fullname = {self.fullname}, nickname ={self.nickname} )>"


if __name__ == "__main__":
    # create the database
    Base.metadata.create_all(engine)

    # populate the database (since the ID is a primary key we don't have to pass a value) - single user
    caro_user = User(name="caro", fullname="zum", nickname="carozum")
    # print(caro_user.name)
    # print(caro_user.id)
    session.add(caro_user)
    # print(session.new)
    session.commit()

    # Add a list of users
    new_users = [
        User(name='Grace', fullname='Grace Hopper', nickname='Pioneer'), User(
            name='Alan', fullname='Alan Turing', nickname='Computer Scientist'),
        User(name='Katherine', fullname='Katherine Johnson', nickname='')]
    session.add_all(new_users)
    session.commit()
