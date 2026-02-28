import os
import re

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Revert \begin{tabular}{c} ... \end{tabular} to just the content
            # The regex is r'\\begin\{tabular\}\{c\}(.*?)\\end\{tabular\}'
            # But we must be careful not to replace actual tables! 
            # Our tabulars are always inside \{ ... \} or { ... } of a \node.
            # And they contain exactly the text and \\ and \tiny and \rl.
            
            def replace_tabular(match):
                inner = match.group(1)
                # Ensure it only contains \rl and \tiny and \\ and spaces/brackets
                if '\\rl{' in inner or 'tiny' in inner:
                    return inner
                return match.group(0)

            content = re.sub(r'\\begin\{tabular\}\{c\}(.*?)\\end\{tabular\}', replace_tabular, content, flags=re.DOTALL)
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
