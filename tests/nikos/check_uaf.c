#include <assert.h>
#include <stdint.h>
#include <stdlib.h>

extern void* npk_arena_create(int64_t initial_capacity);
extern void npk_arena_destroy(void* arena);
extern void* npk_tlc_alloc(int64_t size);
extern void npk_tlc_flush();

// NIKOS LLVM20 Abstract Interpretation Harness
// Goal: Prove that flushing the TLC does not cause Use-After-Free in the main Arena
void harness_uaf_check() {
    void* arena = npk_arena_create(1024);
    
    // Simulate Semantic Pass
    void* ephemeral_node = npk_tlc_alloc(32);
    
    // Flush TLC (frees ephemeral nodes)
    npk_tlc_flush();
    
    // NIKOS will verify that destroying the arena here doesn't double-free
    // or trigger UAF on memory that was already reclaimed by TLC flush.
    npk_arena_destroy(arena);
}

int main() {
    harness_uaf_check();
    return 0;
}
