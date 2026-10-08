import unittest
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer

class TestSentimentAnalyzer(unittest.TestCase):

    def test_sentiment_analyzer(self):
        test_cases = [
            (sentiment_analyzer('I love working')['label'], 'POSITIVE'),
            (sentiment_analyzer('I hate working with Python')['label'], 'NEGATIVE'),
            (sentiment_analyzer('I am neutral on Python')['label'], 'NEUTRAL'),
        ]

        for item in test_cases:
            self.assertEqual(item[0], item[1])

unittest.main()
