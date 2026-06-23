with open("src/api/builder.npk", "r") as f:
    text = f.read()

struct_def = """use "core/precedence.npk".PrecedenceTable;
use "core/precedence.npk".npk_precedence_table_create;

pub struct:GrammarCtx = {
    int32:rule_count;
    wild RuleNode->:rules;
    wild PrecedenceTable->:precedence;
};
"""

text = struct_def + "\n" + text

with open("src/api/builder.npk", "w") as f:
    f.write(text)

