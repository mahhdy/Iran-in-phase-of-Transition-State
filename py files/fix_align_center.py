import os

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            content = content.replace('text centered', 'align=center')
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# Also update in preamble.tex
with open('preamble.tex', 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace('text centered', 'align=center')
with open('preamble.tex', 'w', encoding='utf-8') as file:
    file.write(content)
