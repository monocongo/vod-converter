import pathlib
from setuptools import setup

# the directory containing this file
BASE_DIR = pathlib.Path(__file__).parent

# the text of the README file
README = (BASE_DIR / "README.md").read_text()

setup(
    name="vod-converter",
    version="1.0.0",
    url="https://github.com/monocongo/vod-converter",
    license="MIT",
    author="James Adams",
    author_email="monocongo@gmail.com",
    description=(
        "Converts between visual object dataset formats."
    ),
    long_description=README,
    long_description_content_type="text/markdown",
    packages=["vod_converter"],
    include_package_data=True,
    install_requires=[
    ],
    tests_require=["pytest"],
    test_suite="tests",
    keywords=["object detection", "kitti", "pascal voc",],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    entry_points={
        "console_scripts": [
            "vod_converter=vod_converter.main:main",
        ]
    },
)
