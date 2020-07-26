import os
from flask import Flask, render_template, redirect, request, url_for
from flask import session, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["DBS_NAME"] = 'on_the_record'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
app.secret_key = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

# RENDER WELCOME PAGE ON START UP


@app.route('/')
def index():
    if 'username' in session:
        return redirect('get_records')

    return render_template('welcome.html')

# RENDER LOG IN PAGE


@app.route('/login_page')
def login_page():
    return render_template('login.html')

# CHECK USER LOGIN CREDENTIALS


@app.route('/login', methods=['POST'])
def login():
    users = mongo.db.users
    login_user = users.find_one({'username': request.form['username']})

    if login_user:
        if bcrypt.hashpw(request.form['password'].encode('utf-8'),
                         login_user['password']) == login_user['password']:
            session['username'] = request.form['username']
            return redirect(url_for('get_records'))
    # SEND NEW USER TO REGISTER
    error_message = ('Invalid username or password')
    
    return render_template('login.html')

# REGISTER NEW USER


@app.route('/register', methods=['POST', 'GET'])
def register():
    if request.method == 'POST':
        users = mongo.db.users
        existing_user = users.find_one({'username': request.form['username']})

        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['password'].encode('utf-8'),
                                     bcrypt.gensalt())
            users.insert({'first_name': request.form['first_name'],
                          'last_name': request.form['last_name'],
                          'username': request.form['username'],
                          'email': request.form['email'],
                          'password': hashpass
                          })
            session['username'] = request.form['username']
            return redirect(url_for('get_records'))

        return 'That username already exists!'

    return render_template('register.html')

# LOG OUT USER


@app.route('/logout')
def logout():
    session.clear()
    flash('You were logged out!')
    return render_template('welcome.html')

# SHOW RECORDS IN COLLECTION


@app.route('/get_records')
def get_records():
    return render_template("records.html", records=mongo.db.records.find())

# RENDER PAGE TO ADD RECORD TO COLLECTION


@app.route('/add_record')
def add_record():
    return render_template("addrecord.html", genres=mongo.db.genres.find())

# ACCEPT FORM INPUTS AND INSERT RECORD


@app.route('/insert_record', methods=["POST"])
def insert_record():
    records = mongo.db.records
    records.insert_one(request.form.to_dict())
    return redirect(url_for('get_records'))

# RENDER PAGE TO EDIT RECORD IN THE COLLECTION


@app.route('/edit_record/<record_id>')
def edit_record(record_id):
    the_record = mongo.db.records.find_one({'_id': ObjectId(record_id)})
    all_genres = mongo.db.genres.find()
    return render_template('editrecord.html',
                           record=the_record, genres=all_genres)

# ACCEPT FORM INPUTS AND UPDATE RECORD


@app.route('/update_record/<record_id>', methods=["POST"])
def update_record(record_id):
    records = mongo.db.records
    records.update({'_id': ObjectId(record_id)},
                   {
                        'record_title': request.form.get('record_title'),
                        'artist_name': request.form.get('artist_name'),
                        'label': request.form.get('label'),
                        'year': request.form.get('year'),
                        'genre': request.form.get('genre'),
                        'get_it_here': request.form.get('get_it_here'),
                        'star_rating': request.form.get('star_rating'),
                        'review': request.form.get('review'),
                        'album_art': request.form.get('album_art')
                   })
    return redirect(url_for('get_records'))

# REMOVE SELECTED RECORD


@app.route('/delete_record/<record_id>')
def delete_record(record_id):
    mongo.db.records.remove({'_id': ObjectId(record_id)})
    return redirect(url_for('get_records'))

# SHOW ALL GENRES IN COLLECTION


@app.route('/get_genres')
def get_genres():
    return render_template('genres.html',
                           genres=mongo.db.genres.find())

# RENDER PAGE FOR ADDING GENRE


@app.route('/add_genre')
def add_genre():
    return render_template('addgenre.html', genres=mongo.db.genres.find())

# ACCEPT FORM INPUTS AND INSERT GENRE


@app.route('/insert_genre', methods=["POST"])
def insert_genre():
    genres = mongo.db.genres
    genres.insert_one(request.form.to_dict())
    return redirect(url_for('get_genres'))

# SHOW ALL RECORDS OF A SELECTED GENRE


@app.route('/get_records_in_genre/<genre>')
def get_records_in_genre(genre):
    genre = mongo.db.genres.find({'genre_name': genre})
    return render_template('genre.html',
                           genres=genre,
                           records=mongo.db.records.find())


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
