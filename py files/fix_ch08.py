import os

path = 'chapters/ch08-phase1.tex'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# 'step' is a reserved pgf/tikz key for steps in grids or lists, using it as a style name causes:
# Package pgfkeys Error: The key '/tikz/step' requires a value.
content = content.replace('step/.style', 'my_step/.style')
content = content.replace('node[step]', 'node[my_step]')
content = content.replace('node[step,', 'node[my_step,')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
