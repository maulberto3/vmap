text = '''My father’s family name being 
Pirrip, and my Christian name Philip, 
my infant tongue could make of both 
names nothing longer or more explicit 
than Pip. So, I called myself Pip, 
and came to be called Pip.'''

print('Regex hands-on!')
import re
print(f'Find words containing')
regex = re.compile(r'\w+t\w+')
result = regex.findall(text)
print(result)