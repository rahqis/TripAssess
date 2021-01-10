import nltk
import nltk.sentiment.vader
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer as SIA

positiveScore = 0
negativeScore = 0
neutralScore = 0


def positiveSentimentDetector(descriptions):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SIA()

    # polarity_scores method of SentimentIntensityAnalyzer
    # oject gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(descriptions)

    positiveScore = sentiment_dict["pos"] * 100
    return positiveScore


def negativeSentimentDetector(descriptions):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SIA()

    # polarity_scores method of SentimentIntensityAnalyzer
    # oject gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(descriptions)

    negativeScore = sentiment_dict["neg"] * 100
    return negativeScore


def neutralSentimentDetector(descriptions):
    # Create a SentimentIntensityAnalyzer object.
    sid_obj = SIA()

    # polarity_scores method of SentimentIntensityAnalyzer
    # oject gives a sentiment dictionary.
    # which contains pos, neg, neu, and compound scores.
    sentiment_dict = sid_obj.polarity_scores(descriptions)

    neutralScore = sentiment_dict["neu"] * 100
    return neutralScore