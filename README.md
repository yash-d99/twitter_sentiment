# Sentiment Analysis

## Overview
In this project I used the Twitter Emotion Classification Dataset
(Saravia et al., "CARER: Contextualized Affect Representations for Emotion Recognition," EMNLP 2018)
to train a Linear SVM Model. I then used the Reddit Developer API to allow a user to give a query
and see the breakdown of sentiments of the most recent posts from all subreddits via the post title and/or
the post content.

## Installation and Setup
In order to try this, first run
```bash
git clone https://github.com/yash-d99/twitter_sentiment.git
cd twitter_sentiment
pip install -r requirements.txt
```
In order to get the reddit keys and connect them -
1) Go to https://www.reddit.com/prefs/apps
2) Click "create another app"
3) Set redirect URI to http://localhost and fill out the other fields
4) Create the app
5) Copy the client ID (which is shown under the app name) and copy the client secret
6) Create a .env file in your cloned repository that looks like this (replace the placeholders with your info from above):
  REDDIT_CLIENT_ID= your_client_id 
  REDDIT_CLIENT_SECRET= your_client_secret 
  REDDIT_USER_AGENT=project_name

## Running the App
Once all the steps above have been complete, run 
```bash
python user_input.py
```
Fill in the information it prompts you and enjoy!



