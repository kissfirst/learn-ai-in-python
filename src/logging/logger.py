import logging
import os
from datetime import datetime

# 1.日志文件名
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# 2.日志目录路径
log_dir = os.path.join(os.getcwd(),"src","logs",LOG_FILE)

# 3.创建目录
os.makedirs(log_dir, exist_ok=True)

# 4.完整的日志文件路径
LOG_FILE_PATH = os.path.join(log_dir, LOG_FILE)

# 5 配置 logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(message)s",
    level=logging.INFO,
)