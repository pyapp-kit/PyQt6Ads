import os
from pathlib import Path
import subprocess

from pyqtbuild import PyQtBindings, PyQtProject

ROOT = Path(__file__).parent
ROOT = Path(__file__).parent
ADS_DIR = ROOT / "Qt-Advanced-Docking-System"


def get_ads_version():
    """Get the version from the Qt-Advanced-Docking-System git tags"""
    try:
        # Run git describe in the submodule directory
        result = subprocess.run(
            ["git", "describe", "--tags"],
            cwd=str(ADS_DIR),
            capture_output=True,
            text=True,
            check=True,
        )
        git_tag = result.stdout.strip()

        # Extract major.minor.patch from the git tag
        version_parts = git_tag.split(".")
        if len(version_parts) >= 3:
            # Extract only the numeric parts if needed
            major = version_parts[0].lstrip("v")
            minor = version_parts[1]
            patch = version_parts[2].split("-")[0]  # Remove any git hash suffix
            return f"{major}.{minor}.{patch}"
        else:
            # Fallback version if git tag format is unexpected
            return "4.2.1"  # Set a reasonable default
    except (subprocess.SubprocessError, IndexError):
        # Fallback version if git command fails
        return "4.2.1"  # Set a reasonable default


# Extract version once at module load time
ADS_VERSION = get_ads_version()

class PyQt6Ads(PyQtProject):
    def __init__(self):
        super().__init__()
        self.bindings_factories = [PyQt6Adsmod]

    def setup(self, pyproject, tool, tool_description):
        super().setup(pyproject, tool, tool_description)
        breakpoint()

    def apply_user_defaults(self, tool):
        if tool == "sdist":
            return super().apply_user_defaults(tool)
        qmake_path = "bin/qmake"
        if os.name == "nt":
            qmake_path += ".exe"
        try:
            qmake_bin = str(next(ROOT.rglob(qmake_path)).absolute())
        except StopIteration:
            raise RuntimeError(
                "qmake not found.\n"
                "Please run `uvx --from aqtinstall aqt install-qt <plat> "
                "desktop <qtversion> <arch> --outputdir Qt`"
            )
        self.builder.qmake = qmake_bin
        return super().apply_user_defaults(tool)


class PyQt6Adsmod(PyQtBindings):
    def __init__(self, project):
        super().__init__(project, "PyQt6Ads")

    def apply_user_defaults(self, tool):
        resource_file = os.path.join(
            self.project.root_dir, "Qt-Advanced-Docking-System", "src", "ads.qrc"
        )
        self.builder_settings.append("RESOURCES += " + resource_file)
        super().apply_user_defaults(tool)
