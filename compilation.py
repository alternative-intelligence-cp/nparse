import os, subprocess
out = []
out.append('# NPARSE A39 Compilation\n\n')
files_to_add = [
    'src/main.npk',
    'src/engine/context.npk',
    'src/engine/execute.npk',
    'src/engine/recovery.npk',
    'src/lexer/dfa_lexer.npk',
    'src/core/token.npk',
    'src/core/source_map.npk',
    'src/core/green_node.npk',
    'src/core/red_node.npk',
    'src/core/precedence.npk',
    'src/memory/handle.npk',
    'src/memory/arena.npk',
    'src/memory/hash_consing.npk',
    'src/memory/tlc.npk',
    'src/api/builder.npk',
    'src/api/combinators.npk',
    'src/parsers/json_parser.npk',
    'src/parsers/toml_parser.npk',
    'src/main.npk',
    'src/plugins/loader.npk',
    'src/plugins/hooks.npk'
]

out.append('## 1. Compiler Output\n')
try:
    res = subprocess.run(['/home/randy/Workspace/REPOS/nitpick/build/npkc', '-I', 'src', '--verify', 'src/main.npk'], capture_output=True, text=True)
    out.append(f'Exit Code: {res.returncode}\n')
    if res.returncode == 0:
        out.append('SUCCESS\n')
    else:
        out.append('ERROR\n')
        out.append(res.stderr)
        out.append(res.stdout)
except Exception as e:
    pass

out.append('\n## 2. Source Files\n')
for f in files_to_add:
    if os.path.exists(f):
        out.append(f'\n### {f}\n```nitpick\n')
        with open(f, 'r') as fp:
            out.append(fp.read())
        out.append('\n```\n')

with open('/home/randy/Workspace/META/NITPICK/audits/a39/compilation.md', 'w') as f:
    f.write(''.join(out))
