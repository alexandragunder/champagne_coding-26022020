
from flask import Flask, request, jsonify, render_template
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

    headers = [ 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
                'floors', 'waterfront', 'view', 'condition', 'grade',
                'sqft_above', 'sqft_basement', 'yr_built',
                'yr_renovated', 'zipcode', 'lat', 'long',
                'sqft_living15', 'sqft_lot15', 'year']
    input_data = pd.DataFrame([data])

    # Now run a prediction given the model and input_data

    prediction = model.predict( input_data[headers] )

    # Return a json structure containing input and resulting prediction

    ret = { 'input': data,
            'prediction': "%.2f" % prediction[0] }
    return ret


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
app = Flask( __name__ )

@app.route( '/liveness' )
def liveness():
    return 'Hello there!'

@app.route( '/' )
def serve_html():

    description = { 'bedrooms': [  'Number of bedrooms', 2 ],
                    'bathrooms': [ 'Number of bathrooms (where .5 accounts for a room with a toilet but no shower)', 2 ],
                    'sqft_living': [ 'Square footage of the apartments interior living space', 2000 ],
                    'sqft_lot': [ 'Square footage of the land space', 20000 ],
                    'floors': [ 'Number of floors (float or int)', 2 ],
                    'waterfront': [ 'Waterfront (0=no, 1=yes)', 0 ],
                    'view': [ 'An index from 0 to 4 of how good the view of the property was', 2 ],
                    'condition': [ 'An index from 1 to 5 on the condition of the apartment', 2 ],
                    'grade': [ 'An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design', 8 ],
                    'sqft_above': [ 'The square footage of the interior housing space that is above ground level', 2000 ],
                    'sqft_basement': [ 'The square footage of the interior housing space that is below ground level', 0 ],
                    'yr_built': [ 'The year the house was initially built', 1990 ],
                    'yr_renovated': [ 'The year of the house’s last renovation', 0 ],
                    'zipcode': [ 'What zipcode area the house is in', 98006 ],
                    'lat': [ 'Lattitude', 47.5 ],
                    'long': [ 'Longitude', -122.1 ],
                    'sqft_living15': [ 'The square footage of interior housing living space for the nearest 15 neighbors', 2000 ],
                    'sqft_lot15': [ 'The square footage of the land lots of the nearest 15 neighbors', 20000 ],
                    'year': [ 'Year', 2015 ]}

    return render_template( 'predict.html', options = description )

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

