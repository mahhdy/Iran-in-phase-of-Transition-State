import os

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as f_in:
                content = f_in.read()
            
            # replace step/.style with my_step/.style
            content = content.replace('step/.style=', 'my_step/.style=')
            content = content.replace('step/.style =', 'my_step/.style=')
            # replace node[step] with node[my_step]
            content = content.replace('node[step]', 'node[my_step]')
            content = content.replace('node[step,', 'node[my_step,')
            content = content.replace('node[step=', 'node[my_step=')
            
            with open(path, 'w', encoding='utf-8') as f_out:
                f_out.write(content)
