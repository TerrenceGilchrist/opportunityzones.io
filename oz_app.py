# Structure for the page views
# December 11, 2020 ~5:51 p.m. to 

from flask import Flask, render_template, request
oz_app = Flask(__name__)

@oz_app.route('/home/', methods=['GET','POST'])
        return render_template('input_selections.html')
        
#@oz_app.route('/result/')
#def index():
 #   if request.method == 'POST':
 #       options_selected = request.form.get('regressor')
 #       print(options_selected)

if name == "__main__":
  oz_app.run(debug=TRUE)
