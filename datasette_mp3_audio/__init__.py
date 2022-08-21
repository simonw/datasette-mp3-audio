from datasette import hookimpl
from markupsafe import Markup, escape


@hookimpl
def extra_js_urls(columns, datasette):
    if not columns:
        return None
    return [
        datasette.urls.static_plugins("datasette-mp3-audio", "datasette-mp3-audio.js")
    ]


@hookimpl
def render_cell(value):
    if not isinstance(value, str):
        return
    if value.endswith(".mp3") and (
        value.startswith("http://")
        or value.startswith("https://")
        or value.startswith("/")
    ):
        return Markup(
            f'<audio controls src="{escape(value)}"><a href="{escape(value)}">Download MP3</a></audio>'
        )
