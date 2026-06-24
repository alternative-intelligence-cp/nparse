import re

with open("src/api/combinators.npk", "r") as f:
    code = f.read()

pattern = r'wild RuleNode->:node = @cast_unchecked<RuleNode->>\(@cast_unchecked<int64>\(ctx->rules\) \+ \(@cast_unchecked<int64>\(idx\) \* @sizeof\(RuleNode\)\)\);'
replacement = """wild int8->:rules_base = @cast_unchecked<int8->>(ctx->rules);
        wild RuleNode->:node = @cast_unchecked<RuleNode->>(@ptr_add<int8>(rules_base, @cast_unchecked<int64>(idx) * 80i64));"""

code = re.sub(pattern, replacement, code)

with open("src/api/combinators.npk", "w") as f:
    f.write(code)
