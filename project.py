import os
from pathlib import Path

from pyqtbuild import PyQtBindings, PyQtProject


class PyQt6Ads(PyQtProject):
    def __init__(self):
        super().__init__()
        self.bindings_factories = [PyQt6Adsmod]
        self.verbose = bool(os.getenv("CI") or os.getenv("CIBUILDWHEEL"))

    def apply_user_defaults(self, tool):
        if tool == "sdist":
            return super().apply_user_defaults(tool)
        qmake_path = "bin/qmake"
        if os.name == "nt":
            qmake_path += ".exe"
        try:
            qmake_bin = str(next(Path(self.root_dir).rglob(qmake_path)).absolute())
        except StopIteration:
            raise RuntimeError(
                "qmake not found.\n"
                "Please run `uvx --from aqtinstall aqt install-qt ...`"
            )
        print(f"USING QMAKE: {qmake_bin}")
        self.builder.qmake = qmake_bin
        return super().apply_user_defaults(tool)

    def build_wheel(self, wheel_directory):
        # use lowercase name for wheel, for
        # https://packaging.python.org/en/latest/specifications/binary-distribution-format/
        self.name = self.name.lower()
        return super().build_wheel(wheel_directory)


class PyQt6Adsmod(PyQtBindings):
    def __init__(self, project):
        super().__init__(project, "PyQt6Ads")

    def apply_user_defaults(self, tool):
        resource_file = os.path.join(
            self.project.root_dir, "Qt-Advanced-Docking-System", "src", "ads.qrc"
        )
        self.builder_settings.append("RESOURCES += " + resource_file)
        super().apply_user_defaults(tool)
