#include <stdint.h>
#include <stdlib.h>

// ---------------------------------------------------------
// NPARSE C-ABI Backend Stubs
// These functions correspond to the `extern "nitpick_nparse_sys"`
// declarations in the Nitpick frontend.
// ---------------------------------------------------------

// --- Memory/Arena ---
void* npk_arena_create(int64_t initial_capacity) { return NULL; }
void npk_arena_destroy(void* arena) {}
struct Handle { int32_t index; int32_t generation; };
struct Handle npk_arena_push(void* arena, void* node) { struct Handle h = {0,0}; return h; }
void* npk_arena_get(void* arena, struct Handle handle) { return NULL; }

// --- Memory/TLC ---
void* npk_tlc_alloc(int64_t size) { return NULL; }
void* npk_tlc_alloc_red_node() { return NULL; }
void npk_tlc_flush() {}

// --- Hash Consing ---
struct Handle npk_hash_cons_push(int64_t hash_map_ptr, void* arena, void* node) {
    struct Handle h = {0,0}; return h;
}

// --- Lexer ---
struct Lexer { void* source_data; int64_t source_len; int64_t cursor; };
struct Token { int32_t k; int32_t l; int32_t lt; int32_t tt; int64_t off; };
struct Lexer npk_lexer_init(void* source_data, int64_t source_len) {
    struct Lexer l = {source_data, source_len, 0}; return l;
}
int32_t npk_lexer_transition(int32_t current_state, int8_t byte) { return 0; }
int32_t npk_lexer_consume_trivia(void* lexer) { return 0; }
struct Token npk_lexer_next_token(void* lexer) { struct Token t = {0,0,0,0,0}; return t; }

// --- API Builder ---
int64_t npk_grammar_create() { return 0; }
void npk_grammar_destroy(int64_t grammar_ptr) {}
void npk_grammar_bind(int64_t g, int32_t rule_id, int32_t ast_node_kind) {}

// --- Combinators ---
int32_t npk_rule_token(int64_t g, int32_t token_kind) { return 0; }
int32_t npk_rule_seq(int64_t g, int64_t* rule_ids_ptr, int32_t count) { return 0; }
int32_t npk_rule_choice(int64_t g, int64_t* rule_ids_ptr, int32_t count) { return 0; }
int32_t npk_rule_repeat(int64_t g, int32_t rule_id, int32_t min_matches) { return 0; }
int32_t npk_rule_optional(int64_t g, int32_t rule_id) { return 0; }
int32_t npk_rule_infix(int64_t g, int32_t tk, int32_t prec, int8_t right) { return 0; }
int32_t npk_rule_prefix(int64_t g, int32_t tk, int32_t prec) { return 0; }
int32_t npk_rule_pratt_expr(int64_t g, int64_t* pr, int32_t pc, int64_t* ir, int32_t ic) { return 0; }

// --- Execution & Security ---
struct ParseResult { int32_t tag; union { void* node; int32_t err; } payload; };
struct ParseResult npk_parse(int64_t g, void* src_data, int64_t src_len, uint32_t max_depth) {
    struct ParseResult r = {0}; return r;
}
struct ParseResult npk_memoize_get(int64_t cache, int32_t rule_id, int64_t offset) {
    struct ParseResult r = {0}; return r;
}
void npk_memoize_set(int64_t cache, int32_t rule_id, int64_t offset, struct ParseResult res) {}
int8_t npk_prove_progress(int64_t cursor_before, int64_t cursor_after) { return cursor_after > cursor_before; }

// --- Error Recovery ---
struct ParseResult npk_recover_create_error_node(int64_t arena_ptr, int64_t bad_token_ptr) {
    struct ParseResult r = {0}; return r;
}
int32_t npk_recover_sync_forward(int64_t lexer_ptr, int32_t* sync_tokens, int32_t sync_count) { return 0; }

// --- Precedence Tables ---
void* npk_precedence_table_create(int32_t max_token_id) { return NULL; }
void npk_precedence_table_set(void* tbl, int32_t tid, int32_t pwr, int8_t assoc) {}
int32_t npk_precedence_table_get_power(void* tbl, int32_t tid) { return 0; }
int8_t npk_precedence_table_get_assoc(void* tbl, int32_t tid) { return 0; }

// --- Plugin Loader & Hooks ---
int64_t npk_plugin_load(const char* path) { return 0; }
void npk_plugin_unload(int64_t handle) {}
int64_t npk_plugin_get_symbol(int64_t handle, const char* symbol) { return 0; }
void npk_hook_register_enter(int64_t g, int32_t kind, int64_t cb) {}
void npk_hook_register_exit(int64_t g, int32_t kind, int64_t cb) {}
