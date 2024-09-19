from flask import Flask, request, render_template
import requests

app = Flask(__name__)

API_KEY = 'bd404b3ded074574b8eb61888b718c62'  # Replace with your OpenCage API key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_info', methods=['POST'])
def get_info():
    name = request.form['name']
    date_of_birth = request.form['date_of_birth']
    time_of_birth = request.form['time_of_birth']
    place_of_birth = request.form['place_of_birth']

    url = f'https://api.opencagedata.com/geocode/v1/json?q={place_of_birth}&key={API_KEY}'
    response = requests.get(url).json()

    if response['results']:
        result = response['results'][0]
        latitude = result['geometry']['lat']
        longitude = result['geometry']['lng']
        timezone_info = result['annotations']['timezone']
        timezone_name = timezone_info['name']
        gmt_offset = timezone_info['offset_string']
    else:
        return 'Place not found', 404

    return f'''
    Name: {name}<br>
    Date of Birth: {date_of_birth}<br>
    Time of Birth: {time_of_birth}<br>
    Place of Birth: {place_of_birth}<br>
    Latitude: {latitude}<br>
    Longitude: {longitude}<br>
    Time Zone: {timezone_name}<br>
    GMT Offset: {gmt_offset}
    '''

if __name__ == '__main__':
    app.run(debug=True)
