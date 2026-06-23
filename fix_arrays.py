import re

files = ["src/parsers/json_parser.npk", "src/parsers/toml_parser.npk"]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()
    
    # Replace int64[N]: with array<int64, N>:
    new_content = re.sub(r'int64\[([0-9]+)\]:', r'array<int64, \1>:', content)
    
    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
