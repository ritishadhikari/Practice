from nltk.corpus import stopwords
import nltk
from nltk.stem.snowball import SnowballStemmer
#nltk.download('stopwords')
sw= stopwords.words("english")
print("Stopwords List are :",sw, "\n")
print(len(sw))
stemmer = SnowballStemmer('english')
print("Printing the Stemmmer Words : ",stemmer.stem("serendipity"),"\n")
