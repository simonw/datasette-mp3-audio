# datasette-mp3-audio

[![PyPI](https://img.shields.io/pypi/v/datasette-mp3-audio.svg)](https://pypi.org/project/datasette-mp3-audio/)
[![Changelog](https://img.shields.io/github/v/release/simonw/datasette-mp3-audio?include_prereleases&label=changelog)](https://github.com/simonw/datasette-mp3-audio/releases)
[![Tests](https://github.com/simonw/datasette-mp3-audio/workflows/Test/badge.svg)](https://github.com/simonw/datasette-mp3-audio/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/datasette-mp3-audio/blob/main/LICENSE)

Turn .mp3 URLs into an audio player in the Datasette interface

## Installation

Install this plugin in the same environment as Datasette.

    datasette install datasette-mp3-audio

## Demo

Try this plugin out in [Datasette Lite](https://lite.datasette.io/) here:

- [ScotRail announcements demo](https://lite.datasette.io/?install=datasette-mp3-audio&csv=https://gist.githubusercontent.com/simonw/0a30d52feeb3ff60f7d8636b0bde296b/raw/c078a9e5a0151331e2e46c04c1ebe7edc9f45e8c/scotrail-announcements.csv#/data/scotrail-announcements?_facet=Category)

The demo uses ScotRail train announcements from [matteason/scotrail-announcements-june-2022](https://github.com/matteason/scotrail-announcements-june-2022).

## Usage

Once installed, any cells with a value that ends in `.mp3` and starts with either `http://` or `/` or `https://` will be turned into an embedded HTML audio element like this:

```html
<audio controls src="... value ...">Audio not supported</audio>
```

A "Play X MP3s on this page" button will be added to athe top of any table page listing more than one MP3.

## Development

To set up this plugin locally, first checkout the code. Then create a new virtual environment:

    cd datasette-mp3-audio
    python3 -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
