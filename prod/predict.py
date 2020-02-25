
from flask import Flask, request, jsonify, render_template
from voluptuous import Schema, MultipleInvalid
import pandas as pd
import sklearn

from datamodel import datamodel

def predict():
    """ Main function. Predict house price given a set of input data and a
        stored model. Return a json struct"""

    dm = datamodel()
    
    # Get input parameters
    input_ok, data = fetch_input()
    if not input_ok:
        return 'Error: %s' % data

    # Import the trained model
    model = dm.load_model( 'grad_boosting_regressor' )
    if not model:
        return 'Error: Could not load model'

    # The model needs the input data in a pandas dataframe. Pass array with headers
    # ensures correct estmiate    
    headers = dm.headers()
    input_data = pd.DataFrame([data])

    # Now run a prediction given the model and input_data
    prediction = model.predict( input_data[headers] )

    # Return a json structure containing input and resulting prediction
    ret = { 'input': data,
            'prediction': "%.2f" % prediction[0] }
    return ret



def fetch_input():
    """ Handle input through Flask request.values, then validate the input
        using the voluptuous library. Set default values if input
        variables are not given. Returns a dict containg input or
        default values for all parameters """

    s = datamodel().schema()
    try:
        return 1, s( dict( request.values ))
    except MultipleInvalid as e: 
        return 0, str( e )


#
# Flask framework below
#
app = Flask( __name__ )

@app.route( '/liveness' )
def liveness():
    return 'Hello there!'


@app.route( '/' )
def serve_html():

    dm = datamodel()
    return render_template( 'predict.html', options = dm.description(), models = dm.get_models() )


@app.route( '/script.js', methods=[ 'GET' ])
def serve_script():
    return app.send_static_file( 'script.js' )


@app.route( '/predict', methods=[ 'GET', 'POST' ])
def query_predict():
    return jsonify( predict())

#
# Launch debug mode if run as script
#
if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0', port=8080 )

