import os
import re

src_dir = "src"

for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith(".npk"):
            filepath = os.path.join(root, file)
            with open(filepath, "r") as f:
                content = f.read()
            
            # Replace ptr->field with (<-ptr).field
            new_content = re.sub(r'\b([a-zA-Z0-9_]+)->([a-zA-Z0-9_]+)\b', r'(<-\1).\2', content)
            
            if new_content != content:
                with open(filepath, "w") as f:
                    f.write(new_content)
