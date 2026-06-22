#!/usr/bin/env python3
import z3

# Z3 SMT Solver Hook for Nitpick Compiler Integration
# Goal: Prove the core progress invariant `cursor_after > cursor_before`
# so the LLVM backend can strip out infinite-loop bounds checks.

def prove_progress_invariant():
    # Symbolic variables representing lexer state
    cursor_before = z3.Int('cursor_before')
    cursor_after = z3.Int('cursor_after')
    token_length = z3.Int('token_length')

    s = z3.Solver()

    # Domain constraints: cursor is non-negative, token lengths are strictly positive (>0)
    s.add(cursor_before >= 0)
    s.add(token_length > 0)
    
    # State transition: cursor advances by token length
    s.add(cursor_after == cursor_before + token_length)

    # Invariant to prove: cursor_after > cursor_before
    invariant = (cursor_after > cursor_before)

    # To prove an invariant, we check if its negation is satisfiable
    s.push()
    s.add(z3.Not(invariant))
    
    if s.check() == z3.unsat:
        print("Z3 PROOF SUCCESS: cursor_after > cursor_before holds true.")
        print("COMPILER_OPT: ENABLE_ELISION")
        return True
    else:
        print("Z3 PROOF FAILED: Infinite loop possible.")
        print("Counterexample:", s.model())
        return False

if __name__ == "__main__":
    prove_progress_invariant()
