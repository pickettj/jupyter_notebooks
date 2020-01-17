
#Parser, Mark 1: XML conversion for custom mark-down used for document transcription



#Use Regex to recognize patterns
## There is an RE module for Regex expressions
## to put what you are subbing inside what you are matching: 
### re.sub(r'^\- (.*)$', r'<li>\1</li>', '- qaaaaabcq')
#### How does the regex \1 work?


import re


file_name = 'ser560.md'

f = open(file_name)
text_lines = f.readlines()
f.close()


text_lines.insert(0, '<document>\n')
text_lines.insert(1, '\t<metadata>\n')
text_lines.insert(2, '\t\t<unique_id>' + file_name + '</unique_id>\n')


#<unique_id>ser561</unique_id>

text_lines = [re.sub (r'^\- (.*)$', r'<li>\1</li>', x.lstrip()) for x in text_lines]


outfile = open('parser_output.txt', 'w')
outfile.writelines(text_lines)
outfile.close()




