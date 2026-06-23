import re

files = ["src/parsers/json_parser.npk", "src/parsers/toml_parser.npk"]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()
    
    # Replace array<int64, N>: with array<int32, N>:
    new_content = re.sub(r'array<int64, ([0-9]+)>:', r'array<int32, \1>:', content)
    
    # Remove => int64
    new_content = new_content.replace(' => int64', '')
    
    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
