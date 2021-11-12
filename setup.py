import setuptools
import os

with open(os.path.join(os.path.dirname(os.path.realpath(__file__)), "README.md"), "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="weirdcipher",
    version="__version__",
    author="Federico A. Galatolo",
    author_email="federico.galatolo@ing.unipi.it",
    description="",
    url="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    entry_points = {
        "console_scripts": [
            "weirdcipher=weirdcipher.__main__:main",
        ],
    },
    install_requires=[
        "numpy>=1.21.4"
    ],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta"
    ],
)