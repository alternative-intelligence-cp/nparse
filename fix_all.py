with open("src/memory/tlc.npk", "r") as f:
    text = f.read()
text = text.replace('int8->:res = tlc->bump_ptr;', 'wild int8->:res = tlc->bump_ptr;')
text = text.replace('int8->:res_slow = tlc->bump_ptr;', 'wild int8->:res_slow = tlc->bump_ptr;')
text = text.replace('int8->:buf;', 'wild int8->:buf;')
text = text.replace('int8->:bump_ptr;', 'wild int8->:bump_ptr;')
with open("src/memory/tlc.npk", "w") as f:
    f.write(text)

with open("src/api/builder.npk", "r") as f:
    text = f.read()
text = text.replace('int64(int64:g', 'int64(wild GrammarHandle->:g')
text = text.replace('int32(int64:g', 'int32(wild GrammarHandle->:g')
text = text.replace('NIL(int64:g', 'NIL(wild GrammarHandle->:g')
text = text.replace('pub func:npk_grammar_create = int64()', 'pub func:npk_grammar_create = wild GrammarHandle->()')
text = text.replace('int64:g = @cast_unchecked<int64>(alloc(65536i64)); // allocate 64KB for grammar\n        <-@cast_unchecked<int32->>(g) = 0i32; // initial rule count\n        pass(g);', 'wild GrammarCtx->:ctx = @cast_unchecked<GrammarCtx->>(alloc(24i64));\n        ctx->rule_count = 1i32;\n        ctx->rules = @cast_unchecked<RuleNode->>(calloc(4096i32, 24i64));\n        ctx->precedence = npk_precedence_table_create(256i32);\n        pass(@cast_unchecked<wild GrammarHandle->>(ctx));')
text = text.replace('pub func:npk_grammar_destroy = NIL(int64:grammar_ptr)', 'pub func:npk_grammar_destroy = NIL(wild GrammarHandle->:grammar_ptr)')
with open("src/api/builder.npk", "w") as f:
    f.write(text)

with open("src/api/combinators.npk", "r") as f:
    text = f.read()
text = text.replace('int32(int64:g', 'int32(wild GrammarHandle->:g')
with open("src/api/combinators.npk", "w") as f:
    f.write(text)

