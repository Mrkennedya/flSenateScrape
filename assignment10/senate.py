from flask import Flask, render_template, url_for
from modules import convert_to_dict
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm

app = Flask(__name__)

#create new secret key
app.config['SECRET_KEY'] = '7A8wUjBFvv96DY8rcXZpTnUjGyjH6bh9'

Bootstrap(app)

senators_list = convert_to_dict("Florida_State_Senators.csv")

@app.route('/')
def index():
    district_list = []
    name_list = []
    # List will append the Unique ID – district – and the senator's name
    for senator in senators_list:
        district_list.append(senator['District'])
        name_list.append(senator['Senator'])
        # zip() is a built-in function that combines lists
        # creating a new list of tuples
    pairs_list = zip(district_list, name_list)
    # sort the list by the first item in each tuple, the number
    # pairs_list_sorted = sorted(pairs_list, key=lambda tup: int(tup[0]))
    return render_template('index.html', pairs=pairs_list, the_title="State Senator List")



@app.route('/senator/<num>')
def detail(num):
    for senator in senators_list:
        if senator['District'] == num:
            senator_dict = senator
            break
    return render_template('senator.html', senator=senator_dict, the_title=senator_dict['Senator'])
# your code here



# keep this as is
if __name__ == '__main__':
    app.run(debug=True)
