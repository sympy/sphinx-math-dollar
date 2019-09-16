import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

import versioneer

setuptools.setup(
    name="sphinx-math-dollar",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    author="Aaron Meurer",
    author_email="asmeurer@gmail.com",
    description="Sphinx extension to let you write LaTeX math using $$",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sympy/sphinx-math-dollar/",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires= '>=3.6',
    install_requires=[
        'sphinx'
    ],
    license='MIT',
)
