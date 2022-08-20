from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-mp3-audio",
    description="Turn .mp3 URLs into an audio player in the Datasette interface",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-mp3-audio",
    project_urls={
        "Issues": "https://github.com/simonw/datasette-mp3-audio/issues",
        "CI": "https://github.com/simonw/datasette-mp3-audio/actions",
        "Changelog": "https://github.com/simonw/datasette-mp3-audio/releases",
    },
    license="Apache License, Version 2.0",
    classifiers=[
        "Framework :: Datasette",
        "License :: OSI Approved :: Apache Software License",
    ],
    version=VERSION,
    packages=["datasette_mp3_audio"],
    entry_points={"datasette": ["mp3_audio = datasette_mp3_audio"]},
    install_requires=["datasette"],
    extras_require={"test": ["pytest", "pytest-asyncio", "sqlite-utils"]},
    python_requires=">=3.7",
)
