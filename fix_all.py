import re
import os

def ptr_repl(m):
    t = m.group(1)
    ptr = m.group(2)
    offset = m.group(3)
    return f"<-(@cast_unchecked<{t}->>(@cast_unchecked<int64>({ptr}) + (@cast_unchecked<int64>({offset}) * @sizeof({t}))))"

for root, _, files in os.walk("src"):
    for file in files:
        if file.endswith(".npk"):
            path = os.path.join(root, file)
            with open(path, "r") as f:
                content = f.read()
            
            orig = content
            content = re.sub(r'<-\(@ptr_add<([a-zA-Z0-9_]+)>\(([^,]+),\s*([^)]+)\)\)', ptr_repl, content)
            content = re.sub(r'<-@ptr_add<([a-zA-Z0-9_]+)>\(([^,]+),\s*([^)]+)\)', ptr_repl, content)
            content = re.sub(r'@ptr_add<([a-zA-Z0-9_]+)>\(([^,]+),\s*([^)]+)\)', 
                lambda m: f"@cast_unchecked<{m.group(1)}->>(@cast_unchecked<int64>({m.group(2)}) + (@cast_unchecked<int64>({m.group(3)}) * @sizeof({m.group(1)})))", content)
            
            if content != orig:
                with open(path, "w") as f:
                    f.write(content)
                print(f"Fixed {path}")
