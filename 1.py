#def count_vowels(input_string):
 #   vowels = 'aeiouAEIOU'
  #  return sum(1 for char in input_string if char is vowels)
#input_string = "hello,welcome"
 #   vowels_count=count_vowels(input_string)
  #  print(f"no of vowels : {vowels_count}")

#def countVowels(input_string):
 #   vowels="aeiouAEIOU"
  #  return sum(1 for char in input_string if char in vowels)
#input_string="hello,Welcome to python programming languagee"
#if __name__=="__main__":
 #    vowel_count=countVowels(input_string)
  #   print(f"Number of vowels: {vowel_count}")
def sum_of_digit(n):
    total = sum(int(digit) for digit in str(n))
    return total

#example
print(sum_of_digits(123455655))
