import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["DBS_NAME"] = 'on_the_record'
app.config["MONGO_URI"] = os.getenv("MONGO_URI")

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_records')
def get_records():
    return render_template("records.html", records=mongo.db.records.find())


@app.route('/add_record')
def add_record():
    return render_template("addrecord.html", genres=mongo.db.genres.find())


@app.route('/insert_record', methods=["POST"])
def insert_record():
    records = mongo.db.records
    records.insert_one(request.form.to_dict())
    return redirect(url_for('get_records'))


@app.route('/edit_record/<record_id>')
def edit_record(record_id):
    the_record = mongo.db.records.find_one({'_id': ObjectId(record_id)})
    all_genres = mongo.db.genres.find()
    return render_template('editrecord.html',
                           record=the_record, genres=all_genres)


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
                        'album_art':request.form.get('album_art')
                   })
    return redirect(url_for('get_records'))


@app.route('/delete_record/<record_id>')
def delete_record(record_id):
    mongo.db.records.remove({'_id': ObjectId(record_id)})
    return redirect(url_for('get_records'))


@app.route('/get_genres')
def get_genres():
    return render_template('genres.html',
                           genres=mongo.db.genres.find())


@app.route('/add_genre')
def add_genre():
    return render_template('addgenre.html', genres=mongo.db.genres.find())


@app.route('/insert_genre', methods=["POST"])
def insert_genre():
    genres = mongo.db.genres
    genres.insert_one(request.form.to_dict())
    return redirect(url_for('get_genres'))


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
