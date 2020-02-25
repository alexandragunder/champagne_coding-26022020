
from glob import glob
from joblib import load
from pathlib import Path
from voluptuous import Schema, Required, Any, Coerce, Invalid, MultipleInvalid

#
# Helper class definition of datamodel
#


class datamodel():
    def __init__( self ):
        self.metadata = {
            'bedrooms': {
                'desc': 'Number of bedrooms', 
	        'default': 2,
		'seq': 1,
		'v': Coerce( int )},
            'bathrooms': {
                'desc': 'Number of bathrooms (where .5 accounts for a room with a toilet but no shower)', 
                'default': 2,
                'seq': 2,
                'v': Any( Coerce( float ), Coerce( int ))},
            'sqft_living': {
                'desc': 'Square footage of the apartments interior living space', 
                'default': 2000,
                'seq': 3,
                'v': Coerce( int )},                
            'sqft_lot': {
                'desc': 'Square footage of the land space', 
                'default': 20000,
                'seq': 4,
                'v': Coerce( int )},
            'floors': {
                'desc': 'Number of floors (float or int)', 
                'default': 2,
                'seq': 5,
                'v': Any( Coerce( float ), Coerce( int ))},
            'waterfront': {
                'desc': 'Waterfront (0=no, 1=yes)', 
                'default': 0,
                'seq': 6,
                'v': Coerce( int )},
            'view': {
                'desc': 'An index from 0 to 4 of how good the view of the property was', 
                'default': 2,
                'seq': 7,
                'v': Coerce( int )},
            'condition': {
                'desc': 'An index from 1 to 5 on the condition of the apartment', 
                'default': 2,
                'seq': 8,
                'v': Coerce( int )},
            'grade': {
                'desc': 'An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design', 
                'default': 8,
                'seq': 9,
                'v': Coerce( int )},
            'sqft_above': {
                'desc': 'The square footage of the interior housing space that is above ground level', 
                'default': 2000,
                'seq': 10,
                'v': Coerce( int )},
            'sqft_basement': {
                'desc': 'The square footage of the interior housing space that is below ground level', 
                'default': 0,
                'seq': 11,
                'v': Coerce( int )},                
            'yr_built': {
                'desc': 'The year the house was initially built',
                'default': 1990,
                'seq': 12,
                'v': Coerce( int )},
            'yr_renovated': {
                'desc': 'The year of the house’s last renovation',
                'default': 0,
                'seq': 13,
                'v': Coerce( int )},
            'zipcode': {
                'desc': 'What zipcode area the house is in',
                'default': 98006,
                'seq': 14,
                'v': Coerce( int )},
            'lat': {
                'desc': 'Lattitude',
                'default': 47.5,
                'seq': 15,
                'v': Coerce( float )},
            'long': {
                'desc': 'Longitude',
                'default': -122.1,
                'seq': 16,
                'v': Coerce( float )},
            'sqft_living15': {
                'desc': 'The square footage of interior housing living space for the nearest 15 neighbors',
                'default': 2000,
                'seq': 17,
                'v': Coerce( int )},
            'sqft_lot15': {
                'desc': 'The square footage of the land lots of the nearest 15 neighbors',
                'default': 20000,
                'seq': 18,
                'v': Coerce( int )},
            'year': {
                'desc': 'Year',
                'default': 2015,
                'seq': 19,
                'v': Coerce( int )}
        }


    def schema( self ):
        """ Generate a voluptous schema definition """

        defs = {}
        for key, val in self.metadata.items():
            defs[ Required( key, default=val[ 'default' ])] = val[ 'v' ]
            
        return Schema( defs )


    def headers( self ):
        """ Generate array for passing correct parameter sequence to pandas """
        
        return sorted( self.metadata, key=self.metadata.get( 'seq' ))


    def description( self ):
        """ Generate structure usable for template engine """
        
        desc = {}
        for key, val in self.metadata.items():
            desc[ key ] = [ val[ 'desc' ], val[ 'default' ]]
            
        return desc


    def get_models( self ):
        """ Return list of model names """
        
        return [ Path(i).stem for i in glob( 'models/*.joblib' )]


    def load_model( self, name ):
        """ Load the datamodel that we trained and saved in the Jupyter notebook """
        
        return load( Path( 'models', '{}.joblib'.format( name )))
