"""
Here the models for our database is defined.

I am using Postgres, Flask-SQLAlchemy for this application.

For an introduction to Flask-SQLAlchemy check out: http://flask-sqlalchemy.pocoo.org/2.1/

__init__ function for each model is a constructor, and is necessary to enter
""" 
from app import db

class Ads(db.Model):
    """
    This model gives us a set of specific information for each user in this application
    
    parameters:
    @text_body - the text of the ad
    @post_id - unique post id
    @label - where the ad is prostitution or not
    functions:
    __str__ - Returns the user name and password as an formatted string <Id: post_id>
    """
    __tablename__ = 'ads'
    id = db.Column(db.Integer, primary_key=True)
    text_body = db.Column(db.String)
    post_id = db.Column(db.String,unique=True) 
    label = db.Column(db.String)
    
    def __init__(self,text_body,post_id,label):
        self.text_body = text_body
        self.post_id = post_id
        self.label = label
        
    def __str__(self):
        return "<Id: {}>".format(self.post_id)

