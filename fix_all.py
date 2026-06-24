import os
import re

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Ensure use "unsafe.npk".*;
    if '@ptr_add' in content and 'use "unsafe.npk".*;' not in content:
        content = 'use "unsafe.npk".*;\n' + content

    # Fix @ptr_add(sm->line_starts, ...) -> wild int64->:ls = sm->line_starts; @ptr_add(ls, ...)
    # But wait, we can just replace @ptr_add with the old cast to see if it works, or fix the wild pointer issue.
    # The A15-2.1 specifically asks: "Rewrite all pointer arithmetic using the builtin @ptr_add<T>(ptr, offset)."
    # If the compiler throws NITPICK-PTRARITH-STACK on `tail_chunk->buf`, it's because it's an expression.
    # We should extract them to local wild pointers before @ptr_add.
    
    # Or maybe the compiler bug is just complaining because of missing "wild".
    # Let's fix them manually in Python.
    
    lines = content.split('\n')
    for i in range(len(lines)):
        if '@ptr_add' in lines[i]:
            # Extract the first argument
            m = re.search(r'@ptr_add<([^>]+)>\(([^,]+),\s*(.+?)\)', lines[i])
            if m:
                t = m.group(1)
                ptr_exp = m.group(2).strip()
                offset = m.group(3).strip()
                if not re.match(r'^[a-zA-Z0-9_]+$', ptr_exp):
                    # It's an expression like sm->line_starts or arena->generations
                    var_name = "temp_ptr_" + str(i)
                    lines[i] = lines[i].replace(f'@ptr_add<{t}>({ptr_exp},', f'@ptr_add<{t}>({var_name},')
                    lines[i] = f'        wild {t}->:{var_name} = {ptr_exp};\n' + lines[i]

    content = '\n'.join(lines)
    with open(filepath, 'w') as f:
        f.write(content)

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
        fix_file(file)

print("Fixed files.")
