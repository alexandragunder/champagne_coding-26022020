
from flask import Flask, request, jsonify
from voluptuous import Schema, Required, Any, Coerce, Invalid, MultipleInvalid
from joblib import load
from pathlib import Path
import pandas as pd
import sklearn


def predict():    
    """ Main function. Predict house price given a set of input data and a
        stored model. Return a json struct"""

    # Get input parameters

    input_ok, data = fetch_input()
    if not input_ok:
        return 'Error: %s' % data

    # Import the trained model

    model = load_model( 'grad_boosting_regressor' )
    if not model:
        return 'Error: Could not load model'

    # The model needs the input data in a pandas dataframe. Pass array with headers
    # ensures correct estmiate

    input_data = pd.DataFrame([data])
    headers = [ 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
                'floors', 'waterfront', 'view', 'condition', 'grade',
                'sqft_above', 'sqft_basement', 'yr_built',
                'yr_renovated', 'zipcode', 'lat', 'long',
                'sqft_living15', 'sqft_lot15', 'year']

    # Now run a prediction given the model and input_data

    prediction = model.predict( input_data[headers] )

    # Return a json structure containing input and resulting prediction

    ret = { 'input': data,
            'prediction': prediction[0] }
    return jsonify( ret )


def load_model( name ):
    """ Load the datamodel that we trained and saved in the Jupyter notebook """
    return load( Path( 'models', '{}.joblib'.format( name )))


def fetch_input():
    """ Handle input through Flask request.values, then validate the input
        using the voluptuous library. Set default values if input
        variables are not given. Returns a dict containg input or
        default values for all parameters """

    s = Schema({
        Required( 'bedrooms', default=2 ): Coerce( int ),
        Required( 'bathrooms', default=2 ): Any( Coerce( float ), Coerce( int )),
        Required( 'sqft_living', default=2000 ): Coerce( int ),
        Required( 'sqft_lot', default=20000 ): Coerce( int ),
        Required( 'floors', default=2 ): Any( Coerce( float ), Coerce( int ) ),
        Required( 'waterfront', default=0 ): Coerce( int ),
        Required( 'view', default=2 ): Coerce( int ),
        Required( 'condition', default=3 ): Coerce( int ),
        Required( 'grade', default=8 ): Coerce( int ),
        Required( 'sqft_above', default=2000 ): Coerce( int ),
        Required( 'sqft_basement', default=0 ): Coerce( int ),
        Required( 'yr_built', default=1990 ): Coerce( int ),
        Required( 'yr_renovated', default=0 ): Coerce( int ),
        Required( 'zipcode', default=98006 ): Coerce( int ),
        Required( 'lat', default=47.5 ): Coerce( float ),
        Required( 'long', default=-122.1 ): Coerce( float ),
        Required( 'sqft_living15', default=2000 ): Coerce( int ),
        Required( 'sqft_lot15', default=20000 ): Coerce( int ),
        Required( 'year', default=2015 ): Coerce( int ),
    })
    try:
        return 1, s( dict( request.values ))
    except MultipleInvalid as e: 
        return 0, str( e )


#
# Flask framework below
#
app = Flask( __name__, static_url_path='' )

@app.route( '/liveness' )
def liveness():
    return 'Hello there!'

@app.route( '/', methods=[ 'GET' ])
def root():
    return app.send_static_file( 'index.html' )

@app.route( '/script.js', methods=[ 'GET' ])
def script():
    return app.send_static_file( 'script.js' )

@app.route( '/predict', methods=[ 'GET', 'POST' ])
def query_predict():
    return predict() 

#
# Launch debug mode if run as script
#
if __name__ == '__main__':
    app.run( debug=True, host='0.0.0.0', port=8080 )

