# Hotel Stay! Sentiment Analysis Application

## Table of Contents

1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [AWS Comprehend Integration](#aws-comprehend-integration)
4. [Key Learnings](#key-learnings)
5. [Deployment](#deployment)
6. [References](#references)

## Project Overview

This project is a Python Flask-based web application integrated with AWS Comprehend to perform sentiment analysis on customer feedback for the Hotel Stay! application. The application collects feedback from users, analyzes the sentiment using AWS Comprehend, and displays the results in an intuitive interface.

## System Architecture

1. **Frontend**: Flask-based web application that serves HTML pages and handles user interactions.
2. **Backend**: Python Flask application that processes feedback, performs sentiment analysis using AWS Comprehend, and displays results.
3. **AWS Comprehend**: AWS service used to analyze the sentiment of the customer feedback.
4. **Data Flow**:
   - User submits feedback through the Flask application.
   - Feedback is sent to AWS Comprehend for sentiment analysis.
   - Results are processed and displayed on the results page.

## AWS Comprehend Integration

AWS Comprehend is a natural language processing (NLP) service that uses machine learning to uncover insights from text. It helps in performing sentiment analysis by determining the sentiment of the text provided.

### Usage

1. **Setup AWS Comprehend**:
   - Create an AWS account if you don't have one.
   - Navigate to AWS Comprehend in the AWS Management Console.
   - Make sure you have the necessary IAM permissions to use Comprehend.

2. **Code Integration**:
   - Install the AWS SDK for Python (Boto3):
     ```bash
     pip install boto3
     ```
   - Use the following code to analyze sentiment:
     ```python
     import boto3
     from botocore.exceptions import BotoCoreError, ClientError

     def analyze_sentiment(text):
         comprehend = boto3.client('comprehend', region_name='us-east-1')
         try:
             response = comprehend.detect_sentiment(Text=text, LanguageCode='en')
             sentiment = response['Sentiment']
             return sentiment.upper()
         except (BotoCoreError, ClientError) as error:
             print(f"Error analyzing sentiment: {error}")
             return 'Neutral'
     ```

3. **Application Code**:
   - The Flask application sends the feedback to AWS Comprehend and processes the results to update the sentiment percentages and negative comments. The code files are provide accordingly.

## Key Learnings

- **AWS Comprehend**: Understanding how to integrate AWS Comprehend with a Flask application for sentiment analysis.
- **Flask Web Development**: Building a web application using Flask, handling user feedback, and displaying results.
- **Data Visualization**: Presenting sentiment analysis results in a user-friendly manner.

## Deployment

### S3 Static Website

1. **Create an S3 Bucket**:
   - Navigate to the S3 console.
   - Create a new bucket and enable static website hosting.

2. **Upload Files**:
   - Upload your HTML, CSS, and JavaScript files to the S3 bucket.

3. **Configure Bucket Policy**:
   - Set the bucket policy to allow public access.

4. **Access Your Website**:
   - Use the S3 bucket endpoint to access your deployed application.

### Amazon Elastic Beanstalk

1. **Create an Elastic Beanstalk Application**:
   - Navigate to the Elastic Beanstalk console.
   - Create a new application and environment.

2. **Deploy Your Application**:
   - Upload your Flask application code and deploy it.

3. **Monitor and Manage**:
   - Use the Elastic Beanstalk console to monitor application health and manage deployments.

## References

- Check my [Broadcast](https://drive.google.com/file/d/1phKkabBhYRZ3BZBSjgWH-T8Yhvtq7ZUK/view?usp=sharing)

- [AWS Comprehend Documentation](https://docs.aws.amazon.com/comprehend/latest/dg/what-is-comprehend.html)
- [AWS Comprehend Image](https://your-image-url-here)
- [Broadcast Video Link](https://your-broadcast-video-link-here)
