import asyncio
import re
import time
from time import sleep
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register

@register(outgoing=True, pattern='^.fl(?: |$)(.*)')
async def typewriter(typew):
	message = typew.pattern_match.group(1)
	await typew.edit("Sedang Memulai. Silahkan Tunggu")
	sleep(1)
	await typew.edit("0%")
	number = 1
	await typew.edit(str(number) + "% 
Loading... \n▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n█████████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n██████████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████████▊")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n███████████████▉")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████████████")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████████████▎")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████████████▍")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████████████▌")
	number = number+ 1
	sleep(0.01)
	await typew.edit(str(number) + "% 
Loading... \n████████████████▌")
	sleep(1)
	await typew.edit("Ngapain Lu Nungguin Sih Cok")
	






