from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=False, nullable=False)
    last_name = db.Column(db.String(120), unique=False, nullable=False)
    user_name = db.Column(db.String(120), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    
    planeta_fav = db.relationship('PlanetasFavoritos', backref='user', lazy=True)
    personaje_fav = db.relationship('PersonajesFavoritos', backref='user', lazy=True)

    def __repr__(self):
        return '<User %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "user_name": self.user_name,
            "email": self.email,
        }

# Clase Personajes
class Personajes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    height = db.Column(db.String(250))
    hair_color = db.Column(db.String(250), nullable=False)
    skin_color = db.Column(db.String(250), nullable=False)
    eye_color = db.Column(db.String(250), nullable=False)
    birth_year = db.Column(db.String(250), nullable=False)
    gender = db.Column(db.String(250), nullable=False)

    personajes_favoritos = db.relationship('PersonajesFavoritos', backref='personajes', lazy=True)
   

    def __repr__(self):
        return '<Personajes %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "hair_color": self.hair_color,
            "skin_color": self.skin_color,
            "eye_color": self.eye_color,
            "birth_year": self.birth_year,
            "gender": self.gender,
        }


# Tabla intermedia PersonajesFavoritos
class PersonajesFavoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    personaje_favorito = db.Column(db.Integer, db.ForeignKey('personajes.id'),
        nullable=False)
    
 

    def __repr__(self):
        return '<PersonajesFav %r>' % self.id

    def serialize(self):
        return {
          "id": self.id,
          "user_id": self.user_id,
          "personaje_favorito": self.personaje_favorito
        }
    
# Clase Planetas
class Planetas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250))
    rotation_period = db.Column(db.String(250))
    orbital_period = db.Column(db.String(250), nullable=False)
    diameter = db.Column(db.String(250), nullable=False)
    climate = db.Column(db.String(250), nullable=False)
    gravity = db.Column(db.String(250), nullable=False)
    terrain = db.Column(db.String(250), nullable=False)

    planetas_favoritos = db.relationship('PlanetasFavoritos', backref='planetas', lazy=True)
    
    
    def __repr__(self):
        return '<Planetas %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "diameter": self.diameter,
            "climate": self.climate,
            "gravity": self.gravity,
            "terrain": self.terrain,
        }

# Tabla intermedia PlanetasFavoritos
class PlanetasFavoritos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
        nullable=False)
    planeta_favorito = db.Column(db.Integer, db.ForeignKey('planetas.id'),
        nullable=False)
    
    

    def __repr__(self):
        return '<PlanetasFav %r>' % self.user_id

    def serialize(self):
        return {
          "id": self.id,
          "user_id": self.user_id,
          "planeta_favorito": self.planeta_favorito
        }