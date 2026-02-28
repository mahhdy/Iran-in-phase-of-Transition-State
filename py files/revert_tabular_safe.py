import os
import re

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Revert \begin{tabular}{c} ... \end{tabular} to just the content
            # BUT only if it occurs inside a \node block!
            # Since my additions were always single line: \begin{tabular}{c}\rl{...}\\ \tiny \rl{...}\end{tabular}
            # Or similar. We will just search non-greedily without DOTALL
            
            def replace_tabular(match):
                inner = match.group(1)
                # Ensure it only contains \rl and \tiny and \\ and spaces/brackets
                if '\\rl{' in inner and '\\\\' in inner:
                    return inner
                return match.group(0)

            content = re.sub(r'\\begin\{tabular\}\{c\}(.*?)\\end\{tabular\}', replace_tabular, content)
            
            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)
