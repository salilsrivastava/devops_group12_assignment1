#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
# use_plugin("python.coverage")           ##to be uncommented
use_plugin("python.distutils")


name = "devops_flask"
default_task = "publish"


@init
def set_properties(project):
    project.build_depends_on("flask")
    project.set_property("dir_source_main_python", "src/main")
    project.set_property("dir_source_unittest_python", "src/unittest")
