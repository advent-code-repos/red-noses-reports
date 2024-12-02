from services.red_nosed_report import RedNosedReportService
from services.file_service import FileService


class RedNosedReportController:
    def __init__(self, logger):
        self.logger = logger
        self.service = RedNosedReportService(logger)
        self.file_service = FileService(logger)
        self._reports = None

    def read(self, path):
        self.logger.info(f"Read input starts with {path} path")
        self.logger.debug(f"Params path: {path}")
        try:
            self._reports = self.file_service.read(path)
            self.logger.debug(f"Reports: {self._reports}")
        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise
        return self._reports

    def safe(self, reports):
        self.logger.info(f"Safe input starts with {reports} input")
        try:
            self.logger.debug(f"Reports: {self._reports}")
            safe = 0

        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise

        return safe
