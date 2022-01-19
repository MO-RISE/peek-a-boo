"""Peek-a-boo: A simple dockerized service exposing a videofeed through
WebRTC via a HTTP frontend"""
import atexit
import logging

import uvicorn
from environs import Env
from vidgear.gears.asyncio import WebGear_RTC

env = Env()
SOURCE = env("SOURCE")
FRAME_SIZE_REDUCTION = env.float("FRAME_SIZE_REDUCTION", 20)
LOG_LEVEL = env.log_level("LOG_LEVEL", "WARNING")

# Set logging level
logging.basicConfig(level=LOG_LEVEL)

# Set some available options
options = {
    "frame_size_reduction": FRAME_SIZE_REDUCTION,
    "enable_live_broadcast": True,
}

# initialize WebGear_RTC app
web = WebGear_RTC(source=SOURCE, logging=True, **options)

# close app safely
atexit.register(web.shutdown)

# Run
uvicorn.run(web(), host="0.0.0.0", port=8000)
