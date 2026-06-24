import re

with open("src/memory/tlc.npk", "r") as f:
    code = f.read()

code = code.replace("int64:cursor;", "wild int8->:bump_ptr;\n    int64:bytes_remaining;")

code = code.replace("""        tlc->head = @cast_unchecked<?->>(first);
        tlc->tail = @cast_unchecked<?->>(first);
        tlc->cursor = 0i64;
        tlc->chunk_capacity = cap;""", """        tlc->head = @cast_unchecked<?->>(first);
        tlc->tail = @cast_unchecked<?->>(first);
        tlc->bump_ptr = first->buf;
        tlc->bytes_remaining = cap;
        tlc->chunk_capacity = cap;""")

alloc_body = """        if (size <= 0i64) { fail(4i32); }
        if (size > 1073741824i64) { fail(1i32); }
        int64:aligned_size = (size + 7i64) & (~7i64);
        
        if (aligned_size <= tlc->bytes_remaining) {
            wild int8->:res = tlc->bump_ptr;
            tlc->bump_ptr = @ptr_add<int8>(res, aligned_size);
            tlc->bytes_remaining = tlc->bytes_remaining - aligned_size;
            pass(@cast_unchecked<?->>(res));
        }
        
        wild TlcChunk->:t_tail = @cast_unchecked<TlcChunk->>(tlc->tail);
        wild TlcChunk->:next_chunk = @cast_unchecked<TlcChunk->>(t_tail->next);
        
        if (next_chunk != NULL && aligned_size <= tlc->chunk_capacity) {
            tlc->tail = @cast_unchecked<?->>(next_chunk);
            tlc->bump_ptr = next_chunk->buf;
            tlc->bytes_remaining = tlc->chunk_capacity;
        } else {
            int64:cap = tlc->chunk_capacity;
            if (aligned_size > cap) { cap = aligned_size; }
            wild TlcChunk->:new_chunk = @cast_unchecked<TlcChunk->>(alloc(40i64));
            new_chunk->buf = @cast_unchecked<int8->>(alloc(cap));
            wild TlcChunk->:t_tail_new = @cast_unchecked<TlcChunk->>(tlc->tail);
            new_chunk->next = t_tail_new->next;
            
            t_tail_new->next = @cast_unchecked<?->>(new_chunk);
            tlc->tail = @cast_unchecked<?->>(new_chunk);
            tlc->bump_ptr = new_chunk->buf;
            tlc->bytes_remaining = cap;
        }
        
        wild int8->:res2 = tlc->bump_ptr;
        tlc->bump_ptr = @ptr_add<int8>(res2, aligned_size);
        tlc->bytes_remaining = tlc->bytes_remaining - aligned_size;
        pass(@cast_unchecked<?->>(res2));"""

code = re.sub(r'        if \(size <= 0i64\) \{ \!\!\! 4i32; \}.*?pass\(@cast_unchecked<\?->>\(res\)\);\n', alloc_body + "\n", code, flags=re.DOTALL)

code = code.replace("!!!", "fail")

with open("src/memory/tlc.npk", "w") as f:
    f.write(code)
