# String Similarity Algorithms
Strings are widely used to represent a variety of textual data including messages, emails, product reviews, and documents. By using real applications we are collecting string datasets from various sources. String data from different sources may be inconsistent caused by the typing misatkes or the difference in data formats. The one of the most important fundamental task here is string similarity-which checks whether two strings are similar. 

Below are two similar strings:
- Winkler 
- Welfare

We need a way to compare two strings for similarity. There are multiple algorithms available such as:
- Levenshtein distance,
- Jaro-Winkler,
- Soundex etc.,.

Here we are going to discuss one by one in more detail.

# Levenshtein Distance 
Levenshtein Distance (LD) is a measure of the similarity between two strings, the source string (s) and the target string (t). The distance is the number of deletions, insertions, or substitions required to transform `s` into `t`. 

For example, 
- If `s` is "test" and `t` is "test", then LD(s,t)=0, because no transformations are needed. The strings are already identical. 
- If `s` is "test" and `t` is "tent", then LD(s,t)=1, because one substitution (change "s" to "n") is sufficient to transform `s` to `t`.

> The greater the Levenshtein distance, the more different strings are. 

# Jaro Winkler Algorithm
Jaro Winkler is an algorithm for measuring the similarity between two strings and this algorithm is is usually used in duplicate detection. The value `1` indicates the similarity between the strings and the value `0` indicates the inequality between the strings. 

The Jaro Winkler distance algorithm has three basic sections, namely:
- Calculate the length of the string.
- Specifies the same character of both strings.
- Determine the number of transpositions.

> The higher the Jaro Winkler value on two strings, the more similar the strings are.

# Soundex
Phonetic codifications attempt to represent words with similar pronunciations by the same code. Among all existing phonetic codification algorithms, *Soundex* is the most widely known. It was originally proposed for dealing with the problem of having different spelling variations of the same name (e.g., Lewinsky vs. Lewinskey).

The soundex algorithm is based on the six phonetic classifications of human speech sounds (bilabial, labiodental, dental, alveolar, velar, and glottal), which in turn are based on where we put our lips and toungue to make sounds. The algorithm itself is straightforward since it does not require of backtracking or multiple passes over the input word. This algorithm is as follows:

<ol>
  <li>Capitalize all letters in the word and drop all the punctuation marks.</li>
  <li>Retain the first letter of the word.</li>
  <li>Change all occurences of the following letters to 0 (zero):
  'A', 'E', 'I', 'O', 'U', 'H', 'W', 'Y'</li>
  <li>Change letters from the following sets into the given digit:
    <ul>
        <li> 1 = 'B', 'F', 'P', 'V' </li>
        <li> 2 = 'C', 'G', 'J', 'K', 'Q', 'S', 'X', 'Z' </li>
        <li> 3 = 'D', 'T' </li>
        <li> 4 = 'L' </li>
        <li> 5 = 'M', 'N' </li>
        <li> 6 = 'R' </li>
    </ul>
  </li>
  <li>Remove all pairs of equal digits occurrings beside each other from the string resulted after step (4).</li>
  <li>Remove all zeros from the string that results from step (5)</li>
  <li>Pad the string resulted from step (6) with trailing zeros and return only the first six positions. The output code will be of the form uppercase_letter-digit-digit-digit-digit-digit</li>
</ol>


