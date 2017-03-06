import os
# from server import db
from base64 import urlsafe_b64encode
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    header = db.Column(db.String(40))
    signature = db.Column(db.String(60), nullable=True)
    body = db.Column(db.Text)
    slug = db.Column(db.String(40), unique=True)

    def is_slug_unique(self, slug):
        return self.query.filter_by(slug=slug).exists()

    def generate_slug(self):
        to_encode = os.urandom(30)
        slug = urlsafe_b64encode(to_encode)
        if not self.is_slug_unique(slug):
            slug = self.generate_slug()
        return slug

    def __init__(self, header, signature, body, slug):
        self.header = header
        self.signature = signature
        self.body = body
        self.slug = self.generate_slug()
