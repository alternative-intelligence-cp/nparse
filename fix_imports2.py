import os
import re

src_dir = "src"

for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith(".npk"):
            filepath = os.path.join(root, file)
            with open(filepath, "r") as f:
                content = f.read()
            
            # Replace use X.Y.*; with use "X/Y.npk".*;
            content = re.sub(r'use ([a-z_]+)\.([a-z_]+)\.\*;', r'use "\1/\2.npk".*;', content)
            # Replace use X.Y.Z; with use "X/Y.npk".Z;
            content = re.sub(r'use ([a-z_]+)\.([a-z_]+)\.([A-Za-z_]+);', r'use "\1/\2.npk".\3;', content)
            
            with open(filepath, "w") as f:
                f.write(content)
