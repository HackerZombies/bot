# (c) @UniBorg
# Original written by @UniBorg edit by @INF1N17Y

from telethon import events
import asyncio
from collections import deque


@borg.on(events.NewMessage(pattern=r".hq", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("🤣-<—< 🤣-<—< 🤣-<—< 🤣-<—<"))
	for _ in range(100000000):
		await asyncio.sleep(0.1)
		await event.edit("".join(deq))
		deq.rotate(1)
    
