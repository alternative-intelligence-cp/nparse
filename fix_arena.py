import re

with open("src/memory/arena.npk", "r") as f:
    code = f.read()

code = code.replace("wild GreenNode->:dst = @cast_unchecked<wild GreenNode->>(@cast_unchecked<int8->>(@cast_unchecked<int64>(data_base) + (@cast_unchecked<int64>(idx * 32i64) * @sizeof(int8))));", "wild GreenNode->:dst = @cast_unchecked<GreenNode->>(@ptr_add<int8>(data_base, idx * 32i64));")

code = code.replace("pass(@cast_unchecked<wild GreenNode->>(@cast_unchecked<int8->>(@cast_unchecked<int64>(data_base) + (@cast_unchecked<int64>(idx * 32i64) * @sizeof(int8)))));", "pass(@cast_unchecked<GreenNode->>(@ptr_add<int8>(data_base, idx * 32i64)));")

code = code.replace("wild int8->:data_base = @cast_unchecked<wild int8->>(arena->data);", "wild int8->:data_base = @cast_unchecked<int8->>(arena->data);")

with open("src/memory/arena.npk", "w") as f:
    f.write(code)
