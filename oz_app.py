# Structure for the page views
# December 11, 2020 ~5:51 p.m. to 


from sklearn.linear_model import LinearRegression
from flask import Flask, render_template, request
import pandas as pd

oppzones_app = Flask(__name__)

options_selected = {}
options_list = {}
chart_list = {}
X = {}
intercept = 0
coefficient = 0
predicted_income = 0

Tract_Demographics = {
'Year': [2017,2016,2015,2014,2013,2012,2011,2010,2009,2008,2007,2006,2005,2004,2003,2002,2001],
'Median Family Income Pct': [45.24,39.7,39.7,39.7,38.85,38.85,45.4,45.4,45.4,45.4,45.4,45.4,45.4,45.4,45.13,48,48],
'Median Family Income': [33432,27433,28187,27552,26379,26224,30236,31144,31144,29646,29147,29238,28988,27512,28793,30432,28752],
'Minority Population Pct': [77.09,84.26,84.26,84.26,84.26,84.26,90.44,90.44,90.44,90.44,90.44,90.44,90.44,90.44,90.44,89.58,89.58],
'Minority Population': [1090,1215,1215,1215,1215,1215,1561,1561,1561,1561,1561,1561,1561,1561,1561,1848,1848],
'Owner Occupied Units': [231,199,199,199,199,199,215,215,215,215,215,215,215,215,215,319,319]
}

Test_Tract_Demographics = {
'Year': [2020,2019,2018],
'Median Family Income Pct': [45.24,45.24,45.24],
'Median Family Income': [38273,35242,34382],
'Minority Population Pct': [77.09,77.09,77.09],
'Minority Population': [1090,1090,1090],
'Owner Occupied Units': [231,231,231]
}

Tract_Demographics_c = {'Year': [2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017],
'Median Family Income Pct': [48,48,45.13,45.4,45.4,45.4,45.4,45.4,45.4,45.4,45.4,38.85,38.85,39.7,39.7,39.7,45.24],
'Median Family Income': [28752,30432,28793,27512,28988,29238,29147,29646,31144,31144,30236,26224,26379,27552,28187,27433,33432], 
'Minority Population Pct': [89.58,89.58,90.44,90.44,90.44,90.44,90.44,90.44,90.44,90.44,90.44,84.26,84.26,84.26,84.26,84.26,77.09],
'Minority Population': [1848,1848,1561,1561,1561,1561,1561,1561,1561,1561,1561,1215,1215,1215,1215,1215,1090],
'Owner Occupied Units': [319,319,215,215,215,215,215,215,215,215,215,199,199,199,199,199,231]
}

Test_Tract_Demographics_c = {
'Year': [2018,2019,2020],
'Median Family Income Pct': [45.24,45.24,45.24],
'Median Family Income': [34382,35242,38273],
'Minority Population Pct': [77.09,77.09,77.09],
'Minority Population': [1090,1090,1090],
'Owner Occupied Units': [231,231,231]
}
    
Demographics = pd.DataFrame(data=Tract_Demographics, columns=['Year','Median Family Income Pct','Median Family Income','Minority Population Pct','Minority Population','Owner Occupied Units'])
Test_Demographics = pd.DataFrame(data=Test_Tract_Demographics, columns=['Year','Median Family Income Pct','Median Family Income','Minority Population Pct','Minority Population','Owner Occupied Units'])

Demographics_c = pd.DataFrame(data=Tract_Demographics_c, columns=['Year','Median Family Income Pct','Median Family Income','Minority Population Pct','Minority Population','Owner Occupied Units'])
Test_Demographics_c = pd.DataFrame(data=Test_Tract_Demographics_c, columns=['Year','Median Family Income Pct','Median Family Income','Minority Population Pct','Minority Population','Owner Occupied Units'])


y=Demographics['Median Family Income']
yc=Demographics_c['Median Family Income']

@oppzones_app.route('/')
def home_view():
    # return "<h1>Hello, world!</h1>"
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
        Xc=Demographics_c[options_list]
        X_testc=Test_Demographics_c[options_list]
        regressingc = LinearRegression()
        regressingc.fit(Xc,yc)
        predicted_incomec = regressingc.predict(X_testc)
        predicted_incomec = predicted_incomec[0]
        interceptc = regressingc.intercept_
        coefficientc = regressingc.coef_
        #intercept = round(intercept,2)
        #coefficient = round(coefficient,3)
        return render_template('input_selections.html', options_list=options_list, intercept=intercept, coefficient=coefficient, predicted_income=predicted_income, interceptc=interceptc, coefficientc=coefficientc, predicted_incomec=predicted_incomec)


if __name__ == "__main__":
    oppzones_app.run(debug=TRUE)
