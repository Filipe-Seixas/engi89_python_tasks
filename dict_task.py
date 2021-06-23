# #1 - Define a dictionary call story1, it should have the following keys: 'start', 'middle' and 'end'
story1 = {"start": "Once upon a time there was a person.",
          "middle": "This person had a problem.",
          "end": "The person found a solution to the problem."
          }
# #2 - Print the entire dictionary
print(story1)
# #3 - Print the type of your dictionary
print(type(story1))
# #4 - Print only the keys
print(story1.keys())
# #5 - print only the values
print(story1.values())
# #6 - print the individual values using the keys (individually, lots of print commands)
print(story1["start"])
print(story1["middle"])
print(story1["end"])
# #7 - Now let's add a new key:value pair.
story1["hero"] = "Batman"
