import os

def str_to_bool(val: str | None, default: bool = False) -> bool:
    if val is None:
        return default
    return val.lower() in ("true", "1", "yes")

ENABLE_NLP = str_to_bool(
    os.getenv("ENABLE_NLP"),
    default=False
)

ENABLE_AUDIO_CLEANUP = str_to_bool(
    os.getenv("ENABLE_AUDIO_CLEANUP"),
    default=False
)

AUDIO_TTL_HOURS = int(
    os.getenv("AUDIO_TTL_HOURS", "24")
)
