from . import db

class Profile_Property(db.Model):

    _tablename_ = 'estate'
    id = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(300))
    Title_of_Property = db.Column(db.String(300))
    Number_of_Bedrooms = db.Column(db.Integer)
    Number_of_Bathrooms = db.Column(db.Integer)
    Locations = db.Column(db.String(300))
    Price = db.Column(db.Integer)
    filename = db.Column(db.String(300))

    def _init_(self, Type, Title_of_Property, Number_of_Bathrooms, Number_of_Bedrooms, Locations, Price, filename):
        self.Type = Type
        self.Title_of_Property = Title_of_Property
        self.Number_of_Bathrooms = Number_of_Bathrooms
        self.Number_of_Bedrooms = Number_of_Bedrooms
        self.Locations = Locations
        self.Price = Price
        self.filename = filename

    def  _repr_(self):
        return '<User %r>' % self.Title_of_Property