import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense, Dropout
from tensorflow.keras.optimizers import Adam
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
import pickle

# Fungsi untuk memuat dan mempersiapkan dataset
def load_dataset(file_path):
    # Mengasumsikan dataset dalam format CSV dengan dua kolom: 'text' (berita) dan 'label' (kategori)
    df = pd.read_csv(file_path)
    texts = df['text'].values
    labels = df['label'].values
    return texts, labels

# Fungsi untuk tokenisasi dan padding teks
def preprocess_text(texts, max_words=10000, max_len=100):
    tokenizer = Tokenizer(num_words=max_words, lower=True, split=' ')
    tokenizer.fit_on_texts(texts)
    sequences = tokenizer.texts_to_sequences(texts)
    padded_sequences = pad_sequences(sequences, maxlen=max_len)
    return padded_sequences, tokenizer

# Fungsi untuk membangun model klasifikasi berbasis LSTM
def build_model(input_length, max_words=10000, embedding_dim=100):
    model = Sequential()
    model.add(Embedding(input_dim=max_words, output_dim=embedding_dim, input_length=input_length))
    model.add(LSTM(units=128, return_sequences=True))
    model.add(Dropout(0.5))
    model.add(LSTM(units=64))
    model.add(Dense(units=32, activation='relu'))
    model.add(Dense(units=1, activation='sigmoid'))  # Output binary (disinformasi atau tidak)
    
    model.compile(optimizer=Adam(), loss='binary_crossentropy', metrics=['accuracy'])
    return model

# Fungsi untuk melatih model
def train_model(texts, labels, model, epochs=5, batch_size=64):
    # Label encoding untuk klasifikasi biner
    le = LabelEncoder()
    labels = le.fit_transform(labels)
    
    # Split data menjadi training dan testing set
    X_train, X_test, y_train, y_test = train_test_split(texts, labels, test_size=0.2, random_state=42)
    
    # Melatih model
    model.fit(X_train, y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_test, y_test), verbose=2)
    return model, le

# Fungsi untuk menyimpan model dan tokenizer
def save_model(model, tokenizer, label_encoder, model_filename='disinfo_model.h5', tokenizer_filename='tokenizer.pkl', le_filename='label_encoder.pkl'):
    model.save(model_filename)
    with open(tokenizer_filename, 'wb') as f:
        pickle.dump(tokenizer, f)
    with open(le_filename, 'wb') as f:
        pickle.dump(label_encoder, f)

# Fungsi untuk memuat model dan tokenizer
def load_model_and_tokenizer(model_filename='disinfo_model.h5', tokenizer_filename='tokenizer.pkl', le_filename='label_encoder.pkl'):
    model = tf.keras.models.load_model(model_filename)
    with open(tokenizer_filename, 'rb') as f:
        tokenizer = pickle.load(f)
    with open(le_filename, 'rb') as f:
        label_encoder = pickle.load(f)
    return model, tokenizer, label_encoder

# Fungsi untuk mengklasifikasikan berita baru
def classify_news(news, model, tokenizer, label_encoder, max_len=100):
    # Preprocess berita baru
    sequences = tokenizer.texts_to_sequences([news])
    padded_sequences = pad_sequences(sequences, maxlen=max_len)
    
    # Prediksi menggunakan model
    prediction = model.predict(padded_sequences)
    
    # Klasifikasikan sebagai 'disinformasi' atau 'benar' berdasarkan prediksi
    predicted_label = label_encoder.inverse_transform([int(prediction[0] > 0.5)])[0]
    return predicted_label

if __name__ == "__main__":
    # Memuat dataset
    texts, labels = load_dataset('news_data.csv')
    
    # Preprocess data
    texts_prep, tokenizer = preprocess_text(texts)
    
    # Membangun model
    model = build_model(input_length=texts_prep.shape[1])
    
    # Melatih model
    model, le = train_model(texts_prep, labels, model)
    
    # Menyimpan model dan tokenizer
    save_model(model, tokenizer, le)
    
    # Menguji klasifikasi dengan berita baru
    sample_news = "Pemerintah mengumumkan vaksin baru untuk COVID-19 yang dapat mengatasi varian terbaru."
    label = classify_news(sample_news, model, tokenizer, le)
    print(f"Prediksi label untuk berita: {label}")
      
