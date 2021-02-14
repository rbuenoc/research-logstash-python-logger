from common.tools.logs import initialize_logging, log_info, log_exception
from services.process import process_data

initialize_logging()

try:
    process_data()
except Exception as ex:
    log_exception(__name__, ex)
