# Structure for the page views
# December 11, 2020 ~5:51 p.m. to 


from sklearn.linear_model import LinearRegression
from flask import Flask, render_template, request
import altair as alt
#from altair import Chart
import pandas as pd
import json


options_selected = {}
options_list = {}
chart_list = {}
X = {}
intercept = 0
coefficient = 0
predicted_income = 0

Tract_Demographics = {'Year': [1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],
'Median Family Income Pct': [48,48,48,48,48,48,48,45.13,45.4,45.4,45.4,45.4,45.4,45.4,45.4,45.4,38.85,38.85,39.7,39.7,39.7,45.24],
'Median Family Income': [22176,23088,24288,25824,27504,28752,30432,28793,27512,28988,29238,29147,29646,31144,31144,30236,26224,26379,27552,28187,27433,33432], 
'Minority Population Pct': [89.58,89.58,89.58,89.58,89.58,89.58,89.58,90.44,90.44,90.44,90.44,90.44,90.44,90.44,90.44,90.44,84.26,84.26,84.26,84.26,84.26,77.09],
'Minority Population': [1848,1848,1848,1848,1848,1848,1848,1561,1561,1561,1561,1561,1561,1561,1561,1561,1215,1215,1215,1215,1215,1090],
'Owner Occupied Units': [319,319,319,319,319,319,319,215,215,215,215,215,215,215,215,215,199,199,199,199,199,231]
}

Test_Tract_Demographics = {
'Year': [2018,2019,2020],
'Median Family Income Pct': [45.24,45.24,45.24],
'Median Family Income': [34382,35242,38273],
'Minority Population Pct': [77.09,77.09,77.09],
'Minority Population': [1090,1090,1090],
'Owner Occupied Units': [231,231,231]
}
    
Demographics = pd.DataFrame(data=Tract_Demographics, columns=['Year','Median Family Income Pct','Median Family Income','Minority Population Pct','Minority Population','Owner Occupied Units'])
Test_Demographics = pd.DataFrame(data=Test_Tract_Demographics, columns=['Year','Median Family Income Pct','Median Family Income','Minority Population Pct','Minority Population','Owner Occupied Units'])

y=Demographics['Median Family Income']


# --- Flask App ---

oppzones_app = Flask(__name__)

@oppzones_app.route('/')
def home_view():
    # return "<h1>Hello, world!</h1>"
    chart = alt.Chart(Demographics).mark_line().encode(
    	x='Year',
	y='Minority Population',
    )
    created_chart = chart.save('chart.html')
    return render_template('home.html')

@oppzones_app.route('/result', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        options_selected = request.form.to_dict(flat=True)
        options_list=list(options_selected.values())
        X=Demographics[options_list]
        X_test=Test_Demographics[options_list]
        regressing = LinearRegression()
        regressing.fit(X,y)
        predicted_income = regressing.predict(X_test)
        predicted_income = predicted_income[0]
        intercept = regressing.intercept_
        coefficient = regressing.coef_      
        return render_template('input_selections.html', options_list=options_list, intercept=intercept, coefficient=coefficient, predicted_income=predicted_income)


if __name__ == "__main__":
    oppzones_app.run(debug=TRUE)
