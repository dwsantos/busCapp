from flask import Flask, jsonify, request, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for frontend interaction
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bus_capp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models
class BusRoute(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route_name = db.Column(db.String(100), nullable=False)
    start_location = db.Column(db.String(100), nullable=False)
    end_location = db.Column(db.String(100), nullable=False)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)

class Youth(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    parent_contact = db.Column(db.String(100), nullable=False)
    last_attended = db.Column(db.DateTime, default=datetime.utcnow)

class OutreachArea(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    area_name = db.Column(db.String(100), nullable=False)
    average_income = db.Column(db.Float, nullable=False)
    notes = db.Column(db.String(200))

class NewsfeedItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text, nullable=False)
    posted_on = db.Column(db.DateTime, default=datetime.utcnow)

# Serve UI
@app.route('/')
def index():
    return render_template('index.html')

# API Routes
@app.route('/bus_routes', methods=['GET'])
def get_bus_routes():
    routes = BusRoute.query.all()
    return jsonify([{'id': r.id, 'route_name': r.route_name, 'start_location': r.start_location, 'end_location': r.end_location} for r in routes])

@app.route('/youth', methods=['GET'])
def get_youth():
    youths = Youth.query.all()
    return jsonify([{'id': y.id, 'name': y.name, 'age': y.age, 'parent_contact': y.parent_contact} for y in youths])

@app.route('/outreach_areas', methods=['GET'])
def get_outreach_areas():
    areas = OutreachArea.query.all()
    return jsonify([{'id': a.id, 'area_name': a.area_name, 'average_income': a.average_income, 'notes': a.notes} for a in areas])

@app.route('/newsfeed', methods=['GET'])
def get_newsfeed():
    items = NewsfeedItem.query.order_by(NewsfeedItem.posted_on.desc()).all()
    return jsonify([{'id': i.id, 'title': i.title, 'content': i.content} for i in items])

@app.before_first_request
def create_tables():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
