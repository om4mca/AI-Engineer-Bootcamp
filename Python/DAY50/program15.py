import math
from collections import defaultdict
from typing import Dict, List, Set, Tuple


class BayesInferenceEngine:
    """Pure Python Bayesian Inference and Probabilistic Reasoning Engine."""

    @staticmethod
    def compute_posterior(
        prior: float, likelihood: float, false_positive_rate: float
    ) -> Dict[str, float]:
        """Calculates Posterior Probability P(A|B) given Prior P(A), Likelihood P(B|A),

        and False Positive Rate P(B|~A).
        """
        prior_not_a = 1.0 - prior
        marginal_likelihood = (likelihood * prior) + (
            false_positive_rate * prior_not_a
        )
        posterior = (likelihood * prior) / marginal_likelihood

        return {
            "Prior P(A)": round(prior, 4),
            "Likelihood P(B|A)": round(likelihood, 4),
            "False Positive Rate P(B|~A)": round(false_positive_rate, 4),
            "Marginal Likelihood P(B)": round(marginal_likelihood, 4),
            "Posterior P(A|B)": round(posterior, 4),
        }

    @staticmethod
    def sequential_bayes_update(
        initial_prior: float, test_outcomes: List[Tuple[float, float]]
    ) -> List[Dict[str, float]]:
        """Updates belief iteratively across multiple sequential observations/tests.

        test_outcomes: List of tuples (Likelihood, False_Positive_Rate)
        """
        history = []
        current_prior = initial_prior

        for step, (likelihood, fpr) in enumerate(test_outcomes, start=1):
            result = BayesInferenceEngine.compute_posterior(
                current_prior, likelihood, fpr
            )
            result["Step"] = step
            history.append(result)
            # Update prior for next iteration
            current_prior = result["Posterior P(A|B)"]

        return history


class NaiveBayesTextClassifier:
    """Multinomial Naïve Bayes Classifier from scratch for Text Classification."""

    def __init__(self, laplace_smoothing: float = 1.0):
        self.alpha = laplace_smoothing
        self.class_counts = defaultdict(int)
        self.feature_counts = defaultdict(lambda: defaultdict(int))
        self.vocab: Set[str] = set()
        self.total_docs = 0

    def fit(self, documents: List[str], labels: List[str]):
        """Trains the Naïve Bayes model by building probability tables."""
        for doc, label in zip(documents, labels):
            self.total_docs += 1
            self.class_counts[label] += 1
            words = doc.lower().split()
            for word in words:
                self.vocab.add(word)
                self.feature_counts[label][word] += 1

    def predict(self, text: str) -> Dict[str, float]:
        """Predicts class probabilities using Log-Likelihoods to prevent underflow."""
        words = text.lower().split()
        log_posteriors = {}

        for c, count in self.class_counts.items():
            # Prior P(C)
            log_prior = math.log(count / self.total_docs)
            log_likelihood_sum = 0.0

            total_words_in_class = sum(self.feature_counts[c].values())
            vocab_size = len(self.vocab)

            for word in words:
                # Laplace Smoothing P(W|C)
                word_count = self.feature_counts[c][word]
                word_prob = (word_count + self.alpha) / (
                    total_words_in_class + self.alpha * vocab_size
                )
                log_likelihood_sum += math.log(word_prob)

            log_posteriors[c] = log_prior + log_likelihood_sum

        # Convert Log Probabilities back to Normalized Probabilities
        max_log = max(log_posteriors.values())
        exp_probs = {c: math.exp(lp - max_log) for c, lp in log_posteriors.items()}
        total_exp = sum(exp_probs.values())

        return {c: round(prob / total_exp, 4) for c, prob in exp_probs.items()}


# ==========================================
# Driver Code & Verification
# ==========================================
if __name__ == "__main__":
    print("============================================")
    print("        BAYES ANALYSIS SYSTEM               ")
    print("============================================\n")

    # 1. Single Medical Diagnostic Inference
    print("--- [1] Medical Diagnosis Bayesian Inference ---")
    # Disease Prior = 1% (0.01), Test Sensitivity (Likelihood) = 95% (0.95), False Positive = 5% (0.05)
    diag_res = BayesInferenceEngine.compute_posterior(
        prior=0.01, likelihood=0.95, false_positive_rate=0.05
    )
    for k, v in diag_res.items():
        print(f"  {k:<28}: {v}")

    # 2. Sequential Evidence Updating (Two Consecutive Positive Tests)
    print("\n--- [2] Sequential Bayesian Update (2 Positive Tests) ---")
    tests = [(0.95, 0.05), (0.95, 0.05)]
    history = BayesInferenceEngine.sequential_bayes_update(
        initial_prior=0.01, test_outcomes=tests
    )
    for step in history:
        print(f"  Test #{step['Step']} -> Updated Posterior: {step['Posterior P(A|B)']}")

    # 3. Naïve Bayes Text Classifier (Spam Filter)
    print("\n--- [3] Naïve Bayes Text Classifier Training & Testing ---")
    train_docs = [
        "win free cash prize bonus now",
        "cheap low price offers available",
        "meeting scheduled for project update",
        "please review the attached report and code",
        "exclusive discount deal prize winner",
    ]
    train_labels = ["spam", "spam", "ham", "ham", "spam"]

    clf = NaiveBayesTextClassifier(laplace_smoothing=1.0)
    clf.fit(train_docs, train_labels)

    test_msg = "free project bonus update"
    predicted_probs = clf.predict(test_msg)

    print(f"Input Message  : '{test_msg}'")
    print(f"Class Probabilities:")
    for label, prob in predicted_probs.items():
        print(f"  - {label.upper():<6}: {prob * 100:.2f}%")