import os
import subprocess

out_file = "/home/randy/Workspace/META/NPARSE/audits/a10/compilation.md"

with open(out_file, "w") as out:
    for root, _, files in os.walk("src"):
        for file in files:
            if file.endswith(".npk"):
                path = os.path.join(root, file)
                out.write(f"--- FILE: {path} ---\n")
                with open(path, "r") as f:
                    out.write(f.read())
                out.write("\n\n")

    out.write("--- BUILD OUTPUT ---\n")

subprocess.run(["npkc", "src/main.npk"], stdout=open("build_out.txt", "w"), stderr=subprocess.STDOUT)

with open(out_file, "a") as out:
    with open("build_out.txt", "r") as f:
        out.write(f.read())

import shutil
shutil.copy(out_file, "/home/randy/Workspace/META/NPARSE/audit/a10/compilation.md")
