# Problem Statement:-
# You are given few sentences as a list
# (Python list of sentences).
# Take a query string as an input from the user.
# You have to pull out the sentences matching this
# query inputted by the user in decreasing order of
# relevance after converting every word in the query
# and the sentence to lowercase. The most relevant
# sentence is the one with the maximum number of matching
# words with the query.

# Sentences = [“Python is cool”, “python is good”, “python is not python snake”]

# Input:
# Please input your query string

# “Python is”

# Output:
# 3 results found:

# python is not python snake
# python is good
# Python is cool

sentences = ["python is good","python is not python snake","Python is cool"]
userinput = input("Enter a query : ")
results = list(filter(lambda x: userinput.lower() in x.lower(),sentences))
print(f"{len(results)} results found : ")
for result in results:
    print(result)