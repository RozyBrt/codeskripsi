import pandas as pd
from preprocessing import preprocessing

# Memuat dataset yang akan diproses
df = pd.read_csv('hasilproses/hasilscrapping.csv')  # Ubah dengan nama file dataset yang kamu gunakan

# Jalankan preprocessing dengan file stopwords
stopword_file = 'stopwords-id.txt'
df_preprocessed = preprocessing(df, stopword_file)

# Simpan hasil preprocessing ke dalam satu file CSV tanpa menyertakan kolom 'full_text'
df_preprocessed.to_csv('hasil_preprocessing.csv', index=False)

# Tampilkan beberapa baris hasil akhir setelah preprocessing
print(df_preprocessed.head())
