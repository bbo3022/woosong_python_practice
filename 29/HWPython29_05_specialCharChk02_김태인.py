'''
(...)
group

(?P<name>...)
group name

(?=...)

(?!...)
not
-------------------------------------
\d
demical digit; this is equivalent to the class[0-9]
\D 
Matches any non -digit[^0-9]
\s
whitespace >>[\t\n\r\f\v]
\S
non-whitespace >>>[^\t\n\r\f\v]
\w
alphanumeric character,>>[a-zA-Z0-9]
\W
non-alphanumeric character>>[^a-zA-Z0-9]
------------------------복잡한 문자열을 처리할 때 사용하는 기법
match()
beginning of the strings
search()
location where this RE matches
findall()
all substrings>>returns them as a list
finditer()
all substrings>> returns them as an iterator

'''