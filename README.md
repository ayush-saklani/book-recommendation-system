# Book Recommending System 
<!-- * A content based book recommending system using cosine similarity matrix
* Bag of word approach -->
*  **GitHub Link  - https://github.com/ayush-saklani/book-recommendation-system**

*  **Dataset Link (*used in this project*)- https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k**

*  **Streamlit documentation - https://docs.streamlit.io/library/api-reference**

*  **Dataset link - https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k**

*  **Alternate dataset link (*requires additional preprocessing and changes in model*) - https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks**

## **How to run this project** 
- Open JuPyter notebook and run the program 
- Now you will have 2 pickle files 
- Then you can run apptest.py 
- The command to run that is mentioned 1st the first line of code
- Make sure you have all the libraries intalled specially streamlit

#

# **Table of Contents**

<!-- # Take me to <a href="#pookie">pookie</a>
# <a name="RecommendationSystems">this is pookie</a> -->


1. **Recommendation Systems**
    - **Content based approach.**
    - **Collaborative based approach.**
    - **Hybrid model approach.**
2. **Books recommending system.**
3. **Database description**
4. **Data Preprocessing**
5. **Choosing a Recommendation Algorithm**
6. **Feature Extraction**
7. **Data Preprocessing II**
8. **Algorithm application**
    - **Euclidean Distance**
    - **Cosine Similarity**
9. **Deployment and User Interface**
10.** References**

## **1. Recommendation Systems**

A recommendation system is a type of software application or algorithm designed to provide personalized suggestions or recommendations to users. The primary goal of a recommendation system is to predict and present items (such as products, services, content, or information) that a user might find interesting, relevant, or useful, based on their preferences and behavior.

Recommendation systems are commonly used in various online platforms and services to enhance user experience, increase user engagement, and assist users in discovering new items of interest. There are several types of recommendation systems, with the three main categories being:

1. **Content-Based Recommendation:**
    - **Principle:** Recommends items like those the user has shown interest in before.
    - **Approach:** Analyzes the characteristics of items and the user's preferences.
    - **Example:** Recommending movies based on genres or books based on their content and genres.
2. **Collaborative Filtering:**
    - **Principle:** Recommends items based on the preferences and behaviors of similar users.
    - **Approach:** Utilizes user-item interaction data to identify patterns and make predictions and make recommendations to other users.
    - **Example:** Suggesting products that other users with similar tastes have liked or purchased.
3. **Hybrid Filtering:**
    - **Principle:** It is basically a combination of both the above methods.
    - **Approach:** It is a complex model which recommends products and services based on your history as well based on recommendation of users similar users like you.
    - **Example:** There are organizations that use this like Facebook which shows news which is important for you and for others also in your network and the same is used by LinkedIn also.

 

Recommendation systems often employ various techniques, such as machine learning algorithms, data mining, and statistical methods, to analyze user data and generate accurate predictions.



## **2. Book Recommendation System**

A book recommendation system is a type of recommendation system which recommends similar books to the reader based on his interest. The books recommendation system is used by online websites which provide eBooks like Google Books, Amazon Audibles, Amazon Kindle, Goodreads, etc.

In this project, we will be using the content-based filtering method to build a book recommending system.

## **3. Data Collection**

The dataset used in this project is sourced from Kaggle, the world's largest data science community. Database used in this project is of Goodreads, which is an American social cataloging website and a subsidiary of Amazon. 

## **4. Data Preprocessing**

Now in the books database, we have some extra columns which are not required for our task like number of pages and type of bound (hardbound/paperbound) etc. so we will firstly filter out the data fields which we need for aur model.


 

Now we will remove the redundancy and inconsistency in the database by removing all the rows will duplicate values and all the rows having any empty data field.

Now the data is filtered and is free from errors and redundancies.

## **5.Choosing a Recommendation Algorithm**

Now for the system to decide the similar books we will be using the “Bag of Words” model.

It is a text representation technique. It converts book titles, summaries, or reviews into a matrix of word frequencies. The “Bag of Words” model is applied by tokenizing text and enabling the identification of similar books based on word occurrences. This concise approach enhances the system's ability to recommend books by considering textual content in a straight


## **6. Feature Extraction**

In our case we will use the description of books, authors name, and genre of books to create a combined data field of tags that will be used for string matching.

We will make lists of genres of a book, each word from description, and authors name now having individual values we will remove all the spaces between the words to reduce ambiguity (e.g. J K Rowling -> JKRowling) and merge them to make a new data field called tags. The data is then converted into lowercase for best and efficient results.

As “Bag of Words” is a text representation technique so finally we will convert the tags data field into a string.

## **7. Data Preprocessing II**

Now we will do the text stripping by using the **porter stemmer algorithm**. It converts all the words into the root word or base word.

A stemming algorithm reduces the words “chocolates”, “chocolatey”, and “Choco” to the root word, “chocolate” and “retrieval”, “retrieved”, “retrieves” to the stem “retrieve”.

It will reduce the redundancy of tags as American and America were different tags before now, they are same. This will help us to find the result much quicker.


## **8. Algorithm application**

**CountVectorizer** is a tool in the Python scikit-learn library that converts text into vectors based on the frequency of words in the text. It breaks down text into words, removes special characters, and converts all words to lowercase. This will create vectors from the tags of all the books.

Now we have two methods to find similar book recommendations or calculate vector proximities.
1. **Euclidean Distance** - Measures the straight-line distance between two points in Euclidean space. Euclidean distance considers both magnitude and direction, making it sensitive to scale. Euclidean distance can be affected by the curse of dimensionality, especially in high-dimensional spaces.
2. **Cosine Similarity** - Measures the cosine of the angle between two vectors, providing a measure of orientation similarity. Cosine similarity is scale-invariant, emphasizing directional similarity. Cosine similarity often performs well in high-dimensional spaces.



Cosine similarity is commonly used in natural language processing, information retrieval, and recommendation systems so we will use that for this purpose.

Now by using the cosine similarity algorithm from sklearn python library we will get a 15000 X 15000 sized matrix that will have the value of similarity from each book to all books. The value of will be from the range [1,0] 1 from most similarity (itself) and zero for no similarity.

Now we can make a function that will return the 6 nearest vectors with least cosine distance from that book and show us.

## **9. Deployment and User Interface**

The from end for this application is made using a fantastic python library called streamlit that has the easiest and fastest way to create a front end for a python application it also provides hosting app deployment for free that can allow the application to be accessed by any device with internet browser.

## **10. References and Links**

 **GitHub Link  - https://github.com/ayush-saklani/book-recommendation-system**

**Dataset Link (*used in this project*)- https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k**

**Streamlit documentation - https://docs.streamlit.io/library/api-reference**

**Dataset link - https://www.kaggle.com/datasets/mdhamani/goodreads-books-100k**

**Alternate dataset link (*requires additional preprocessing*) - https://www.kaggle.com/datasets/jealousleopard/goodreadsbooks**