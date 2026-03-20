import click

from youtube_transcriber.transcriber import transcribe_youtube


@click.command()
@click.argument("youtube_url")
def main(youtube_url: str) -> None:
    """Transcribe a YouTube video's audio with timestamps.

    The model can be overridden via the GEMINI_MODEL environment variable.
    """
    click.echo(transcribe_youtube(youtube_url))
