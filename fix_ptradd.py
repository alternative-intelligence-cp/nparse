import re

def fix_file(path):
    with open(path, "r") as f:
        text = f.read()

    # match lines like: wild RuleNode->:X = @ptr_add<RuleNode>(rules_ptr, offset);
    # and replace with: wild RuleNode->:X = @cast_unchecked<RuleNode->>(@ptr_add<int8>(@cast_unchecked<int8->>(rules_ptr), offset * 24i64));
    
    text = re.sub(r'(@ptr_add<RuleNode>\(([^,]+),\s*)([^)]+)(\))', r'@cast_unchecked<RuleNode->>(@ptr_add<int8>(@cast_unchecked<int8->>(\2), (\3) * 24i64))', text)
    
    with open(path, "w") as f:
        f.write(text)

fix_file("src/api/builder.npk")
fix_file("src/engine/execute.npk")

