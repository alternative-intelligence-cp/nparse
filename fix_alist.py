with open("src/engine/execute.npk", "r") as f:
    text = f.read()

text = text.replace("apush(1i64);", "apush(parse_stack, 1i64);")
text = text.replace("while (asize() > 0i64) {", "while (asize(parse_stack) > 0i64) {")
text = text.replace("int64:action = apop();", "int64:action = apop(parse_stack);")
text = text.replace("if (asize() > @cast_unchecked<int64>(max_recursion_depth)) {", "if (asize(parse_stack) > @cast_unchecked<int64>(max_recursion_depth)) {")

with open("src/engine/execute.npk", "w") as f:
    f.write(text)
