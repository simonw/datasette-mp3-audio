from datasette.app import Datasette
import pytest
import sqlite_utils


@pytest.mark.asyncio
@pytest.mark.parametrize(
    "value,expect_audio",
    (
        (1, False),
        (1.2, False),
        (None, False),
        ("dog", False),
        ("no_slash.mp3", False),
        ("/has_slash.mp3", True),
        ("https://blah/has_url.mp3", True),
        ("http://blah/has_url.mp3", True),
    ),
)
async def test_mp3_audio(value, expect_audio):
    datasette = Datasette(memory=True)
    db = datasette.add_memory_database("test")

    def setup(conn):
        sqlite_utils.Database(conn)["demo"].insert({"value": value})

    await db.execute_write_fn(setup, block=True)

    response = await datasette.client.get("/test/demo")
    assert response.status_code == 200
    html = response.text
    if expect_audio:
        assert (
            f'<audio controls src="{value}"><a href="{value}">Download MP3</a></audio>' in html
        )
    else:
        assert "<audio " not in html
