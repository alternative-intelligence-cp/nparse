import os

task_file = "/home/randy/.gemini/antigravity/brain/e2b5d10a-3a6b-4d01-9618-9562a7b06b1d/task.md"

with open(task_file, "r") as f:
    content = f.read()

mods_to_check = ["MOD-003", "MOD-004", "MOD-010", "MOD-011", "MOD-012", "MOD-014", "MOD-015"]
for mod in mods_to_check:
    content = content.replace(f"- `[ ]` **{mod}:**", f"- [x] **{mod}:**")

with open(task_file, "w") as f:
    f.write(content)

print("Checked off completed tasks.")
