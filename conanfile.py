from conan import ConanFile
from conan.tools.cmake import CMake, cmake_layout, CMakeToolchain
from conan.tools.files import apply_conandata_patches, export_conandata_patches, copy, get, rmdir
import os

class fiberpool_Conan(ConanFile):
    name = "fiberpool"
    version = "0.1"

    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "examples*", "include*", "tests*", "CMakeLists.txt"

    description="C++17 Fiberpool"
    url = "https://github.com/ulricheck/fiberpool.git"

    default_options = {
        "Boost/*:without_fiber": False,
    }

    requires = (
        "boost/1.81.0",
        )

    def layout(self):
        cmake_layout(self)

    def generate(self):
        tc = CMakeToolchain(self)
        tc.generate()

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        copy(self, pattern="*.hpp", dst=os.path.join(self.package_folder, "include"), src=os.path.join(self.source_folder, "include"))

    def package_id(self):
        self.info.clear()

