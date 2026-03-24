def count_vowel_constant(s):
    v="aeiouAEIOU"
    vowel_count=0
    consonent_count=0
    for char in s.lower():
       if char.isalpha():
          if char in v:
             vowel_count +=1
          else:
              consonent_count +=1
    return vowel_count,consonent_count 
s=input("enter the string:")
print(count_vowel_constant(s))

