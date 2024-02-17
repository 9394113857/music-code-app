import sqlite3
from prettytable import PrettyTable

# Function to create empty tables in the SQLite database
def create_empty_tables():
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('music_database.db')
        cursor = conn.cursor()

        # Define SQL queries to create tables
        queries = [
            """
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Songs (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                artist TEXT NOT NULL,
                album TEXT,
                genre TEXT,
                filepath TEXT NOT NULL
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS Playlists (
                id INTEGER PRIMARY KEY,
                user_id INTEGER,
                name TEXT NOT NULL,
                FOREIGN KEY (user_id) REFERENCES Users(id)
            )
            """,
            """
            CREATE TABLE IF NOT EXISTS PlaylistSongs (
                playlist_id INTEGER,
                song_id INTEGER,
                FOREIGN KEY (playlist_id) REFERENCES Playlists(id),
                FOREIGN KEY (song_id) REFERENCES Songs(id),
                PRIMARY KEY (playlist_id, song_id)
            )
            """
        ]

        # Execute each query to create tables
        for query in queries:
            cursor.execute(query)

        # Commit changes and close connection
        conn.commit()
        conn.close()

        print("All tables are created successfully!")

    except sqlite3.Error as e:
        print("Error:", e)

# Function to show the structure of a table
def show_table_structure(table_name):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect('music_database.db')
        cursor = conn.cursor()

        # Get table structure
        cursor.execute(f"PRAGMA table_info({table_name})")
        table_info = cursor.fetchall()

        # Create a PrettyTable
        table = PrettyTable()
        table.field_names = ["SNo", "Column Name", "Data Type"]

        # Add rows to the PrettyTable
        for index, column in enumerate(table_info, start=1):
            table.add_row([index, column[1], column[2]])

        # Print the PrettyTable
        print(f"\nTable: {table_name}")
        print(table)

        # Close connection
        conn.close()

    except sqlite3.Error as e:
        print("Error:", e)

if __name__ == "__main__":
    create_empty_tables()

    # Prompt user to view table structure
    while True:
        choice = input("\nDo you want to view the structure of any table? (y/n): ").strip().lower()
        if choice != 'y':
            break

        table_name = input("Enter the name of the table (e.g., Users, Songs, Playlists, PlaylistSongs): ").strip()
        show_table_structure(table_name)

    print("\nExiting the program. Have a nice day!")
