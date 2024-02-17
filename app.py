from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///music_database.db'

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

# Define User model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

# Define Song model
class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('songs', lazy=True))

# Initialize Login Manager
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    # return render_template('index.html')
    return "Welcome!"

@app.route('/songs')
@login_required
def songs():
    user_songs = current_user.songs
    return render_template('songs.html', songs=user_songs)

@app.route('/add_song', methods=['GET', 'POST'])
@login_required
def add_song():
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        new_song = Song(title=title, artist=artist, user_id=current_user.id)
        db.session.add(new_song)
        db.session.commit()
        flash('Song added successfully!', 'success')
        return redirect(url_for('songs'))
    return render_template('add_song.html')

@app.route('/delete_song/<int:song_id>', methods=['POST'])
@login_required
def delete_song(song_id):
    song = Song.query.get_or_404(song_id)
    if song.user != current_user:
        flash('You are not authorized to delete this song.', 'danger')
        return redirect(url_for('songs'))
    db.session.delete(song)
    db.session.commit()
    flash('Song deleted successfully!', 'success')
    return redirect(url_for('songs'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

if __name__ == "__main__":
    with app.app_context():
        db.create_all() 
    app.run(debug=True) 
