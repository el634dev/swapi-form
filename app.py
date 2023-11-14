"""Import json to seperate data"""
import json
import requests
# Import flask, request and render template from Flask
from flask import Flask, request, render_template

app = Flask(__name__)

# SWAPI Links
SWAPI_BASE_LINK = "https://swapi.py4e.com/api/people/"

# Create a new route
@app.route('/', methods=['GET', 'POST'])
def form_data():
    """
    :desc: Request data from API and display it
    :params: None
    :return: None
    """
    # Check if the request method is POST
    if request.method == "POST":
        # Request data using request.value.get()
        char_index = request.form.get("char-index")
        # --------------------------------------------
        return_data = requests.get(f"{SWAPI_BASE_LINK}{char_index}", timeout=10).content
        # print(return_data)
        # --------------------------------------------
        context = {
          "name" : json.loads(return_data).get("name"),
          "height" : json.loads(return_data).get("height"),
          "mass" : json.loads(return_data).get("mass"),
          "eye_color" : json.loads(return_data).get("eye_color"),
          "hair_color" : json.loads(return_data).get("hair_color"),
        }
        return render_template('display.html', **context)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=False) 
  