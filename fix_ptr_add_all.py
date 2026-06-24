import os
import re
import glob

def fix_ptr_add():
    files = glob.glob("src/**/*.npk", recursive=True)
    pattern = re.compile(r'@ptr_add<([A-Za-z0-9_]+)>\(([^,]+),\s*([^)]+)\)')
    
    for file in files:
        with open(file, 'r') as f:
            content = f.read()
            
        new_content = pattern.sub(r'@cast_unchecked<\1->>(@cast_unchecked<int64>(\2) + (@cast_unchecked<int64>(\3) * @sizeof(\1)))', content)
        
        if new_content != content:
            with open(file, 'w') as f:
                f.write(new_content)
            print(f"Fixed {file}")

if __name__ == "__main__":
    fix_ptr_add()
