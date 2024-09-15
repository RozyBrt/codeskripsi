import re
import pandas as pd
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory

# Fungsi Case Folding (mengubah teks menjadi huruf kecil)
def clean_lower(text):
    return text.lower()

# Fungsi Remove Punctuation
clean_spcl = re.compile('[/(){}\[\]\|@,;]')
clean_symbol = re.compile('[^0-9a-z]')

def clean_punct(text):
    text = clean_spcl.sub('', text)  # Hapus simbol tertentu
    text = clean_symbol.sub(' ', text)  # Ganti simbol lainnya dengan spasi
    return text

# Fungsi untuk membaca stopwords dari file eksternal
def load_stopwords(file_path):
    with open(file_path, 'r') as file:
        additional_stopwords = set(file.read().splitlines())  # Membaca setiap baris
    return additional_stopwords

# Fungsi untuk menghapus stopwords
def clean_stopwords(text, stopwords):
    return ' '.join(word for word in text.split() if word not in stopwords)

# Fungsi Utama Preprocessing
def preprocessing(df, stopword_file):
    # 1. Case folding
    df['after_case_folding'] = df['full_text'].apply(clean_lower)
    
    # 2. Remove punctuation
    df['after_remove_punctuation'] = df['after_case_folding'].apply(clean_punct)
    
    # 3. Load stopwords dari file dan Sastrawi
    factory = StopWordRemoverFactory()
    stopwords_sastrawi = set(factory.get_stop_words())
    stopwords_file = load_stopwords(stopword_file)
    stopwords = stopwords_sastrawi.union(stopwords_file)

    # 4. Stopwords removal
    df['after_remove_stopwords'] = df['after_remove_punctuation'].apply(lambda x: clean_stopwords(x, stopwords))
    
    # Mengembalikan hanya kolom hasil preprocessing
    return df[['after_case_folding', 'after_remove_punctuation', 'after_remove_stopwords']]
