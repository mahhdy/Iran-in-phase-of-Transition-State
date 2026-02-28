import os
import re

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # The bug: `minimum width=XXX, text width=XXX`
            # We want to replace exactly that pattern back to `minimum width=XXX`.
            # XXX can contain anything.
            # Using lazy match `(.+?)`
            
            content = re.sub(r'minimum width=([^,]+?),\s*text width=\1', r'minimum width=\1', content)
            
            # Also, some might have been duplicated differently? Wait, my regex was:
            # content = re.sub(r'minimum width=([^,}]+)', r'minimum width=\1, text width=\1', content)
            # So the replacement is EXACTLY `, text width=\1`.
            # And then `content = re.sub(r'text width=([^,}]+)(,\n?\s*text width=\1)+', r'text width=\1', content)`
            
            content = re.sub(r'minimum width=([^}]+?)(,\s*text width=\1)+', r'minimum width=\1', content)
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# and for preamble:
with open('preamble.tex', 'r', encoding='utf-8') as file:
    content = file.read()
content = re.sub(r'minimum width=([^}]+?)(,\s*text width=\1)+', r'minimum width=\1', content)
with open('preamble.tex', 'w', encoding='utf-8') as file:
    file.write(content)
