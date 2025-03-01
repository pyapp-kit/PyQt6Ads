"""Delocate wheel file."""

import re
import sys
from subprocess import run
from pathlib import Path
import shutil


def main() -> None:
    if sys.platform != "darwin":
        return

    dest_dir, wheel, *_ = sys.argv[1:]

    # unzip the wheel to a tmp directory
    tmp_dir = Path(wheel).parent / "tmp"
    shutil.unpack_archive(wheel, tmp_dir, format="zip")

    # fix the rpath in the tmp directory
    if sys.platform == "darwin":
        for so in Path(tmp_dir).rglob("*.so"):
            fix_rpath(so)

    # re-zip the tmp directory and place it at dest_dir / wheel.name
    new_wheel = Path(dest_dir) / Path(wheel).name
    shutil.make_archive(new_wheel, "zip", tmp_dir)
    # remove the .zip extension
    shutil.move(f"{new_wheel}.zip", new_wheel)
    assert new_wheel.exists()
    print("Placed the repaired wheel at", new_wheel)


RPATH_RE = re.compile(r"^\s*path (.+) \(offset \d+\)$", re.MULTILINE)


def fix_rpath(so: Path, new_rpath: str = "@loader_path/PyQt6/Qt6/lib") -> None:
    # delete all current rpaths
    current_rpath = run(["otool", "-l", str(so)], capture_output=True, text=True)
    for rpath in RPATH_RE.findall(current_rpath.stdout):
        run(["install_name_tool", "-delete_rpath", rpath, so], check=True)

    # add new rpath
    run(["install_name_tool", "-add_rpath", new_rpath, so], check=True)
    print(f"Updated RPATH for {so} to {new_rpath}")


if __name__ == "__main__":
    main()
