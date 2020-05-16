import setuptools
import SwSpotify

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SwSpotify",
    version=SwSpotify.__version__,
    author="Aadi Bajpai",
    author_email="swspotify@swaglyrics.dev",
    description="Get currently playing song and artist from Spotify faster without using the API.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SwagLyrics/SwSpotify",
    packages=['SwSpotify'],
    install_requires=['flask==1.1.2', 'requests==2.23.0', 'flask-cors==3.0.8', 'pywin32; platform_system=="Windows"',
                      'pyobjc; platform_system=="Darwin"'],
    extras_require={
        'dev': [
            'mock',
            'pytest',
            'pytest-cov'
        ]
    },
    keywords='spotify swaglyrics python app',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
