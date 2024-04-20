from flask import Flask, request, jsonify
import pandas as pd
from test_tapas_wtq import get_converted_answer  # Assuming your functions are in test_tapas_wtq.py

app = Flask(__name__)

# Store answers in a simple in-memory structure for demonstration purposes
answers = {}

@app.route('/ask', methods=['POST'])
def ask_question():
    """
    POST API to send the input question along with the dataset.
    Expects JSON with 'question' and 'dataset' (in CSV format as a string).
    """
    data = request.json
    question = data.get('question')
    dataset_csv = data.get('dataset')

    if not question or not dataset_csv:
        return jsonify({'error': 'Question and dataset are required.'}), 400

    # Convert dataset CSV string to a pandas DataFrame
    dataset = pd.read_csv(pd.compat.StringIO(dataset_csv))
    dataset_dict = dataset.to_dict(orient='records')

    # Get the converted answer
    answer = get_converted_answer(dataset_dict, question)

    # For simplicity, use the question as the key
    answers[question] = answer

    return jsonify({'message': 'Question processed successfully.'}), 200

@app.route('/answer', methods=['GET'])
def get_answer():
    """
    GET API to retrieve the answer.
    Expects 'question' as a query parameter.
    """
    question = request.args.get('question')

    if not question or question not in answers:
        return jsonify({'error': 'Answer not found for the given question.'}), 404

    answer = answers[question]
    return jsonify({'answer': answer}), 200

if __name__ == '__main__':
    app.run(debug=True)