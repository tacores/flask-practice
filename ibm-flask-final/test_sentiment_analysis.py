from SentimentAnalysis.sentiment_analysis import sentiment_analyzer
import unittest

class TestSentimentAnalyzer(unittest.TestCase):
    def test_sentiment_analyzer(self):
        res = sentiment_analyzer('I love working with Python')
        self.assertEqual(res['label'], 'SENT_POSITIVE')

        res = sentiment_analyzer('I hate working with Pyhton')
        self.assertEqual(res['label'], 'SENT_NEGATIVE')

        res = sentiment_analyzer('I am neutral on Python')
        self.assertEqual(res['label'], 'SENT_NEUTRAL')

unittest.main()
