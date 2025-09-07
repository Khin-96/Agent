import logging
import webbrowser
from typing import Optional
from livekit.agents import function_tool, RunContext
from ytmusicapi import YTMusic

# ✅ Initialize YTMusic (anonymous mode)
ytmusic = YTMusic()

# 🎵 Keep track of last played song
last_played = {"song": None, "url": None}

@function_tool()
async def play_music(ctx: RunContext, song: str, platform: Optional[str] = "ytmusic") -> str:
    """Play a song on YouTube Music without announcing it."""
    global last_played
    try:
        logging.debug(f"Searching YouTube Music for: {song}")
        results = ytmusic.search(song, filter="songs")
        if results:
            video_id = results[0]["videoId"]
            url = f"https://music.youtube.com/watch?v={video_id}"
            webbrowser.open(url)
            last_played["song"] = song
            last_played["url"] = url
            # Return empty string instead of announcement
            return ""
        else:
            return f"Um, sorry, I couldn't find '{song}'."
    except Exception as e:
        logging.error(f"Error playing music: {e}")
        return f"Uh, error playing music: {str(e)}"

@function_tool()
async def pause_music(ctx: RunContext) -> str:
    """Pause music without announcing it."""
    if last_played["song"]:
        # Return empty string - the action speaks for itself
        return ""
    return "No music is currently playing."

@function_tool()
async def resume_music(ctx: RunContext) -> str:
    """Resume music without announcing it."""
    if last_played["url"]:
        webbrowser.open(last_played["url"])
        # Return empty string
        return ""
    return "No song to resume."

@function_tool()
async def stop_music(ctx: RunContext) -> str:
    """Stop music without announcing it."""
    global last_played
    if last_played["song"]:
        last_played = {"song": None, "url": None}
        # Return empty string
        return ""
    return "No music is currently playing."