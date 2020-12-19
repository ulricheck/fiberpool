from conans import ConanFile, tools, CMake

class fiberpool_Conan(ConanFile):
    name = "fiberpool"
    version = "0.1"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "examples*", "include*", "tests*", "CMakeLists.txt"

    description="C++17 Fiberpool"
    url = "https://github.com/ulricheck/fiberpool.git"

    default_options = {
        "Boost:without_fiber": False,
    }

    requires = (
        "Boost/1.72.0@camposs/stable",
        )


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="*.hpp", dst="include", src="include")

    def package_id(self):
        self.info.header_only()

