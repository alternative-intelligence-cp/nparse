import os

src_dir = "src"

for root, dirs, files in os.walk(src_dir):
    for file in files:
        if file.endswith(".npk"):
            filepath = os.path.join(root, file)
            with open(filepath, "r") as f:
                content = f.read()
            
            new_content = content.replace("use nparse.", "use ")
            
            if new_content != content:
                with open(filepath, "w") as f:
                    f.write(new_content)
