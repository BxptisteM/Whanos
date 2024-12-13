from pathlib import Path


def jenkins_var(key: str, value: str) -> None:
    ansible_dir = Path("ansible")
    group_vars_file = ansible_dir / "group_vars/jenkins.yml"

    group_vars_file.parent.mkdir(parents=True, exist_ok=True)
    group_vars_file.touch(exist_ok=True)

    if group_vars_file.exists():
        with open(group_vars_file, "r") as f:
            lines = f.readlines()
    else:
        lines = []

    new_var_line = f'{key}: "{value}"\n'

    updated = False
    for i, line in enumerate(lines):
        if line.startswith(key):
            lines[i] = new_var_line
            updated = True
            break

    if not updated:
        lines.append(new_var_line)

    with open(group_vars_file, "w") as f:
        f.writelines(lines)
