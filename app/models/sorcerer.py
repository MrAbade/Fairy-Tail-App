from . import db


class Sorcerer(db.Model):
    __tablename__ = 'sorcerers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))

    guild_id = db.Column(db.Integer, db.ForeignKey('guilds.id'))
