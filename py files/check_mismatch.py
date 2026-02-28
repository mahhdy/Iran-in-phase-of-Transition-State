import os
import re

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Find all nodes.  \node[options] (...) {text\\text};
            # Specifically, look for `\node[...` containing `\\` but NOT containing `align=` or `text width=` or `text centered` in the options directly.
            # Also, some nodes might be using a style that lacks `align=center`.
            # To be 100% safe, if a node has `\\`, just ensure it gets `align=center`.
            # BUT we ONLY want to inject it if it's missing in the OPTIONS block.
            # What if `align=center` is in the style? It doesn't hurt to add it again.
            
            # Regex to find: \node[...](...){...\\...}
            # Or just \node[...]{...\\...}
            
            # Actually, another error was `\begin{center}` ended by `\end{tikzpicture}`.
            # Look at my log snippet earlier:
            # > ! LaTeX Error: \begin{center} on input line 809 ended by \end{tikzpicture}.
            # Let's fix that one too!
            
            # Let's write a simple script to find the \begin{center} mismatch first.
            if 'ch13-economy.tex' in path:
                # Need to find line 809 in ch13-economy.tex
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if '\\begin{center}' in line:
                        pass
        
