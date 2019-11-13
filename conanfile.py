from conans import ConanFile, tools, CMake

class fiberpool_Conan(ConanFile):
    name = "fiberpool"
    version = "0.1"
    generators = "cmake"
    settings = "os", "compiler", "build_type", "arch"
    exports_sources = "examples*", "include*", "tests*", "CMakeLists.txt"

    description="C++17 Fiberpool"

    default_options = {
        "Boost:without_fiber": False,
    }

    requires = (
        "Boost/1.70.0@camposs/stable",
        )


    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()

    def package(self):
        self.copy(pattern="*.h", dst="include", src="include")
        self.copy(pattern="*.h", dst="include", src="3rdParty/RTSPClient/include")
        self.copy(pattern="*.h", dst="include", src="3rdParty/RTSPServer/include")
        self.copy(pattern="*.so", dst="lib", keep_path=False)
        self.copy(pattern="*.lib", dst="lib", keep_path=False)
        self.copy(pattern="*.dll", dst="bin", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)

