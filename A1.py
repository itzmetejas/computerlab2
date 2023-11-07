import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize

nltk.download('punkt')
nltk.download('stopwords')

random_text = """
Data processing encompasses a series of operations that convert raw data into structured
and organized information. This process begins with data collection, where data is gathered
from various sources such as sensors, databases, forms, or external systems. Once collected,
the data can be in various formats, including text, numbers, images, or multimedia.
The next step in data processing is data cleaning and validation. This involves identifying
and correcting errors, inconsistencies, and missing values in the data. Clean and accurate data
is essential for reliable analysis and decision-making. Data cleaning often involves techniques
like outlier detection and data imputation.
After data cleaning, data transformation is performed. This includes tasks like data normalization,
aggregation, and summarization. Normalization ensures that data is on a consistent scale, while
aggregation and summarization reduce data complexity by generating statistics or aggregating data into meaningful groups.
Data processing also includes data integration, where data from multiple sources is combined
into a unified dataset. Integration can be challenging due to differences in data structures and
formats. Techniques like data mapping and data warehousing are used to facilitate integration.
"""

words = word_tokenize(random_text)
stemmer = PorterStemmer()
stop_words = set(stopwords.words('english'))
preprocessed_words = []

for word in words:
  word = word.lower()
  word = word.strip('.,?!-()[]"'')

  if word not in stop_words:
    word = stemmer.stem(word)
    preprocessed_words.append(word)

preprocessed_text = " ".join(preprocessed_words)

print(random_text)
print(preprocessed_text)
