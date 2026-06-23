import os
import subprocess
import glob

output_file = "/home/randy/Workspace/META/NPARSE/audit/a8/compilation.md"

files = glob.glob("src/**/*.npk", recursive=True)

with open(output_file, "w") as f:
    for file in sorted(files):
        f.write(f"### {file}\n")
        f.write("```nitpick\n")
        with open(file, "r") as src_f:
            f.write(src_f.read())
        f.write("\n```\n\n")
        
    f.write("### Build Output\n")
    f.write("```\n")
    result = subprocess.run(
        ["npkc", "-I", "src", "src/main.npk", "--verify"],
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )
    f.write(result.stdout)
    f.write("\n```\n")
    
print(f"Generated {output_file}")
