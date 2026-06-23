import os

task_file = "/home/randy/.gemini/antigravity/brain/e2b5d10a-3a6b-4d01-9618-9562a7b06b1d/task.md"

with open(task_file, "r") as f:
    content = f.read()

mods_to_check = ["MOD-005", "MOD-006", "MOD-007", "MOD-008", "MOD-009", "MOD-013", "MOD-016"]
for mod in mods_to_check:
    content = content.replace(f"- `[ ]` **{mod}:**", f"- [x] **{mod}:**")

with open(task_file, "w") as f:
    f.write(content)

print("Checked off remaining tasks.")
