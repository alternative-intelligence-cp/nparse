import re

def fix_builder():
    with open("src/api/builder.npk", "r") as f:
        text = f.read()

    text = text.replace(
        "wild RuleNode->:rules_ptr = ctx->rules;\n        wild RuleNode->:r = @cast_unchecked<RuleNode->>(@ptr_add<int8>(@cast_unchecked<int8->>(rules_ptr), (@cast_unchecked<int64>(rule_id) * 24i64)));",
        "wild int8->:rules_ptr_bytes = @cast_unchecked<int8->>(ctx->rules);\n        wild RuleNode->:r = @cast_unchecked<RuleNode->>(@ptr_add<int8>(rules_ptr_bytes, @cast_unchecked<int64>(rule_id) * 24i64));"
    )

    text = text.replace(
        "wild RuleNode->:rules_ptr = ctx->rules;\n        wild RuleNode->:fwd = @cast_unchecked<RuleNode->>(@ptr_add<int8>(@cast_unchecked<int8->>(rules_ptr), (@cast_unchecked<int64>(fwd_rule_id) * 24i64)));\n        wild RuleNode->:act = @cast_unchecked<RuleNode->>(@ptr_add<int8>(@cast_unchecked<int8->>(rules_ptr), (@cast_unchecked<int64>(actual_rule_id) * 24i64)));",
        "wild int8->:rules_ptr_bytes = @cast_unchecked<int8->>(ctx->rules);\n        wild RuleNode->:fwd = @cast_unchecked<RuleNode->>(@ptr_add<int8>(rules_ptr_bytes, @cast_unchecked<int64>(fwd_rule_id) * 24i64));\n        wild RuleNode->:act = @cast_unchecked<RuleNode->>(@ptr_add<int8>(rules_ptr_bytes, @cast_unchecked<int64>(actual_rule_id) * 24i64));"
    )
    with open("src/api/builder.npk", "w") as f:
        f.write(text)

def fix_execute():
    with open("src/engine/execute.npk", "r") as f:
        text = f.read()

    text = text.replace(
        "wild RuleNode->:r = @cast_unchecked<RuleNode->>(@ptr_add<int8>(@cast_unchecked<int8->>(rules_ptr), (@cast_unchecked<int64>(rule_id) * 24i64)));",
        "wild int8->:rules_ptr_bytes = @cast_unchecked<int8->>(rules_ptr);\n                    wild RuleNode->:r = @cast_unchecked<RuleNode->>(@ptr_add<int8>(rules_ptr_bytes, @cast_unchecked<int64>(rule_id) * 24i64));"
    )
    with open("src/engine/execute.npk", "w") as f:
        f.write(text)

fix_builder()
fix_execute()
