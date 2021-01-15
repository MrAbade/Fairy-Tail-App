from . import db

class Guild(db.Model):
    __tablename__ = 'guilds'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    sorcerer_list = db.relationship('Sorcerer', backref=db.backref('guild'))
