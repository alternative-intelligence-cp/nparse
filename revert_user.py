with open("src/memory/tlc.npk", "r") as f:
    text = f.read()

text = text.replace("tlc->tail->next", "(<-(tlc->tail)).next")
text = text.replace("tlc->tail->buf", "(<-(tlc->tail)).buf")

with open("src/memory/tlc.npk", "w") as f:
    f.write(text)
