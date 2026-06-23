with open("src/memory/hash_consing.npk", "r") as f:
    content = f.read()

new_func = """pub func:hash_green_node = uint32(wild GreenNode->:node) {
    uint32:hash = FNV_OFFSET_BASIS;
    
    // Helper to mix a 32-bit integer byte-by-byte
    uint32:v_kind = @cast_unchecked<uint32>((<-node).kind);
    hash = hash ^ (v_kind & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_kind >> 8u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_kind >> 16u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_kind >> 24u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    
    uint32:v_width = @cast_unchecked<uint32>((<-node).width);
    hash = hash ^ (v_width & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_width >> 8u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_width >> 16u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_width >> 24u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    
    uint32:v_cc = @cast_unchecked<uint32>((<-node).child_count);
    hash = hash ^ (v_cc & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_cc >> 8u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    
    uint32:v_flags = @cast_unchecked<uint32>((<-node).flags);
    hash = hash ^ (v_flags & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_flags >> 8u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    
    uint32:v_fc_idx = (<-node).first_child.index;
    hash = hash ^ (v_fc_idx & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_fc_idx >> 8u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_fc_idx >> 16u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_fc_idx >> 24u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    
    uint32:v_fc_gen = (<-node).first_child.generation;
    hash = hash ^ (v_fc_gen & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_fc_gen >> 8u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_fc_gen >> 16u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_fc_gen >> 24u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    
    uint32:v_ns_idx = (<-node).next_sibling.index;
    hash = hash ^ (v_ns_idx & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_ns_idx >> 8u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_ns_idx >> 16u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_ns_idx >> 24u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    
    uint32:v_ns_gen = (<-node).next_sibling.generation;
    hash = hash ^ (v_ns_gen & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_ns_gen >> 8u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_ns_gen >> 16u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    hash = hash ^ ((v_ns_gen >> 24u32) & 255u32);
    hash = (((hash => uint64) * (FNV_PRIME => uint64)) & 0xFFFFFFFFu64) => uint32;
    
    pass(hash);
};"""

import re
content = re.sub(r'pub func:hash_green_node = uint32\(wild GreenNode->:node\) \{.*?\n\};\n', new_func + '\n', content, flags=re.DOTALL)

with open("src/memory/hash_consing.npk", "w") as f:
    f.write(content)
