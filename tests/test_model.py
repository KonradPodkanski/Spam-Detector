import unittest
from model import train_and_predict

class TestSpamDetector(unittest.TestCase):

    def test_spam_messages(self):
        spam_examples = [
            "Congratulations! You've won a free cruise to the Bahamas!",
            "Click now to claim your $1000 prize!",
            "Urgent: Update your bank information to avoid penalties.",
            "Win a free iPhone today!",
            "Free entry into our $5000 cash giveaway!",
            "You’ve earned a special bonus! Claim now.",
        ]
        for msg in spam_examples:
            with self.subTest(msg=msg):
                self.assertEqual(train_and_predict(msg), 1)

    def test_ham_messages(self):
        ham_examples = [
            "Hey, are we still meeting for lunch today?",
            "Don't forget about the meeting at 3PM.",
            "Can you send me the report by tomorrow?",
            "How are you doing? Long time no see!",
            "I'll call you when I get home.",
            "Let's go for a walk this evening.",
        ]
        for msg in ham_examples:
            with self.subTest(msg=msg):
                self.assertEqual(train_and_predict(msg), 0)

if __name__ == '__main__':
    unittest.main()
