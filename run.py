from pathlib import Path

ortools = Path("or-tools") / "ortools"
ortools_stubs = Path("ortools-stubs")


def touch_pyi(folder):
    if not (folder / "__init__.py").exists():
        return
    tmp = Path(ortools_stubs / "/".join(folder.parts[2:]))
    Path(tmp).mkdir(parents=True, exist_ok=True)
    Path(tmp / "__init__.pyi").touch()
    for f in folder.iterdir():
        if f.is_dir():
            touch_pyi(f)


if __name__ == "__main__":
    touch_pyi(ortools)
