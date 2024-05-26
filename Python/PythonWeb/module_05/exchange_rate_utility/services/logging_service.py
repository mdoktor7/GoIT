from aiofile import AIOFile
from aiopath import AsyncPath
import datetime
from constants import LOG_FILE_PATH


class LoggingService:
    def __init__(self, log_file_path=None):
        self.log_file_path = log_file_path or LOG_FILE_PATH

    async def log_command(self, command: str):
        log_path = AsyncPath(self.log_file_path)
        async with AIOFile(log_path, 'a') as afp:
            await afp.write(f"{datetime.datetime.now()}: {command}\n")
