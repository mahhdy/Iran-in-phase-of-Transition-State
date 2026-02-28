import os
import re

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Find all style definitions: something/.style={...}
            # Inside it, if there is minimum width=(value), and align=center or text centered
            # we should add text width=(value)
            
            def replace_style(match):
                inner = match.group(0)
                if 'minimum width=' in inner and 'text width=' not in inner:
                    m = re.search(r'minimum width=([^,]+)', inner)
                    if m:
                        val = m.group(1).strip()
                        inner = inner.replace('minimum width=' + val, f'minimum width={val},\n        text width={val}')
                return inner

            content = re.sub(r'[a-zA-Z0-9_-]+/\.style=\{[^}]+\}', replace_style, content)
            
            # Special case for nodes that have `minimum width` in their options directly
            # ex: \node[actor, minimum width=4cm, ...]
            # Let's just blindly add text width when minimum width is set?
            content = re.sub(r'minimum width=([^,}]+)', r'minimum width=\1, text width=\1', content)
            # Remove duplicated text width if any
            content = re.sub(r'text width=([^,}]+)(,\n?\s*text width=\1)+', r'text width=\1', content)

            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# Also update in preamble.tex
with open('preamble.tex', 'r', encoding='utf-8') as file:
    content = file.read()
content = re.sub(r'minimum width=([^,}]+)', r'minimum width=\1, text width=\1', content)
content = re.sub(r'text width=([^,}]+)(,\n?\s*text width=\1)+', r'text width=\1', content)
with open('preamble.tex', 'w', encoding='utf-8') as file:
    file.write(content)
