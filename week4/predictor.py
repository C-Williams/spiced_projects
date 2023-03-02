import pickle

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from sklearn.linear_model import LogisticRegression

from argparse import ArgumentParser

# Instantiate the parser with a description of what the program does.
parser = ArgumentParser(description="Lyrics Guessing Bot")

# Add an argument that must be given when calling the function
# help = When -h or --help is typed after calling the funciton, it gives the help message
parser.add_argument(
    "lyrics",
    help="The artists I have in my library are: Ariana Grande, B.B. King, Earth, Wind & Fire, Kendrick Lamar, and The Stooges. What lyrics should I guess?")

# The ArgumentParser.parse_args() method runs the parser and places the extracted data in a argparse.Namespace object:
args = parser.parse_args()

# Here we extracts the user inputs
lyric_input = args.lyrics

# Load in the pickle file that has the DataFrame of artists and lyrics
file = open('five_artists', 'rb')
full_list = pickle.load(file)
file.close()

# Start of the prediction model
CORPUS = full_list['lyrics'].to_list()
LABELS = full_list['artist'].to_list()

df_lyrics = pd.DataFrame(CORPUS, index=LABELS, columns=['lyrics'])

X = df_lyrics['lyrics']
y = df_lyrics.index

cv = CountVectorizer(stop_words='english',ngram_range=(1,1))
X_tran = cv.fit_transform(X)

tf = TfidfTransformer()
tf_X_tran = tf.fit_transform(X_tran)

lreg = LogisticRegression()
lreg.fit(tf_X_tran,y)

def predict_it(song_lyrics):

    lyrics_to_predict = [song_lyrics]

    lyrics_to_predict_tran = cv.transform(lyrics_to_predict)

    X_pred_trans = tf.transform(lyrics_to_predict_tran)

    # Some of my artist names are encoded in UTF-8
    # However, .encode/.decode were not working well so I did it by hand
    prediction = (lreg
                    .predict(X_pred_trans)[0]
                    .replace('%27', "'")
                    .replace('%2C', ',')
                    .replace('%3F', '?')
                    .replace('%5B', '[')
                    .replace('%5D', ']')
                    .replace('%28', "(")
                    .replace('%29', ")")
                    .replace('%2A', "*")
                    .replace('%26', "&")
                    .replace('%7', "|")
                    .replace('-', " ")
                    .replace('%21', "!")
                    .replace('_', ' ')
    )
                    
    print(f'My guess is: {prediction}')

predict_it(lyric_input)