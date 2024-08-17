from flask import Flask, render_template, request, redirect, url_for
import boto3
from botocore.exceptions import BotoCoreError, ClientError

app = Flask(__name__)

# Initialize feedback data
feedback_data = {'Positive': 0, 'Neutral': 0, 'Negative': 0, 'negative_comments': []}

@app.route('/')
def index():
    return redirect(url_for('survey_progress', question_number=1))

@app.route('/progress/<int:question_number>')
def survey_progress(question_number):
    if question_number > 10:
        return redirect(url_for('results'))
    return render_template('survey.html', question_number=question_number)

@app.route('/submit', methods=['POST'])
def submit_feedback():
    feedback = request.form.get('feedback')
    if feedback:
        sentiment = analyze_sentiment(feedback)
        # Map the sentiment values to match feedback_data keys
        sentiment_map = {
            'POSITIVE': 'Positive',
            'NEUTRAL': 'Neutral',
            'NEGATIVE': 'Negative'
        }
        sentiment = sentiment_map.get(sentiment.upper(), 'Neutral')
        print(f"Feedback: {feedback} | Sentiment: {sentiment}")  # Debug print
        if sentiment in feedback_data:
            feedback_data[sentiment] += 1
            if sentiment == 'Negative':
                feedback_data['negative_comments'].append(feedback)
        else:
            print(f"Unexpected sentiment value: {sentiment}")  # Debug print
    question_number = int(request.form.get('question_number', 1))
    return redirect(url_for('survey_progress', question_number=question_number + 1))

@app.route('/results')
def results():
    total_feedback = feedback_data['Positive'] + feedback_data['Neutral'] + feedback_data['Negative']
    print(f"Total Feedback Count: {total_feedback}")  # Debug print
    sentiment_percentages = {
        'Positive': (feedback_data['Positive'] / total_feedback * 100) if total_feedback > 0 else 0,
        'Neutral': (feedback_data['Neutral'] / total_feedback * 100) if total_feedback > 0 else 0,
        'Negative': (feedback_data['Negative'] / total_feedback * 100) if total_feedback > 0 else 0
    }
    print(f"Sentiment Percentages: {sentiment_percentages}")  # Debug print
    print(f"Negative Comments: {feedback_data['negative_comments']}")  # Debug print

    # Pass negative comments to the template
    return render_template('results.html', sentiment_percentages=sentiment_percentages, negative_comments=feedback_data['negative_comments'])

def analyze_sentiment(text):
    comprehend = boto3.client('comprehend', region_name='us-east-1')
    try:
        response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
        sentiment = response['Sentiment']
        # Normalize sentiment value to match application keys
        return sentiment.upper()
    except (BotoCoreError, ClientError) as error:
        # Log the error or handle it accordingly
        print(f"Error analyzing sentiment: {error}")
        return 'Neutral'  # Default to Neutral if there's an error

@app.errorhandler(Exception)
def handle_exception(e):
    return render_template('error.html', error_message=str(e)), 500

if __name__ == '__main__':
    app.run(debug=True)
