import sqlite3

conn = sqlite3.connect('sqlite.db')
cursor = conn.cursor()
 
cursor.execute('''
CREATE TABLE IF NOT EXISTS classification_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text_input TEXT,
    input_length INTEGER,
    predicted_label TEXT,
    confidence REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    processing_time_ms INTEGER,
    client_ip TEXT,
    status TEXT
)
''')

conn.commit()
conn.close()

print("Database initialized successfully!")