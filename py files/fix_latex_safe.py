import os
import re

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Safe replacement for \rl{\rl{ ... }}
            # using regex that captures whatever is inside \rl{\rl{ ... }} 
            # as long as it doesn't contain a closing brace before the end of the text.
            # But the best way is recursive parse or just replacing \rl{\rl{ if we know
            # what's inside has exactly no brackets, or using re.sub with cautious pattern.
            content = re.sub(r'\\rl\{\\rl\{([^}]*)\}\}', r'\\rl{\1}', content)

            # fix ultrathick
            content = content.replace('ultrathick', 'ultra thick')
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
