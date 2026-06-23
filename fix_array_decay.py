import re
import sys

files = ["src/parsers/json_parser.npk", "src/parsers/toml_parser.npk"]

for filepath in files:
    with open(filepath, "r") as f:
        content = f.read()
    
    new_content = content
    # Replace the specific array usages with @
    targets = ["member_seq", "obj_seq", "arr_seq", "val_choice", "kv_seq", "th_seq", "entry_choice", "doc_seq"]
    
    for t in targets:
        new_content = new_content.replace(f"{t} => int64", f"@{t} => int64")
        
    if new_content != content:
        with open(filepath, "w") as f:
            f.write(new_content)
