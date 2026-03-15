 SPAM-EMAIL-DETECTION
 
COMPANY : CODTECH IT SOLUTION

NAME : TAMILSELVAN G

INTERN ID :CTIS4802

DOMAIN : PYTHON PROGRAMMING

DURATION : 8 WEEKS

MENTOR : NEELA SANTHOSH

1.PROJECT OVERVIEW :

This Python project is designed to create a Spam Email Detection Model. It collects email text data, processes the text using machine learning techniques, and classifies the messages as Spam or Ham (Not Spam). The final output predicts whether a new email message is spam or not.

1. Libraries

1. pandas Library
Pandas is used to store and manage the dataset in a structured table format called a DataFrame, which makes it easy to handle email data.

2. Scikit-learn Library
Scikit-learn is used to build and train the machine learning model for spam classification.
3. NumPy Library
NumPy helps in handling numerical data during the machine learning process.

2. Key Variables

1. Dataset
Contains email messages and their labels (spam or ham).
2. Feature Data (X)
The email text converted into numeric vectors using CountVectorizer.

3. Target Data (y)
The labels that represent whether an email is spam or ham.

3. Functions
1. Text Vectorization

The email text is converted into numeric form using CountVectorizer, allowing the machine learning model to process text data.

2. Training the Model

The dataset is split into training and testing sets, and the Naive Bayes classifier is trained using the training data.

3. Model Evaluation

The trained model is evaluated using accuracy score and classification report to measure how well it predicts spam emails.

4. Prediction

The model can take a new email message as input and classify it as Spam or Ham.
