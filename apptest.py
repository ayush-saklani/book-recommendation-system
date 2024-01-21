# streamlit run apptest.py
import pickle
import streamlit as st


def recommend_me_a_book(book):
    index = books[books['title'] == book].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_book_name = []
    recommended_book_cover = [] 
    recommended_isbn = []
    recommended_link = []
    # author  desc  genre  img  isbn  link  pages  rating  reviews  title  totalratings
    
    for i in distances[1:7]:
        isbn = books.iloc[i[0]].isbn
        recommended_book_cover.append(books.iloc[i[0]].img)
        recommended_book_name.append(books.iloc[i[0]].title)
        recommended_isbn.append(books.iloc[i[0]].isbn)
        recommended_link.append(books.iloc[i[0]].link)

    return recommended_book_cover,recommended_book_name,recommended_isbn,recommended_link

st.set_page_config(layout="wide")
st.title('Book Recommending System')
st.caption('For all you bookworms')
books = pickle.load(open('book_list.pkl','rb')) #read binary me matlab read kar sakte ho 
similarity = pickle.load(open('similarity_matrix.pkl','rb'))
book_list = books['title'].values
selected_book = st.selectbox("Type or select a book from the list",book_list)
given_index = books[books['title'] == selected_book].index[0]  


if st.button('Show Recommendation', use_container_width=True):
    recommended_book_cover,recommended_book_name,recommended_isbn,recommended_link=recommend_me_a_book(selected_book)
    
    with st.container():
        col1,col2,col3,col4,col5 = st.columns(5)
        with col1:
            st.image(books.iloc[given_index].img,use_column_width=True)
        with col2:
            st.header(books.iloc[given_index].title)
            st.markdown('##### Genre : ')
            st.markdown(",  ".join(books.iloc[given_index].genre))
            st.code('ISBN : '+books.iloc[given_index].isbn)
            st.link_button('More Info',books.iloc[given_index].link,use_container_width=True)
    st.subheader("You may like these Titles......")
    with st.container():
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        with col1:
            with st.container(height=160):
                st.subheader(recommended_book_name[0])
        with col2:
            with st.container(height=160):
                st.subheader(recommended_book_name[1])
        with col3:
            with st.container(height=160):
                st.subheader(recommended_book_name[2])
        with col4:
            with st.container(height=160):
                st.subheader(recommended_book_name[3])
        with col5:
            with st.container(height=160):
                st.subheader(recommended_book_name[4])
        with col6:
            with st.container(height=160):
                st.subheader(recommended_book_name[5])
    with st.container():
        columns = st.columns(6)
        for i, column in enumerate(columns):
            with column:
                if i < len(recommended_book_cover):
                    st.image(recommended_book_cover[i],use_column_width=True)
    with st.container():
        columns = st.columns(6)
        for i, column in enumerate(columns):
            with column:
                if i < len(recommended_link):
                    st.link_button('More Info', recommended_link[i], use_container_width=True)
    with st.container():
        columns = st.columns(6)
        for i, column in enumerate(columns):
            with column:
                if i < len(recommended_isbn):
                    st.code('ISBN : ' + recommended_isbn[i])
              
# to run this app
# streamlit run apptest.py

# alternative design