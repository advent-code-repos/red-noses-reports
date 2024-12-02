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
            safe = self.service.count_safe_level(reports)
            self.logger.debug(f"How many safe level?: {self.safe}")

        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise

        return safe

    def dampener(self, reports):
        self.logger.info(f"Dampener input starts with {reports} input")
        try:
            self.logger.debug(f"Reports: {self._reports}")
            safe = self.service.count_safe_dampener(reports)
            self.logger.debug(f"How many safe level?: {self.safe}")

        except Exception as e:
            self.logger.error(f"We have an Exception: {e}")
            raise

        return safe
