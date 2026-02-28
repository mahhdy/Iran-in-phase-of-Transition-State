import os
import re

directories = ['chapters', 'appendices']

# 1. replace `text centered` with `align=center`
for d in directories:
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith('.tex'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                content = content.replace('text centered,', 'align=center,')
                content = content.replace('text centered', 'align=center')
                
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(content)

# 2. add text width if minimum width is present
def repl(m):
    val = m.group(1)
    return f"minimum width={val}, text width={val}"

for d in directories:
    for root, dirs, files in os.walk(d):
        for f in files:
            if f.endswith('.tex'):
                path = os.path.join(root, f)
                with open(path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                content = re.sub(r'minimum width=([0-9.]+cm)(?!\s*,\s*text width)', repl, content)
                content = re.sub(r'minimum size=([0-9.]+cm)(?!\s*,\s*text width)', lambda m: f"minimum size={m.group(1)}, text width={m.group(1)}", content)
                
                with open(path, 'w', encoding='utf-8') as file:
                    file.write(content)
