with open("src/api/builder.npk", "r") as f:
    text = f.read()

text = text.replace("alloc(@sizeof(GrammarCtx))", "alloc(24i64)")
text = text.replace("ctx->precedence = npk_precedence_table_create(256i32);", "ctx->precedence = raw npk_precedence_table_create(256i32);")

with open("src/api/builder.npk", "w") as f:
    f.write(text)

