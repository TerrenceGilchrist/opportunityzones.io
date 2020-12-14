# Structure for the page views
# December 11, 2020 ~5:51 p.m. to 



from flask import Flask, render_template, request
import pandas as pd

oppzones_app = Flask(__name__)

options_selected = {}
options_list = {}
chart_list = {}
X = {}
intercept = 0
coefficient = 0

Tract_Demographics = {
'Year': [2020,2019,2018,2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001],
'Median Family Income Pct': [45.24,45.24,45.24,45.24,39.7,39.7,39.7,38.85,38.85,45.4,45.4,45.4,45.4,45.4,45.4,45.4,45.4,45.13,48,48],
'Median Family Income': [38273,35242,34382,33432,27433,28187,27552,26379,26224,30236,31144,31144,29646,29147,29238,28988,27512,28793,30432,28752],
'Minority Population Pct': [77.09,77.09,77.09,77.09,84.26,84.26,84.26,84.26,84.26,90.44,90.44,90.44,90.44,90.44,90.44,90.44,90.44,90.44,89.58,89.58],
'Minority Population': [1090,1090,1090,1090,1215,1215,1215,1215,1215,1561,1561,1561,1561,1561,1561,1561,1561,1561,1848,1848],
'Owner Occupied Units': [231,231,231,231,199,199,199,199,199,215,215,215,215,215,215,215,215,215,319,319]
}

Demographics = pd.DataFrame(data=Tract_Demographics, columns=['Year','Median Family Income Pct','Median Family Income','Minority Population Pct','Minority Population','Owner Occupied Units'])

y=Demographics['Median Family Income']

@oppzones_app.route('/')
def home_view():
    # return "<h1>Hello, world!</h1>"
    return render_template('home.html')

@oppzones_app.route('/result', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        options_selected = request.form.to_dict(flat=True)
        options_list=list(options_selected.values())
        X=Demographics['Minority Population']
        return render_template('input_selections.html', options_selected=options_selected, options_list=options_list, intercept=intercept, y=y, X=X)


if __name__ == "__main__":
    oppzones_app.run(debug=TRUE)
