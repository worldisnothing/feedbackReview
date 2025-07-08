from flask import Flask, request, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DB_PATH = 'reviews.db'

feedback_category = {
    'positive': ['хорош', 'люблю'],
    'negative': ['плохо', 'ненавиж']
}
default_category = 'neutral'


def init_db():
    '''
    Init DB
    '''
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                text TEXT NOT NULL,
                sentiment TEXT NOT NULL,
                created_at TEXT NOT NULL
            );
        ''')
        conn.commit()


def analyze_sentiment(text: str) -> str:
    '''
    Feedback analyzer
    :param text: feedback text for analyzing
    :type text: str
    :return: feedback category
    :rtype: str
    '''
    text = text.lower()
    for sentiment, keywords in feedback_category.items():
        for kw in keywords:
            if kw in text:
                return sentiment
    return default_category


@app.route('/reviews', methods=['POST'])
def create_review():
    '''
    Analyze and create feedback with category in DB table reviews
    :return:
    '''
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'Missing \"text\" field'}), 400

    text = data['text']
    sentiment = analyze_sentiment(text)
    created_at = datetime.utcnow().isoformat()

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO reviews (text, sentiment, created_at) VALUES (?, ?, ?)',
            (text, sentiment, created_at)
        )
        review_id = cursor.lastrowid

    return jsonify({
        'id': review_id,
        'text': text,
        'sentiment': sentiment,
        'created_at': created_at
    }), 201


@app.route('/reviews', methods=['GET'])
def get_reviews():
    '''
    Get all or specified in query items from DB table reviews
    '''
    sentiment_filter = request.args.get('sentiment')
    query = 'SELECT id, text, sentiment, created_at FROM reviews'
    params = ()

    if sentiment_filter:
        query += ' WHERE sentiment = ?'
        params = (sentiment_filter,)

    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(query, params)
        rows = cursor.fetchall()

    reviews = [
        {'id': row[0], 'text': row[1], 'sentiment': row[2], 'created_at': row[3]}
        for row in rows
    ]
    return jsonify(reviews)


if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5555)
