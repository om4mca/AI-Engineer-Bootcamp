# 🚀 AI Engineer Bootcamp - Day 51

## 📅 Date
03-09-2026

## 📚 Topics Covered

- # Day 51 — Introduction to Machine Learning

##  ML Introduction
## AI vs ML vs DL
## ML Workflow
## Supervised Learning
## Unsupervised Learning
## Reinforcement Learning
## Features & Target
## Training/Test Data
## Regression
## Classification
## Overfitting
## Underfitting
## Data Leakage
## 15 Practice Programs
## Hospital ML Problem Analyzer
## Employee ML Problem Analyzer
## Notebook
## 20 Interview Questions
## README.md
## GitHub Push


## 📂 GitHub

Day51 Completed Successfully ✅

## 🧠 Interview Preparation


1.  What is Machine Learning?

Machine Learning (ML) is a subset of Artificial Intelligence where computers use algorithms to identify patterns in data and make decisions or predictions without being explicitly programmed for specific rules.

2. How is ML different from traditional programming?

Traditional Programming: You input Data + Rules $\rightarrow$ Program computes the Output.Machine Learning: You input Data + Desired Output $\rightarrow$ Algorithm learns and outputs the Rules (Model).

3. What is the difference between AI, ML and Deep Learning?

Artificial Intelligence (AI): The broad concept of creating smart machines capable of performing tasks that typically require human intelligence.Machine Learning (ML): A subfield of AI focused on algorithms that automatically learn and improve from experience without explicit programming.Deep Learning (DL): A specialized subfield of ML that uses multi-layered Artificial Neural Networks to analyze complex, unstructured data (like photos, video, or audio).

4. What is supervised learning?

A type of machine learning where the algorithm is trained on a labeled dataset—meaning the input data is paired with the correct output answers (ground truth) to guide the model's learning process.

5. What is unsupervised learning?

A type of machine learning where the algorithm works on an unlabeled dataset to discover hidden patterns, groupings, or structures on its own without predefined targets or human guidance.

6. What is reinforcement learning?

A trial-and-error learning paradigm where an autonomous software agent learns to make optimal decisions in an environment by receiving feedback in the form of rewards for good actions and penalties for bad ones.

7. What is a feature?

An individual, measurable property or characteristic of a dataset used as an input variable to make predictions (e.g., Age, Square Footage, Income).

8. What is a target variable?

The output or ground truth variable that the machine learning model is being trained to predict or estimate (e.g., House Price, Spam/Ham, Disease Status).

9. What is the difference between X and y?

$X$ (Features): The matrix of independent input variables supplied to the model.$y$ (Target): The vector containing the dependent output variable(s) the model tries to learn to predict.

10. What is training data?

The major portion of a dataset (typically 70%–80%) used to fit the model parameters and teach it patterns during the development phase.

11. What is testing data?

An isolated subset of data held back during training to evaluate how accurately the model generalizes to completely unseen real-world data.

12. Why do we split a dataset?

To prevent memorization (overfitting) and get an unbiased evaluation of how well the model will perform on new, unseen data in production.

13. What is regression?

A supervised learning task where the objective is to predict a continuous numerical value (e.g., predicting stock prices or temperature).

14. What is classification?

A supervised learning task where the objective is to assign data points into discrete categorical classes or labels (e.g., classifying an email as Spam or Not Spam).

15. What is overfitting?

A condition where a model learns the training data, noise, and outliers too precisely, resulting in near-perfect accuracy on training data but poor performance on testing data.

16. What is underfitting?

A condition where a model is too simple to capture the underlying structure or patterns in the data, leading to poor accuracy on both training and testing datasets.

17. What is data leakage?

An error where information from outside the training dataset (such as future data or target labels from the test set) accidentally enters the training pipeline, causing unrealistically optimistic training metrics that fail in real-world deployment.

18. Give a real-world example of supervised learning.

Email Spam Filtering: A system is trained on millions of emails labeled explicitly as "Spam" or "Not Spam" ($y$) using text features ($X$) like subject lines, keywords, and sender domains to automatically classify incoming emails.

19. Give a real-world example of unsupervised learning.

Customer Segmentation in E-Commerce: Clustering algorithms analyze raw purchasing history, browsing logs, and user demographics without preset labels to group customers into distinct buying personas for targeted marketing.

20. Explain the complete ML workflow.[ Problem Definition ]
          │
          ▼
[ Data Collection & Cleaning ]
          │
          ▼
[ Feature Engineering ]
          │
          ▼
[ Train / Test Split ]
          │
          ▼
[ Model Training ]
          │
          ▼
[ Model Evaluation ]
          │
          ▼
[ Deployment & Monitoring ]
Problem Definition: Identify the business objective and determine if it requires classification, regression, or clustering.Data Collection & Cleaning: Gather raw data, handle missing values, and remove duplicates/outliers.Feature Engineering: Select relevant inputs, transform text/categorical columns into numbers, and scale values.Train/Test Split: Divide data into separate training (for learning patterns) and testing sets (for unbiased validation).Model Training: Feed training data ($X_{train}, y_{train}$) into the chosen algorithm to learn patterns.Model Evaluation: Test predictions against real labels ($y_{test}$) using evaluation metrics (Accuracy, MAE, R², Precision/Recall).Deployment & Monitoring: Deploy the model into production systems and continuously monitor for performance decay or data drift.