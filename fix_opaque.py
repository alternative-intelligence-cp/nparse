with open("src/api/builder.npk", "r") as f:
    text = f.read()
text = text.replace('pub opaque:GrammarHandle;', 'pub struct:GrammarHandle = {};')
with open("src/api/builder.npk", "w") as f:
    f.write(text)

import re
import glob

def fix_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    pattern = re.compile(r'(@ptr_add<([^>]+)>\s*\(\s*)([a-zA-Z0-9_]+->[a-zA-Z0-9_\.]+)(\s*,\s*)(.*?)\)')
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        m = pattern.search(line)
        if m:
            type_str = m.group(2)
            expr = m.group(3)
            var_name = expr.replace('->', '_').replace('.', '_')
            indent = line[:len(line) - len(line.lstrip())]
            decl = f"{indent}wild {type_str}->:{var_name} = {expr};"
            new_lines.append(decl)
            new_line = line[:m.start(3)] + var_name + line[m.end(3):]
            new_lines.append(new_line)
        else:
            new_lines.append(line)
    with open(filepath, 'w') as f:
        f.write('\n'.join(new_lines))

for f in glob.glob("src/**/*.npk", recursive=True):
    fix_file(f)
