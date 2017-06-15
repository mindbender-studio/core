"""This module holds state.

Modules in this package may modify state.

Erasing the contents of each container below will completely zero out
the currently held state of mindbender-core.

"""

_registered_formats = list()
_registered_plugins = dict()
_registered_plugin_paths = dict()
_registered_root = {"_": ""}
_registered_host = {"_": None}
