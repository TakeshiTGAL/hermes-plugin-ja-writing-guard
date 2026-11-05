"""Load the repo root as a package, the way Hermes loads an installed plugin directory."""

from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent.parent
PACKAGE = "ja_writing_guard_plugin"


def load_plugin():
    if PACKAGE in sys.modules:
        return sys.modules[PACKAGE]
    spec = importlib.util.spec_from_file_location(
        PACKAGE, PLUGIN_DIR / "__init__.py", submodule_search_locations=[str(PLUGIN_DIR)]
    )
    module = importlib.util.module_from_spec(spec)
    sys.modules[PACKAGE] = module
    spec.loader.exec_module(module)
    return module


def load_module(name: str):
    """Import one plugin submodule. The name has to be one of the fixed modules below."""
    load_plugin()
    if name == "detector":
        return importlib.import_module("ja_writing_guard_plugin.detector")
    if name == "rules":
        return importlib.import_module("ja_writing_guard_plugin.rules")
    if name == "surfaces":
        return importlib.import_module("ja_writing_guard_plugin.surfaces")
    if name == "rewrite":
        return importlib.import_module("ja_writing_guard_plugin.rewrite")
    if name == "hook":
        return importlib.import_module("ja_writing_guard_plugin.hook")
    if name == "tools":
        return importlib.import_module("ja_writing_guard_plugin.tools")
    raise ImportError(name)


def load_detector():
    return load_module("detector")
