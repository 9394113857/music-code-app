import os

def create_directory_structure(root_dir):
    # Create app directory
    app_dir = os.path.join(root_dir, 'app')
    if not os.path.exists(app_dir):
        os.makedirs(app_dir)  # Create the 'app' directory if it doesn't exist

    # Create app subdirectories
    subdirs = ['templates', 'static/css', 'static/js', 'uploads', 'instance', 'templates/playlists']
    for subdir in subdirs:
        subdir_path = os.path.join(app_dir, subdir)
        if not os.path.exists(subdir_path):
            os.makedirs(subdir_path)  # Create subdirectories inside 'app' if they don't exist

    # Create instance subdirectories
    instance_dir = os.path.join(root_dir, 'instance')
    if not os.path.exists(instance_dir):
        os.makedirs(instance_dir)  # Create the 'instance' directory if it doesn't exist

    # Create empty files
    files_to_create = [
        os.path.join(app_dir, '__init__.py'),
        os.path.join(app_dir, 'models.py'),
        os.path.join(app_dir, 'routes.py'),
        os.path.join(app_dir, 'forms.py'),
        os.path.join(app_dir, 'templates', 'base.html'),
        os.path.join(app_dir, 'templates', 'login.html'),
        os.path.join(app_dir, 'templates', 'signup.html'),
        os.path.join(app_dir, 'templates', 'home.html'),
        os.path.join(app_dir, 'templates', 'queue.html'),
        os.path.join(app_dir, 'templates', 'playlists', 'create_playlist.html'),
        os.path.join(app_dir, 'templates', 'playlists', 'view_playlist.html'),
        os.path.join(root_dir, 'static', 'css', 'styles.css'),
        os.path.join(root_dir, 'static', 'js', 'script.js'),
        os.path.join(root_dir, 'instance', 'config.py'),
        os.path.join(root_dir, 'run.py'),
        os.path.join(root_dir, 'requirements.txt')
    ]
    for file_path in files_to_create:
        if os.path.exists(file_path):
            choice = input(f"File '{file_path}' already exists. Do you want to overwrite it? (y/n): ").strip().lower()
            if choice != 'y':
                continue  # Skip this file if user chooses not to overwrite
        with open(file_path, 'w') as f:
            pass  # Create the file or overwrite it if it already exists

if __name__ == "__main__":
    create_directory_structure(os.getcwd())  # Call the function with the current root directory
