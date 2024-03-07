"""Models for Blogly."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)


class User(db.Model):
    """users"""

    __tablename__ = "users"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    first_name = db.Column(db.String(20),
                     nullable=False,
                     unique=False)
    last_name = db.Column(db.String(20),
                     nullable=False,
                     unique=False)
    image_url = db.Column(db.String(500), nullable=False)

    def greet(self):
        """Greet using name."""

        return f"I'm {self.name} the {self.species or 'thing'}"

    def feed(self, units=10):
        """Nom nom nom."""

        self.hunger -= units
        self.hunger = max(self.hunger, 0)

    def __repr__(self):
        """Show info about pet."""

        p = self
        return f"<Pet {p.id} {p.name} {p.species} {p.hunger}>"

    @classmethod
    def get_by_species(cls, species):
        """Get all pets matching that species."""

        return cls.query.filter_by(species=species).all()
    
    
def get_full_name(self):
    
    """Return the full name of a user
    """
    u = self # current user
    
    return f"{u.first_name} {u.last_name}"
