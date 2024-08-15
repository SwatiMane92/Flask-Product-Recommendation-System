from flask import Flask, render_template, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics.pairwise import cosine_similarity
import os;

app = Flask(__name__)

# Get the directory of the current script
base_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to the Reviews.csv file
file_path = os.path.join(base_dir, 'Reviews.csv')

# Load the dataset
df = pd.read_csv(file_path)



# Preprocess data
df = df[['Id', 'ProductId', 'Score', 'Summary', 'Text']]
df = df.iloc[:10000, :]
ratings_df = df[['Id', 'ProductId', 'Score']]

# Create pivot table
pivot_table = ratings_df.pivot_table(index='Id', columns='ProductId', values='Score', fill_value=0)

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    if request.method == 'POST':
        user_id = int(request.form['user_id'])  # Get user ID from form
        k = 5  # Number of recommendations
        user_ratings = pivot_table.loc[user_id, :].values.reshape(1, -1)
        user_item_similarity = cosine_similarity(user_ratings, pivot_table)
        similar_item_indices = user_item_similarity.argsort()[0, ::-1][:k]

        recommendations = ratings_df[ratings_df['Id'].isin(similar_item_indices)].head(k)
    
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
