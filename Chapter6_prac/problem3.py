# 3. A spam comment is defined as a text containing following keywords:
#    “Make a lot of money”, “buy now”, “subscribe this”, “click this”.
#    Write a program to detect these spams.

text = input("Enter the text of the comment: ")
if ("Make a lot of money" in text) or ("buy now" in text) or ("subscribe this" in text) or ("click this" in text):
    print("This comment is a spam.")    
else:
    print("This comment is not a spam.")
