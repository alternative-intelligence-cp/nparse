# nparse

Nitpick Native Parsing, Lexing, and Abstract Syntax Tree (AST) Engine/Library.

**Nparse** is a unified, professional-grade parsing engine built for the maturing Nitpick ecosystem. It provides a foundational library to parse various languages, configuration formats, and DSLs with excellent error tolerance and incremental parsing capabilities.

## Architecture Highlights

- **Red/Green Tree Architecture**: Follows industry gold standards (Tree-sitter, Roslyn, rust-analyzer) to implement Lossless Concrete Syntax Trees (CST).
  - **Green Tree**: Immutable, structurally shared, bottom-up tree that captures everything including whitespace, comments, and invalid tokens.
  - **Red Tree**: Ephemeral, top-down facade providing absolute byte offsets and parent pointers for semantic analysis.
- **High-Performance Memory Management**: Uses Generational Handles (`Handle<Node>`) backed by arenas to eliminate use-after-free bugs during the parsing phases.
- **Zero-Copy Slicing**: Relies entirely on `StrView` for token text during the initial analysis phase without heap-allocating substrings.
- **Stateful/Modal Lexing Engine**: Capable of switching contexts efficiently, combined with a Thompson NFA regex engine backend (`nregx`) for robust pattern matching.
- **Parser Combinators & Pratt Parsing**: Provides a deterministic C-ABI compatible API to build grammar combinators programmatically and handle expression operator precedence flawlessly.
- **Error Tolerance and Synchronization**: Implements robust error recovery through synchronization tokens instead of failing abruptly on the first syntax error.

## Use Cases

Nparse serves as the parsing backend for:
- Standard formats like JSON and TOML
- The Nitpick language compiler and LSP (Language Server Protocol) implementation
- Formatting, refactoring, and code analysis tools within the Nitpick ecosystem

## License

This project is licensed under the [LICENSE](LICENSE) provided in the repository.


---

## Nitpick Ecosystem

This repository is part of the [Nitpick](https://github.com/alternative-intelligence-cp/nitpick) ecosystem. 
- 🌍 **[Nitpick-Lang Hub](https://github.com/alternative-intelligence-cp/nitpick-lang)** — The central hub connecting all Nitpick projects.
- 📖 **[Official Web Documentation](https://ai-liberation-platform.org/nitpick/docs/)** — Guides, references, and language specifications.
- 🛠️ **[Nitpick Compiler](https://github.com/alternative-intelligence-cp/nitpick)** — The core language and toolchain.
