import os
import subprocess

out_file = "/home/randy/Workspace/META/NITPICK/audits/a40/compilation.md"
src_dir = "src"

with open(out_file, "w") as out:
    out.write("# NPARSE Source Compilation (A2)\n\n")
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.endswith(".npk"):
                filepath = os.path.join(root, file)
                out.write(f"### {filepath}\n")
                out.write("```\n")
                with open(filepath, "r") as f:
                    out.write(f.read())
                if not out.tell() == 0 and not out.tell() == '\n':
                    out.write("\n")
                out.write("```\n\n")

    out.write("## Build Output\n")
    out.write("```\n")

# Run compiler
try:
    find_proc = subprocess.Popen(["find", "src", "-name", "*.npk"], stdout=subprocess.PIPE)
    files = find_proc.stdout.read().split()
    compiler_path = "/home/randy/Workspace/REPOS/nitpick/build/npkc"
    cmd = [compiler_path, "-I", "src", "--verify", "src/main.npk"]
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
    with open(out_file, "a") as out:
        out.write(res.stdout)
except Exception as e:
    with open(out_file, "a") as out:
        out.write(str(e))

with open(out_file, "a") as out:
    out.write("\n```\n")
