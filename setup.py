import setuptools

with open("README.rst", "r") as fh:
    long_description = fh.read()

import versioneer

setuptools.setup(
    name="sphinx-math-dollar",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="SymPy Development Team",
    author_email="sympy@googlegroups.com",
    description="Sphinx extension to let you write LaTeX math using $$",
    long_description=long_description,
    url="https://github.com/sympy/sphinx-math-dollar/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # python_requires= '>=3.6',
    install_requires=[
        'sphinx'
    ],
    license='MIT',
)
