'''
You are asked to develop a simple tag counter that will look for the occurrence of certain words or phrases in a piece of text. You are given a paragraph as a string and a list of tag groups as a list of lists of strings. Write a tag_counter function that returns a list of integers with the number of times each tag in the tag group was used in the text.

Note: Your function should be case-insensitive with regards to the tag groups.
'''

tag_groups = [
    ['data scientist', 'data analyst'], 
    ['data engineer', 'data wrangler'], 
    ['machine learning engineer'], 
    ['data' , 'engineer']]

text = "Today, with the advent of data science, different roles have emerged in the industry. Job postings are abundant of many names such as data scientist, data engineer, data wrangler, deep learning specialist, and machine learning specialist to name a few."

def tag_counter(text, tag_groups):
    counts = []
    for group in tag_groups:
        count = 0
        for tag in group:
            count += text.lower().count(tag)
        counts.append(count)
    return counts

print(tag_counter(text, tag_groups))