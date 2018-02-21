from flask import Flask, request
from flask import render_template
from py_muffins_cupcakes import certified_or_denied

app = Flask(__name__)

@app.route('/')
def entry_page():
    return render_template('index.html')

@app.route('/predict_recipe/', methods=['GET', 'POST'])


def render_message():

    prevailing_wage_float = request.form['prevailing_wage']
 

    accept_rate_soc_float = request.form['accept_rate_soc']


    total_apps_soc_int = request.form['total_apps_soc']
  
                         

    accept_rate_emp_float = request.form['accept_rate_emp']
  

    total_apps_emp_int = request.form['total_apps_emp']


    yr_2011_int = request.form['yr_2011']


    yr_2012_int = request.form['yr_2012']


    yr_2013_int = request.form['yr_2013']
  
    
    yr_2014_int = request.form['yr_2014']
    
    yr_2015_int = request.form['yr_2015']
    
    yr_2016_int = request.form['yr_2016']
    
    full_time_int = request.form['full_time']
    

    message = certified_or_denied(prevailing_wage_float,
                            accept_rate_soc_float,
                            total_apps_soc_int,
                            accept_rate_emp_float,
                            total_apps_emp_int,
                            yr_2011_int,
                            yr_2012_int,
                            yr_2013_int,
                            yr_2014_int,
                            yr_2015_int,
                            yr_2016_int,
                            full_time_int)

    return render_template('index.html',
                           message=message)


if __name__ == '__main__':
    app.run(debug=True)