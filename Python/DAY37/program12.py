import math
from collections import defaultdict


class NaiveBayesSpamFilter:

    def __init__(self, alpha=1.0):
        # alpha is Laplace smoothing parameter
        self.alpha = alpha
        self.spam_word_counts = defaultdict(int)
        self.ham_word_counts = defaultdict(int)
        self.total_spam_emails = 0
        self.total_ham_emails = 0
        self.vocab = set()

    def train(self, dataset):
        """Trains the filter on a list of (text, label) tuples."""
        for text, label in dataset:
            words = set(text.lower().split())  # Unique words in email
            if label == "spam":
                self.total_spam_emails += 1
                for word in words:
                    self.spam_word_counts[word] += 1
                    self.vocab.add(word)
            else:  # 'ham' (normal email)
                self.total_ham_emails += 1
                for word in words:
                    self.ham_word_counts[word] += 1
                    self.vocab.add(word)

    def predict(self, text):
        """Calculates P(Spam | Text) using Naive Bayes with log probabilities

        (to prevent arithmetic underflow).
        """
        words = set(text.lower().split())

        total_emails = self.total_spam_emails + self.total_ham_emails
        prior_spam = self.total_spam_emails / total_emails
        prior_ham = self.total_ham_emails / total_emails

        # Work in log-space to prevent underflow with small floating-point numbers
        log_prob_spam = math.log(prior_spam)
        log_prob_ham = math.log(prior_ham)

        for word in words:
            # P(Word | Spam) with Laplace smoothing
            p_word_given_spam = (
                self.spam_word_counts[word] + self.alpha
            ) / (self.total_spam_emails + 2 * self.alpha)

            # P(Word | Ham) with Laplace smoothing
            p_word_given_ham = (self.ham_word_counts[word] + self.alpha) / (
                self.total_ham_emails + 2 * self.alpha
            )

            log_prob_spam += math.log(p_word_given_spam)
            log_prob_ham += math.log(p_word_given_ham)

        # Convert back from log scale to probability: P(Spam | Text)
        # Using soft-max trick for stability: 1 / (1 + e^(log_ham - log_spam))
        p_spam_given_text = 1.0 / (1.0 + math.exp(log_prob_ham - log_prob_spam))

        return p_spam_given_text


# ==============================================================================
# Example Usage & Verification
# ==============================================================================

# 1. Training Corpus
training_data = [
    # Spam Examples
    ("win free money now click link", "spam"),
    ("cheap offer free cash prize win", "spam"),
    ("urgent claim your free cash prize", "spam"),
    ("win free prize money", "spam"),
    # Ham (Legitimate) Examples
    ("project meeting scheduled for tomorrow", "ham"),
    ("please review the attached report and project file", "ham"),
    ("are we still meeting for lunch today", "ham"),
    ("can you send over the project invoice", "ham"),
]

# 2. Train Model
filter_model = NaiveBayesSpamFilter(alpha=1.0)
filter_model.train(training_data)

# 3. Test New Incoming Emails
test_emails = [
    "win free cash prize now",
    "project meeting tomorrow",
    "free project review link",
]

print("==================================================")
print("       NAIVE BAYES SPAM FILTER RESULTS")
print("==================================================")

for email in test_emails:
    p_spam = filter_model.predict(email)
    label = "SPAM 🚨" if p_spam > 0.5 else "HAM (Clean) ✅"
    print(f"Email: '{email}'")
    print(f"  --> P(Spam | Text) : {p_spam:.2%}")
    print(f"  --> Classification : {label}\n")