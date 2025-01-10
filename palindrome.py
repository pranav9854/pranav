def is_pallindrome(s):
   s = s.lower()
   return s ==s[::-1]
word=input("enter a word:")
if is_pallindrome(word):
    print("pallindrome")
else:
    print("not pallindrome") 