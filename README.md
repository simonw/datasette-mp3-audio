# datasette-mp3-audio

[![PyPI](https://img.shields.io/pypi/v/datasette-mp3-audio.svg)](https://pypi.org/project/datasette-mp3-audio/)
[![Changelog](https://img.shields.io/github/v/release/simonw/datasette-mp3-audio?include_prereleases&label=changelog)](https://github.com/simonw/datasette-mp3-audio/releases)
[![Tests](https://github.com/simonw/datasette-mp3-audio/workflows/Test/badge.svg)](https://github.com/simonw/datasette-mp3-audio/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-mp3-audio/blob/main/LICENSE)

Turn .mp3 URLs into an audio player in the Datasette interface

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-mp3-audio

## Usage

Usage instructions go here.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-mp3-audio
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
