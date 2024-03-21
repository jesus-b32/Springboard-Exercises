from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class Pet(db.Model):
    """Pet."""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.Text,
                     nullable=False)
    species = db.Column(db.Text,
                        nullable=False)
    photo_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)
    

def testing_data():
#     """Create some sample data."""

    # In case this is run more than once, empty out existing data
    # Post.query.delete()
    for pet in Pet.query.all():
        db.session.delete(pet)     
    db.session.commit()
    
    # Add testing data 
    pet1 = Pet(name='Buddy',
                species='dog',
                photo_url='https://www.vidavetcare.com/wp-content/uploads/sites/234/2022/04/golden-retriever-dog-breed-info.jpeg',
                age=5,
                available = False)
    pet2 = Pet(name='Scooby Doo',
            species='dog',
            photo_url='https://upload.wikimedia.org/wikipedia/en/5/53/Scooby-Doo.png',
            age=7)
    db.session.add_all([pet1, pet2])    
    db.session.commit()