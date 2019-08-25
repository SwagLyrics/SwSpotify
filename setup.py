import os
from codecs import open
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

here = os.path.abspath(os.path.dirname(__file__))
about = {}
with open(os.path.join(here, 'SwSpotify', '__version__.py'), 'r', 'utf-8') as f:
    exec(f.read(), about)

setuptools.setup(
    name=about['__title__'],
    version=about['__version__'],
    author=about['__author__'],
    author_email=about['__author_email__'],
    description=about['__description__'],
    license=about['__license__'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=about['__url__'],
    packages=setuptools.find_packages(),
    install_requires=[
        'pywin32; platform_system=="Windows"',
        'pyobjc; platform_system=="Darwin"',
        'pydbus; platform_system=="Linux"'
    ],
    keywords='spotify swaglyrics python app',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
