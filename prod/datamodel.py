
class datamodel():

	self _init_():
		self.meta = { 'bedrooms': { desc: 'Number of bedrooms', 
		                            default: 2,
		                            seq: 1,
		                            v: Coerce( int )},
                    'bathrooms': { desc: 'Number of bathrooms (where .5 accounts for a room with a toilet but no shower)', 
                    default: 2 
                    seq: 2,
                    v: Any( Coerce( float ), Coerce( int ))},
                    'sqft_living': { desc: 'Square footage of the apartments interior living space', 
                    default: 2000,
                    seq: 3,
                    v: Coerce( int )},

                    'sqft_lot': { desc: 'Square footage of the land space', 
                    default: 20000,
                    seq: 4,
                    v: Coerce( int )},

                    'floors': { desc: 'Number of floors (float or int)', 
                    default: 2,
                    seq: 5,
                    v: Any( Coerce( float ), Coerce( int ))},

                    'waterfront': { desc: 'Waterfront (0=no, 1=yes)', 
                    default: 0,
                    seq: 6,
                    v: Coerce( int )},

                    'view': { desc: 'An index from 0 to 4 of how good the view of the property was', 
                    default: 2,
                    seq: 7,
                    v: Coerce( int )},

                    'condition': { desc: 'An index from 1 to 5 on the condition of the apartment', 
                    default: 2,
                    seq: 8,
                    v: Coerce( int )},

                    'grade': { desc: 'An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design', 
                    default: 8,
                    seq: 9,
                    v: Coerce( int )},

                    'sqft_above': { desc: 'The square footage of the interior housing space that is above ground level', 
                    default: 2000,
                    seq: 10,
                    v: Coerce( int )},

                    'sqft_basement': { desc: 'The square footage of the interior housing space that is below ground level', 
                    default: 0,
                    seq: 11,
                    v: Coerce( int )},
                    'yr_built': [ 'The year the house was initially built', 1990 ],
                    'yr_renovated': [ 'The year of the house’s last renovation', 0 ],
                    'zipcode': [ 'What zipcode area the house is in', 98006 ],
                    'lat': [ 'Lattitude', 47.5 ],
                    'long': [ 'Longitude', -122.1 ],
                    'sqft_living15': [ 'The square footage of interior housing living space for the nearest 15 neighbors', 2000 ],
                    'sqft_lot15': [ 'The square footage of the land lots of the nearest 15 neighbors', 20000 ],
                    'year': [ 'Year', 2015 ]}


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

    headers = [ 'bedrooms', 'bathrooms', 'sqft_living', 'sqft_lot',
                'floors', 'waterfront', 'view', 'condition', 'grade',
                'sqft_above', 'sqft_basement', 'yr_built',
                'yr_renovated', 'zipcode', 'lat', 'long',
                'sqft_living15', 'sqft_lot15', 'year']
