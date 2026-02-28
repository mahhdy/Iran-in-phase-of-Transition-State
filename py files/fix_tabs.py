import os

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # fix tab + iny
            content = content.replace('\tiny ', '\\tiny ')
            content = content.replace('\tiny', '\\tiny')
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
