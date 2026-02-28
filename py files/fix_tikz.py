import os
import re

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Replace \rl{...}\\{\tiny ...} with \begin{tabular}{c}\rl{...}\\{\tiny \rl{...}}\end{tabular}
            content = re.sub(r'\\rl{([^}]*)}\\\\\{\\tiny\s*([^}]*)\}', r'\\begin{tabular}{c}\\rl{\1}\\\\{\\tiny \\rl{\2}}\\end{tabular}', content)
            
            # Replace \rl{...}\\[Xcm]\rl{\tiny ...} 
            content = re.sub(r'\\rl{([^}]*)}\\\\\[([^\]]*)\]\\rl\{\\tiny\s*([^}]*)\}', r'\\begin{tabular}{c}\\rl{\1}\\\\\[\2]\\rl{\\tiny \3}\\end{tabular}', content)

            # Same logic for \rl{...}\\\rl{\tiny ...}
            content = re.sub(r'\\rl{([^}]*)}\\\\\\rl\{\\tiny\s*([^}]*)\}', r'\\begin{tabular}{c}\\rl{\1}\\\\{\\tiny \\rl{\2}}\\end{tabular}', content)

            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

