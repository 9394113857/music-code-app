from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Song  # Import the User and Song models

routes = Blueprint('routes', __name__)

@routes.route('/')
def index():
    return render_template('index.html')

@routes.route('/songs')
@login_required
def songs():
    user_songs = current_user.songs
    return render_template('songs.html', songs=user_songs)

@routes.route('/add_song', methods=['GET', 'POST'])
@login_required
def add_song():
    if request.method == 'POST':
        title = request.form['title']
        artist = request.form['artist']
        new_song = Song(title=title, artist=artist, user_id=current_user.id)
        db.session.add(new_song)
        db.session.commit()
        flash('Song added successfully!', 'success')
        return redirect(url_for('routes.songs'))
    return render_template('add_song.html')

@routes.route('/delete_song/<int:song_id>', methods=['POST'])
@login_required
def delete_song(song_id):
    song = Song.query.get_or_404(song_id)
    if song.user != current_user:
        flash('You are not authorized to delete this song.', 'danger')
        return redirect(url_for('routes.songs'))
    db.session.delete(song)
    db.session.commit()
    flash('Song deleted successfully!', 'success')
    return redirect(url_for('routes.songs'))

@routes.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('routes.index'))
