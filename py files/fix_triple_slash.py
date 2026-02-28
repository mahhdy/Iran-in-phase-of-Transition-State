import os
import re

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # replace \\\[ with \\[
            # but in string syntax:
            # content.replace('\\\\\\[', '\\\\[') 
            content = content.replace('\\\\\[', '\\\\[')
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
