import os

for root, dirs, files in os.walk('.'):
    for f in files:
        if f.endswith('.tex'):
            path = os.path.join(root, f)
            with open(path, 'r', encoding='utf-8') as file:
                lines = file.readlines()
                if len(lines) >= 191:
                    line = lines[190]
                    if '\\rl{' in line or '\\\\' in line:
                        print(f"File: {path}, Line 191: {line.strip()}")
