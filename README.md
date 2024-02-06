# **Book Recommending System**    <img src="https://upload.wikimedia.org/wikipedia/commons/0/0f/Stacked_books_icon.svg" width="60" height="60" align="left"/>

* **Dataset Link -** [Goodreads Books 100k](https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k) 📊
* **Alternate Dataset Link (*requires additional preprocessing and changes in model*) -** [GoodreadsBooks](https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks)📊

* **Streamlit Documentation -** [API Reference](https://docs.streamlit.io/library/api-reference)🧾

# **Coding Language and Library Used**
<p align="left">
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="60" height="60"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jupyter/jupyter-original-wordmark.svg" width="60" height="60"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/streamlit/streamlit-original.svg" width="60" height="60"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/numpy/numpy-plain-wordmark.svg"  width="60" height="60"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pandas/pandas-original-wordmark.svg" width="60" height="60"/>
<img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg" width="60" height="60"/>
</p>
          


# **How to run this project ?** 

1. Open Jupyter notebook and run the program.
2. After running, you will have 2 pickle files.
3. Run `apptest.py` using the command mentioned in the first line of code.
4. Ensure all required libraries, especially Streamlit, are installed *(use the latest pip libraries from [here](https://pypi.org/)).*


```code
pip install numpy
pip install pandas
pip install scikit-learn
pip install nltk
pip install pickle5
```
#

# **Table of Contents**

1. **[Recommendation Systems](#recommendation-systems)**
    1. ***[Content Based Recommendation](#content-based-recommendation)***
    2. ***[Collaborative Filtering](#collaborative-filtering)***
    3. ***[Hybrid Filtering](#hybrid-filtering)***
2. **[Data Preprocessing](#data-preprocessing)**
3. **[Choosing a Recommendation Algorithm](#choosing-a-recommendation-algorithm)**
4. **[Feature Extraction](#feature-extraction)**
5. **[Data Preprocessing II](#data-preprocessing-ii)**
6. **[Algorithm Application](#algorithm-application)**
   1. ***[Euclidean Distance](#euclidean-distance)***
   2. ***[Cosine Similarity](#cosine-similarity)***
7. **[Deployment and User Interface](#deployment-and-user-interface)**

# **Recommendation Systems**

A recommendation system predicts and presents items that a user might find relevant based on preferences and behavior.

1. ### **Content Based Recommendation**
   - **Principle:** Recommends items similar to what the user has shown interest in.
   - **Approach:** Analyzes item characteristics and user preferences.
   - **Example:** Recommending movies based on genres or books based on content and genres.
2. ### **Collaborative Filtering**
   - **Principle:** Recommends items based on the preferences and behaviors of similar users.
   - **Approach:** Utilizes user-item interaction data to identify patterns.
   - **Example:** Suggesting products liked or purchased by users with similar tastes.
3. ### **Hybrid Filtering**
   - **Principle:** A combination of content-based and collaborative filtering.
   - **Approach:**  Recommends items based on user history and similar users' recommendations.
   - **Example:** Facebook and LinkedIn use hybrid filtering for personalized content.
   
# **Data Preprocessing**

Filter unnecessary data fields and remove duplicates and empty values for clean data.

# Choosing a Recommendation Algorithm

Using the "Bag of Words" algorithm, a text representation technique converting titles, summaries, or reviews into a matrix of word frequencies.

# Feature Extraction

Use book descriptions, authors' names, and genres to create a combined data field of tags for string matching.

# Data Preprocessing II

Apply the Porter Stemmer algorithm for text stripping, reducing words to their root form and minimizing redundancy.

# Algorithm Application

Utilize CountVectorizer to convert text into vectors based on word frequency, creating vectors from tags of all books.

1. ### **Euclidean Distance**
   - Measures straight-line distance between two points in Euclidean space.
   - Sensitive to scale and affected by the curse of dimensionality.
2. ### **Cosine Similarity**
   - Measures cosine of the angle between two vectors.
   - Scale-invariant and suitable for high-dimensional spaces.

Apply cosine similarity algorithm to get a similarity matrix. Create a function to return 6 nearest vectors with the least cosine distance.

# Deployment and User Interface

Use Streamlit for the frontend, providing the easiest way to create a user interface for the Python application. Streamlit also offers free hosting for easy accessibility on any device with an internet browser.


# **Keep Coding, Keep Smiling!, Have Fun!** 💻🚀