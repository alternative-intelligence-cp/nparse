with open("src/core/precedence.npk", "r") as f:
    text = f.read()
text = text.replace("@sizeof(PrecedenceTable)", "24i64")
with open("src/core/precedence.npk", "w") as f:
    f.write(text)

with open("src/memory/tlc.npk", "r") as f:
    text = f.read()
text = text.replace("@sizeof(TlcChunk)", "32i64")
text = text.replace("@sizeof(ThreadLocalCache)", "24i64")
with open("src/memory/tlc.npk", "w") as f:
    f.write(text)
