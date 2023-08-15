import string
from googletrans import Translator
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer

text = input("Enter Sentence: ")
translator = Translator()
eng_text = translator.translate(text, dest='en')
lower_case = eng_text.text.lower()
cleaned_text = lower_case.translate(str.maketrans('', '', string.punctuation))

tokenized_words = word_tokenize(cleaned_text, "english")

final_words = []
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

print(final_words)

def sentiment_analyse(sentiment_text):
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    print(score)
    neg = score['neg']
    pos = score['pos']
    neu = score['neu']
    if neg > pos:
        print("%{point} Negative Sentiment".format(point=((neu+neg)*100)))
    elif pos > neg:
        print("%{point} Positive Sentiment".format(point=((neu+pos)*100)))
    else:
        print('Neural Vibe')

sentiment_analyse(cleaned_text)
