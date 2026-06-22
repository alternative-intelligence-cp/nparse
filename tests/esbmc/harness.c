#include <assert.h>
#include <stdint.h>
#include <stdlib.h>

// Mock of the NPARSE execution loop for ESBMC Bounded Model Checking
extern void* npk_arena_create(int64_t initial_capacity);
extern struct ParseResult npk_parse(int64_t g, void* src_data, int64_t src_len, uint32_t max_depth);

struct ParseResult { int32_t tag; union { void* node; int32_t err; } payload; };

void simulate_adversarial_grammar() {
    int64_t grammar_id = 1;
    char adversarial_input[15]; // Bounded stream up to depth 15
    
    // Nondeterministic input for ESBMC
    for(int i = 0; i < 15; i++) {
        adversarial_input[i] = (char) nondet_int();
    }
    
    // We expect the parser to return deterministically without panicking
    // even with garbage input.
    struct ParseResult result = npk_parse(grammar_id, adversarial_input, 15, 10);
    
    // Safety property: tag is either 0 (Success) or 1 (Error), but we never trapped
    assert(result.tag == 0 || result.tag == 1);
}

int main() {
    simulate_adversarial_grammar();
    return 0;
}
