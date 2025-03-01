import os
from pathlib import Path
import subprocess

from pyqtbuild import PyQtBindings, PyQtProject

ROOT = Path(__file__).parent
ADS_DIR = ROOT / "Qt-Advanced-Docking-System"


def get_ads_version():
    """Get the version from the Qt-Advanced-Docking-System git tags"""
    # Run git describe in the submodule directory
    try:
        result = subprocess.run(
            ["git", "describe", "--tags"],
            cwd=str(ADS_DIR),
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except subprocess.CalledProcessError:
        raise RuntimeError(
            "Failed to get version from Qt-Advanced-Docking-System git tags"
        )


class PyQt6Ads(PyQtProject):
    def __init__(self):
        super().__init__()
        self.bindings_factories = [PyQt6Adsmod]

    def setup(self, pyproject, tool, tool_description):
        super().setup(pyproject, tool, tool_description)
        self.version_str = get_ads_version()

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
        resource_file = str(ADS_DIR / "src" / "ads.qrc")
        self.builder_settings.append("RESOURCES += " + resource_file)
        super().apply_user_defaults(tool)
