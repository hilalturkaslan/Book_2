import streamlit as st

# Başlık
st.title('Kitap Öneri Sistemi')

# Kullanıcıdan kitap adı girmesini iste
book_title = st.text_input('Kitabınızın adı nedir?')

# Kullanıcıya kitap türü seçme imkanı ver
book_genre = st.selectbox('İlgi alanınıza göre bir tür seçin:', ['Dram', 'Bilim Kurgu', 'Romantik', 'Gerilim', 'Kişisel Gelişim', 'Tarih', 'Hikaye'])

# Arama butonu ekleyelim
search_button = st.button('Kitap Ara')

# Sabit kitap veri seti
recommended_books = [
    {"title": "Kitap 1", "author": "Yazar 1", "genre": "Dram", "description": "Bu kitap hakkında açıklama", "cover": "https://via.placeholder.com/150", "year": 2021, "pages": 320},
    {"title": "Kitap 2", "author": "Yazar 2", "genre": "Bilim Kurgu", "description": "Bu kitap hakkında açıklama", "cover": "https://via.placeholder.com/150", "year": 2020, "pages": 280},
    {"title": "Kitap 3", "author": "Yazar 3", "genre": "Romantik", "description": "Bu kitap hakkında açıklama", "cover": "https://via.placeholder.com/150", "year": 2019, "pages": 250},
    {"title": "Kitap 4", "author": "Yazar 4", "genre": "Gerilim", "description": "Bu kitap hakkında açıklama", "cover": "https://via.placeholder.com/150", "year": 2022, "pages": 300},
    {"title": "Kitap 5", "author": "Yazar 5", "genre": "Kişisel Gelişim", "description": "Bu kitap hakkında açıklama", "cover": "https://via.placeholder.com/150", "year": 2021, "pages": 320},
    {"title": "Kitap 6", "author": "Yazar 6", "genre": "Tarih", "description": "Bu kitap hakkında açıklama", "cover": "https://via.placeholder.com/150", "year": 2020, "pages": 280}
]

if search_button and book_title:
    st.write(f"'{book_title}' kitabına benzer kitaplar öneriliyor...")

    # Seçilen türe göre önerileri filtrele
    filtered_books = [book for book in recommended_books if book['genre'] == book_genre]
    
    if filtered_books:
        for book in filtered_books:
            col1, col2 = st.columns([1, 3])
            with col1:
                st.image(book["cover"], width=100)  # Kitap kapağını göster
            with col2:
                st.subheader(book["title"])
                st.write(f"Yazar: {book['author']}")
                st.write(f"Tür: {book['genre']}")
                st.write(f"Yayın Yılı: {book['year']}")
                st.write(f"Sayfa Sayısı: {book['pages']}")
                st.write(f"Açıklama: {book['description']}")
                st.markdown("---")
    else:
        st.write("Bu türe ait öneri bulunamadı. Farklı bir tür deneyin.")

else:
    st.write("Kitap adı girin ve 'Kitap Ara' butonuna tıklayın.")




