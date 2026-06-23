with open("src/engine/execute.npk", "r") as f:
    text = f.read()

text = text.replace("astack(4096i64);", "int64:parse_stack = alist(4096i64);")
text = text.replace("apush(parse_stack, 1i64);", "drop alpush(parse_stack, 1i64);")
text = text.replace("while (asize(parse_stack) > 0i64) {", "while (alsize(parse_stack) > 0i64) {")
text = text.replace("int64:action = apop(parse_stack);", "int64:action = alpop(parse_stack);")
text = text.replace("if (asize(parse_stack) > @cast_unchecked<int64>(max_recursion_depth)) {", "if (alsize(parse_stack) > @cast_unchecked<int64>(max_recursion_depth)) {")

with open("src/engine/execute.npk", "w") as f:
    f.write(text)
