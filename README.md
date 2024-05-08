# word_predictor
**Word Predictor App**

Word Predictor is a Python application that analyzes text files and predicts the next word based on the input word. The application has the following features:

Statistics: Displays basic statistics about the training data, such as the number of files, total number of words, and the number of unique words. It also lists the five rarest words found in the training data.
Prediction Modes: Offers three different prediction modes:
Mode A: Given an input word, the application lists the top k words that are most likely to follow the input word based on the training data.
Mode B: Given an input word, the application generates n words by randomly selecting the next word from the list of possible words that can follow the input word.
Mode C: Given an input word, the application generates n words based on the probability distribution of the possible words that can follow the input word.
Usage:

Prepare a directory with text files to be used as training data.
Update the directory variable in the code with the path to the training data directory.
Run the application.
The application will display basic statistics about the training data.
Select a prediction mode (A, B, or C) and input the required word(s) and number(s).

**Dependencies:**

Python 3.x
os
re
random
collections

**Installation:**

1. Clone the repository.
2. Update the directory variable in the code with the path to the training data directory.
3. Run the application using a Python interpreter.
   
Contributing:

Contributions are welcome. Please submit a pull request with your suggested changes.

License:

This project is licensed under the MIT License.
