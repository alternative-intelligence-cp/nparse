import os

for root, _, files in os.walk('src'):
    for f in files:
        if f.endswith('.npk'):
            path = os.path.join(root, f)
            with open(path, 'r') as fp:
                content = fp.read()
            if '@ptr_add' in content and 'use "unsafe.npk".*;' not in content:
                print(f"Adding to {path}")
                # Insert right after the first `use` or at the top
                lines = content.splitlines(True)
                new_lines = []
                inserted = False
                for line in lines:
                    new_lines.append(line)
                    if line.startswith('use ') and not inserted:
                        new_lines.append('use "unsafe.npk".*;\n')
                        inserted = True
                if not inserted:
                    new_lines.insert(0, 'use "unsafe.npk".*;\n')
                with open(path, 'w') as fp:
                    fp.writelines(new_lines)
