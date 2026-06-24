import os
import re

files = [
    'src/core/source_map.npk',
    'src/memory/arena.npk',
    'src/memory/hash_consing.npk',
    'src/lexer/dfa_lexer.npk',
    'src/memory/tlc.npk',
    'src/engine/execute.npk',
    'src/engine/recovery.npk'
]

for file in files:
    if os.path.exists(file):
        with open(file, 'r') as f:
            content = f.read()
        
        # Replace `wild TYPE->:temp_ptr_` with `wildx TYPE->:temp_ptr_`
        content = re.sub(r'wild\s+([a-zA-Z0-9_]+->:temp_ptr_)', r'wildx \1', content)
        
        with open(file, 'w') as f:
            f.write(content)

print("Fixed wildx.")
