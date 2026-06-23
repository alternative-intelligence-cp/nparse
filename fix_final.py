with open("src/api/builder.npk", "r") as f:
    text = f.read()

text = text.replace('ctx->precedence = npk_precedence_table_create(256i32);', 'ctx->precedence = raw npk_precedence_table_create(256i32);')

with open("src/api/builder.npk", "w") as f:
    f.write(text)


with open("src/lexer/dfa_lexer.npk", "r") as f:
    text = f.read()

text = text.replace('pass(<-( @ptr_add<int32>(table, idx) ));', 'wild int32->:table_ptr = table;\n        pass(<-( @ptr_add<int32>(table_ptr, idx) ));')

with open("src/lexer/dfa_lexer.npk", "w") as f:
    f.write(text)
