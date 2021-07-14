import admins
get
set

__all__ = ["set", "get", "admins"]
import clear 
import get
import is_empty
from queues import put
from queues import task_done

__all__ = ["clear", "get", "is_empty", "put", "task_done"]
from queues import clear 
from queues import get
from queues import is_empty
from queues import put
from queues import task_done

__all__ = ["clear", "get", "is_empty", "put", "task_done"]

from admins import admins
from admins import get
from admins import set

__all__ = ["set", "get", "admins"]

from pyrogram import Client

import config

client = Client(config.SESSION_NAME, config.API_ID, config.API_HASH)
run = client.run
