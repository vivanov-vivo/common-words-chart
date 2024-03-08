# script.py
from flask import Flask, request, jsonify
# import sys
import os
from collections import Counter

# Create a Flask application instance
app = Flask(__name__)


def count_word_appearances(file_paths, num_common_words):
    word_count = Counter()

    # Iterate over each file
    for file_path in file_paths:
        # Open the file
        with open(file_path, 'r') as file:
            # Read each line
            for line in file:
                # Split the line into words
                words = line.split()
                # Count appearances of each word
                for word in words:
                    # Remove punctuation and convert to lowercase for consistency
                    word = word.strip('.,!?;:').lower()
                    # Update the count in the Counter
                    if word:
                        word_count[word] += 1

    # Get the most common words
    most_common_words = word_count.most_common(num_common_words)

    return most_common_words


@app.route('/', methods=['GET'])
def process_files():
    try:
        # use 
        files = os.environ.get('FILE_PATHS', ' ').split(',')
        num_of_words = int(os.environ.get('NUMOFWORDS', 4))
        # Get the most common words and print in json format
        return (count_word_appearances(files, num_of_words))

    except Exception as e:
        return jsonify({"error": str(e)}), 400


if __name__ == "__main__":
    # Run the Flask application
    app.run(debug=True, host='0.0.0.0', port=8080)