from datasette import hookimpl
from markupsafe import Markup, escape


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
            '<audio controls src="{}">Audio not supported</audio>'.format(escape(value))
        )
