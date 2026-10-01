import logging


"""
    Helper function to setup custom logger
    Parameters:
        - module_name: File name of module
        - log_level: Logging level (defaults to INFO)
    Returns:
        - logger: Handle to the logger
"""
def setup_custom_logger(module_name: str, log_level=logging.INFO):
    # Create a unique logger instance for this module
    logger = logging.getLogger(module_name)
    logger.setLevel(log_level)

    # Avoid duplicate log entries if re-initialized
    if logger.hasHandlers():
        logger.handlers.clear()

    # Formatter configuration
    log_format = logging.Formatter("%(asctime)s | %(name)s | [%(levelname)s] | %(message)s")

    # Handler 1: Terminal/Console Output
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_format)
    logger.addHandler(console_handler)

    # Handler 2: Write ERRORS only strictly to an active file log
    file_handler = logging.FileHandler("plant_guard_logs.log", encoding="utf-8")
    file_handler.setLevel(logging.ERROR)  # The file will only capture ERROR and higher
    file_handler.setFormatter(log_format)
    logger.addHandler(file_handler)

    return logger
