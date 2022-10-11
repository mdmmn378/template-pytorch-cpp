from setuptools import setup
from setuptools import Extension
from torch.utils.cpp_extension import BuildExtension, CppExtension
from torch.utils import cpp_extension

setup(
    name='activations',  # Should match the macro of pybind
    ext_modules=[
        CppExtension('activations', ['src/main.cpp']),
    ],
    cmdclass={
        'build_ext': BuildExtension
    })

# ext_modules = Extension(
#    name='activations-tool',
#    sources=['src/main.cpp'],
#    include_dirs=cpp_extension.include_paths(),
#    language='c++')

# setup(
#     name='activations',
#     ext_modules=[ext_modules],
#     cmdclass={
#         'build_ext': BuildExtension
#     })