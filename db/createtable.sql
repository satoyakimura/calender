CREATE TABLE IF NOT EXISTS users(
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(255) UNIQUE,
    hashed_password VARCHAR(255),
    bonus INTEGER,
    login TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    logout TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS schedules(
    schedule_id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(user_id),
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    title VARCHAR(255),
    content TEXT
    );

CREATE TABLE IF NOT EXISTS friends (
    user_id_1 INTEGER REFERENCES users(user_id),
    user_id_2 INTEGER REFERENCES users(user_id),
    UNIQUE (user_id_1, user_id_2)
    );

CREATE TABLE IF NOT EXISTS message (
    message_id SERIAL PRIMARY KEY,
    sender_id INTEGER REFERENCES users(user_id),
    receiver_id INTEGER REFERENCES users(user_id),
    content TEXT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
