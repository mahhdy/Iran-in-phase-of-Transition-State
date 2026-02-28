import os
import re

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # replace {\tiny \rl{...}} with \tiny \rl{...}
            # because the {} braces might confuse tabular parser!
            content = re.sub(r'\\\{\\tiny\s*([^}]+)\}', r'\\ \tiny \1', content)
            # Wait, the string was \{\tiny \rl{...}}
            # So { \tiny \rl { ... } }
            # Actually just search for \{\tiny \rl{ and replace with \tiny \rl{ and remove the trailing }
            # A safer regex:
            # We want to replace exactly \{\tiny \rl{...}}
            content = re.sub(r'\{\\tiny\s*\\rl\{([^}]*)\}\}', r'\\tiny \\rl{\1}', content)
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
