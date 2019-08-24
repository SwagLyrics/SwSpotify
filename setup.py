import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SwSpotify",
    version="1.0.0",
    author="Aadi Bajpai",
    author_email="swspotify@aadibajpai.me",
    description="Get currently playing song and artist from Spotify faster without using the API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SwagLyrics/SwSpotify",
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