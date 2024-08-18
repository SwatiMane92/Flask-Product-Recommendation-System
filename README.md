# Product Recommendation System (Flask)

This project is a Flask-based web application that provides product recommendations using a recommendation algorithm. The system utilizes TF-IDF vectorization and K-Means clustering to analyze user reviews and generate recommendations.

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Dataset](#dataset)
- [Features](#features)
- [Usage](#usage)
- [Results](#results)
- [License](#license)

## Overview

The Product Recommendation System is a web application developed using Flask. It recommends products based on user ratings and reviews. The system leverages K-Means clustering and cosine similarity to provide personalized recommendations.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/product-recommendation-system-flask.git
   cd product-recommendation-system-flask
   ```

2. Install the required packages:

   ```bash
   pip install flask pandas scikit-learn
   ```

3. Ensure the `Reviews.csv` dataset is in the project directory.

## Dataset

The dataset used for this project is `Reviews.csv`, which includes user reviews and ratings of various products. The relevant columns utilized are:

- `Id`: The unique identifier of the user.
- `ProductId`: The unique identifier of the product.
- `Score`: The rating given by the user to the product.
- `Summary`: Summary of the review (used for potential future enhancements).
- `Text`: Detailed text of the review (used for potential future enhancements).

## Features

- **Web Interface**: Allows users to enter their ID and get product recommendations.
- **Data Preprocessing**: Handles missing values and processes the dataset.
- **Cosine Similarity**: Computes similarity between user ratings and products.
- **K-Means Clustering**: (Optional) Clusters users for enhanced recommendation accuracy.

## Usage

1. **Run the Flask Application**:

   ```bash
   python app.py
   ```

2. **Access the Web Interface**:

   Open your web browser and go to `http://localhost:5000`.

3. **Get Recommendations**:

   - Enter a user ID in the input field.
   - Click on "Get Recommendations" to see the top product recommendations.

## Results

- **Recommendations**: Provides a list of recommended products based on the entered user ID.
- **UI**: Simple web interface to interact with the recommendation system.
