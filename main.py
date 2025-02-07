from flask import Flask, jsonify, render_template
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)  # Enable CORS for frontend interaction

# Serve UI
@app.route('/')
def index():
    return render_template('index.html')

# Sample API Routes without database
@app.route('/bus_routes', methods=['GET'])
def get_bus_routes():
    sample_routes = [
        {'id': 1, 'route_name': 'Northside', 'start_location': 'Church', 'end_location': 'Downtown'},
        {'id': 2, 'route_name': 'Southside', 'start_location': 'Church', 'end_location': 'Uptown'}
    ]
    return jsonify(routes=sample_routes)

@app.route('/youth', methods=['GET'])
def get_youth():
    sample_youth = [
        {'id': 1, 'name': 'John Doe', 'age': 12, 'parent_contact': '123-456-7890'},
        {'id': 2, 'name': 'Jane Doe', 'age': 14, 'parent_contact': '987-654-3210'}
    ]
    return jsonify(youth=sample_youth)

@app.route('/outreach_areas', methods=['GET'])
def get_outreach_areas():
    sample_areas = [
        {'id': 1, 'area_name': 'Downtown', 'average_income': 40000, 'notes': 'High traffic area'},
        {'id': 2, 'area_name': 'Suburbs', 'average_income': 60000, 'notes': 'Family-friendly'}
    ]
    return jsonify(outreach_areas=sample_areas)

@app.route('/newsfeed', methods=['GET'])
def get_newsfeed():
    sample_news = [
        {'id': 1, 'title': 'Sunday Service', 'content': 'Join us for worship this Sunday!'},
        {'id': 2, 'title': 'Youth Event', 'content': 'Fun activities for all kids on Saturday!'}
    ]
    return jsonify(newsfeed=sample_news)

if __name__ == '__main__':
    try:
        port = int(os.environ.get('PORT', 5000))
        app.run(host='0.0.0.0', port=port, debug=False)  # Set debug to False to avoid multiprocessing errors
    except SystemExit:
        print("Flask application exited unexpectedly.")
