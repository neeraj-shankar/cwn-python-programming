Python RegEx Expressions Functions
-----------------------------------------------------------------------------------------------------------------------

1. findall(pattern,string)	
-----------------------------------------------------------------------------------------
This matches all the occurrences of the pattern present in the string.

2. search(pattern,string)	
-----------------------------------------------------------------------------------------
This matches the pattern which is present at any position in the string. This will match the first occurrence of 
the pattern.

3. split(pattern,string)	
-----------------------------------------------------------------------------------------
This splits the string on the given pattern.


4. sub(pattern,rep_substring,string)	
-----------------------------------------------------------------------------------------
This replaces one or more matching pattern in the string with the given substring.


Meta Characters
-----------------------------------------------------------------------------------------------------------------------

[ ](Square brackets):
-----------------------------------------------------------
This matches any single character in this bracket with the given string.

. (Period):
-----------------------------------------------------------
This matches all the characters except the newline. If we pass this as a pattern in the findall() function it will 
match with all the characters present in the string except newline characters.

^ (Carret)	
-----------------------------------------------------------
This matches the given pattern at the start of the string.This is used to check if the string starts with a particular
pattern or not.	

$ (Dollar)
-----------------------------------------------------------
This matches the given pattern at the end of string. This is used to check if the string ends with a pattern or not.

* (Star)
-----------------------------------------------------------
This matches 0 or more occurrences of the pattern to its left.	

+ (Plus)	
-----------------------------------------------------------
This matches 1 or more occurrences of the pattern to its left.	

? (Question mark)
-----------------------------------------------------------
This matches 0 or 1 occurrence of the pattern to its left.	

{ } (Braces)
-----------------------------------------------------------
This matches the specified number of occurrences of pattern present in the braces.	


(Alternation)
----------------------------------------------------------
This works like ‘or’ condition. In this we can give two or more patterns. If the string contains at least one of the 
given patterns this will give a match.

( ) (Group)	
-----------------------------------------------------------
This is used to group various regular expressions together and then find a match in the string.	

\ (Backslash)	
-----------------------------------------------------------
This is used to match special sequences or can be used as escape characters also.	
