import os
import glob
import subprocess

out_file = "/home/randy/Workspace/META/NPARSE/audits/a10/compilation.md"
src_dir = "/home/randy/Workspace/REPOS/nparse/src"

with open(out_file, "w") as f:
    for root, _, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".npk"):
                path = os.path.join(root, file)
                rel_path = os.path.relpath(path, src_dir)
                f.write(f"\n# File: src/{rel_path}\n```nitpick\n")
                with open(path, "r") as src_f:
                    f.write(src_f.read())
                f.write("\n```\n")

    f.write("\n# Build Output\n```\n")
    try:
        result = subprocess.run(["npkc", "src/main.npk"], cwd="/home/randy/Workspace/REPOS/nparse", capture_output=True, text=True)
        f.write(result.stdout)
        f.write(result.stderr)
    except Exception as e:
        f.write(str(e))
    f.write("\n```\n")
print("Compilation file generated successfully!")
