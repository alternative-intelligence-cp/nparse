import re

with open("src/lexer/dfa_lexer.npk", "r") as f:
    content = f.read()

# Replace `<-@ptr_add<T>(ptr, offset)`
def ptr_repl(m):
    t = m.group(1)
    ptr = m.group(2)
    offset = m.group(3)
    return f"<-(@cast_unchecked<{t}->>(@cast_unchecked<int64>({ptr}) + (@cast_unchecked<int64>({offset}) * @sizeof({t}))))"

content = re.sub(r'<-\(@ptr_add<([a-zA-Z0-9_]+)>\(([^,]+),\s*([^)]+)\)\)', ptr_repl, content)
content = re.sub(r'<-@ptr_add<([a-zA-Z0-9_]+)>\(([^,]+),\s*([^)]+)\)', ptr_repl, content)

with open("src/lexer/dfa_lexer.npk", "w") as f:
    f.write(content)
