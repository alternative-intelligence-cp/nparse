import os
import re

base_dir = "/home/randy/Workspace/REPOS/nparse/src/parsers"
for filename in ["toml_parser.npk", "json_parser.npk"]:
    filepath = os.path.join(base_dir, filename)
    with open(filepath, "r") as f:
        content = f.read()
    
    # 1. Replace array<int64, N> with array<int32, N>
    content = re.sub(r'array<int64,\s*(\d+)>', r'array<int32, \1>', content)
    
    # 2. Remove => int64 casts inside the arrays
    content = content.replace(" => int64", "")
    
    # 3. Replace @@name => int64 with @cast_unchecked<wild int32[]->>(@name)
    # Wait, the audit says: Replace @@kv_seq => int64 with @cast_unchecked<wild int32[]->>(@kv_seq)
    # The regex for @@var => int64 (since => int64 is already removed above, it will just be @@var)
    # Wait, actually, let's just replace @@(\w+) with @cast_unchecked<wild int32[]->>(@\1)
    content = re.sub(r'@@(\w+)', r'@cast_unchecked<wild int32[]->>(@\1)', content)
    
    with open(filepath, "w") as f:
        f.write(content)

print("Replaced combinators arrays and @@ in parsers.")
