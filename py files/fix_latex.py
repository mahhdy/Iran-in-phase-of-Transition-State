import os
import re

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # fix double rl
            content = content.replace(r'\rl{\rl{', r'\rl{')
            content = content.replace(r'}}', r'}')  # Wait, this is very dangerous. 
            # safe double rl fix 
            content = re.sub(r'\\rl\{\\rl\{([^}]*)\}\}', r'\\rl{\1}', content)

            # fix ultrathick
            content = content.replace('ultrathick', 'ultra thick')
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
