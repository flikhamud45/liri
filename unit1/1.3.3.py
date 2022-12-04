def is_funny(string):
     return len([chr for chr in string if chr != 'h' and chr != 'a']) == 0
print(is_funny("hahahahahaha"))