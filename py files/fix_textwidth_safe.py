import os
import re

for root, dirs, files in os.walk('chapters'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Simple approach: find all occurrences of `minimum width=NUMcm`
            # and replace with `minimum width=NUMcm, text width=NUMcm`
            # BUT make sure we don't duplicate if `text width` is ALREADY right next to it or soon after.
            # actually just replace `minimum width=([0-9.]+cm)` with `temp_width=\1` 
            # then replace `temp_width` back with `minimum width=..., text width=...`
            # Wait, what if someone wrote `minimum width=3cm, text width=3cm`? 
            # I can just strip existing `text width=[^,}]+` and then add it back!
            
            # 1. Clean existing text width if it is within a node options bracket [ ... ]
            # Actually, doing it via purely regex replacement of `minimum width`:
            def repl(m):
                val = m.group(1)
                # m.group(0) is `minimum width=2.4cm`
                # We return `minimum width=2.4cm, text width=2.4cm`
                return f"minimum width={val}, text width={val}"

            # Remove all `text width=...` that we might have added or was there 
            # (assuming they don't have complex values)
            # content = re.sub(r',\s*text width=[^,}]+', '', content)
            
            # BUT wait, some nodes ONLY had `text width`! I don't want to remove them.
            # Let's just find `minimum width` that does NOT have `text width` right after it.
            content = re.sub(r'minimum width=([0-9.]+cm)(?!\s*,\s*text width)', repl, content)

            with open(path, 'w', encoding='utf-8') as file:
                file.write(content)

# Same for preamble
path = 'preamble.tex'
with open(path, 'r', encoding='utf-8') as file:
    content = file.read()
content = re.sub(r'minimum width=([0-9.]+cm)(?!\s*,\s*text width)', lambda m: f"minimum width={m.group(1)}, text width={m.group(1)}", content)
with open(path, 'w', encoding='utf-8') as file:
    file.write(content)

