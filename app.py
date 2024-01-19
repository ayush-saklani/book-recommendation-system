import pickle
import streamlit as st

def recommend(book):
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
    # return recommended_book_name,recommended_book_cover

st.set_page_config(layout="wide")
st.title('Book Recommender System')
st.caption('For all you bookworms')
books = pickle.load(open('book_list.pkl','rb')) #read binary me matlab read kar sakte ho 
similarity = pickle.load(open('similarity.pkl','rb'))

book_list = books['title'].values
selected_book = st.selectbox("Type or select a book from the list",book_list)

if st.button('Show Recommendation', use_container_width=True):
    recommended_book_cover,recommended_book_name,recommended_isbn,recommended_link=recommend(selected_book)

    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        with st.container(height=200,border=None):
            st.subheader(recommended_book_name[0])
        st.image(recommended_book_cover[0],width=220)
        st.link_button('More Info', recommended_link[0], use_container_width=True)
        st.code('ISBN : '+recommended_isbn[0])
    with col2:
        with st.container(height=200,border=None):
            st.subheader(recommended_book_name[1])
        st.image(recommended_book_cover[1],width=220)
        st.link_button('More Info', recommended_link[1], use_container_width=True)
        st.code('ISBN : '+recommended_isbn[1])
    with col3:
        with st.container(height=200,border=None):
            st.subheader(recommended_book_name[2])
        st.image(recommended_book_cover[2],width=220)
        st.link_button('More Info', recommended_link[2], use_container_width=True)
        st.code('ISBN : '+recommended_isbn[2])
    with col4:
        with st.container(height=200,border=None):
            st.subheader(recommended_book_name[3])
        st.image(recommended_book_cover[3],width=220)
        st.link_button('More Info', recommended_link[3], use_container_width=True)
        st.code('ISBN : '+recommended_isbn[3])
    with col5:
        with st.container(height=200,border=None):
            st.subheader(recommended_book_name[4])
        st.image(recommended_book_cover[4],width=220)
        st.link_button('More Info', recommended_link[4], use_container_width=True)
        st.code('ISBN : '+recommended_isbn[4])
    with col6:
        with st.container(height=200,border=None):
            st.subheader(recommended_book_name[5])
        st.image(recommended_book_cover[5],width=220)
        st.link_button('More Info', recommended_link[5], use_container_width=True)
        st.code('ISBN : '+recommended_isbn[5])

# to run this app
# streamlit run app.py



