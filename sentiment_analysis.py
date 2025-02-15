import nltk
import pickle
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

# unpickling the two texts
with open('saved_texts.pickle','rb') as input_file:
    Wuthering_Height = pickle.load(input_file)
    Jane_Eyre = pickle.load(input_file)
    
# general the sentiment score for the two texts
score1 = SentimentIntensityAnalyzer().polarity_scores(Wuthering_Height)
score2 = SentimentIntensityAnalyzer().polarity_scores(Jane_Eyre)
print("Wuthering Height: ", score1)
print("Jane EyreL: ", score2)

