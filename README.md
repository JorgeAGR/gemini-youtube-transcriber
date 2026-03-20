# gemini-youtube-transcriber

Transcribes YouTube videos using the Gemini API, exposed as both a Python library and an MCP server.

## Why Gemini?

Gemini has native, first-party access to YouTube — it can read and process a YouTube video directly from its URL, with no downloading, no intermediate storage, and no third-party tooling required. You pass a URL, Gemini watches the video (at FPS<1 and low-resolution to save on tokens, as this is an audio-centric task), and returns a transcription. This keeps the implementation minimal and the latency low.

## Output format

Each line of the transcription follows a consistent, machine-readable format:

```
MM:SS: <text>
```

When multiple speakers are distinguishable:

```
MM:SS: Speaker A: <text>
MM:SS: Speaker B: <text>
```

## Installation

```bash
pip install .
```

Requires a [Gemini API key](https://aistudio.google.com/apikey). Set it as an environment variable:

```bash
export GEMINI_API_KEY="your-key-here"
```

Optionally, override the Gemini model (default: `gemini-3-flash-preview`):

```bash
export GEMINI_MODEL="gemini-3.1-flash-lite-preview"
```

## Usage

### CLI

```bash
transcribe https://www.youtube.com/watch?v=...
```

### Python

```python
from youtube_transcriber import transcribe_youtube

transcript = transcribe_youtube("https://www.youtube.com/watch?v=...")
print(transcript)
```

### mcpb (Claude Desktop)

Download the latest `.mcpb` file from the [Releases](../../releases/latest) page and open it — Claude Desktop will install the extension automatically and prompt you for your Gemini API key.

### MCP server

```bash
python -m youtube_transcriber.server
```

Register in your MCP client config:

```json
{
  "mcpServers": {
    "youtube-transcriber": {
      "command": "python",
      "args": ["-m", "youtube_transcriber.server"],
      "env": {
        "GEMINI_API_KEY": "your-key-here",
        "GEMINI_MODEL": "gemini-3-flash-preview"
      }
    }
  }
}
```

The MCP tool `transcribe_youtube_video` accepts a YouTube URL and returns the full transcription string.

### mcpb

A `manifest.json` is included for one-click installation via [mcpb](https://mcpb.dev). mcpb will prompt you for your Gemini API key and handle the rest — no manual config editing required.

```bash
mcpb install .
```
