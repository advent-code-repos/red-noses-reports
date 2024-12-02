from services.red_nosed_report import RedNosedReportService
from services.file_service import FileService

class RedNosedReportController:
  def __init__(self, logger):
    self.logger = logger
    self.service = RedNosedReportService(logger)
    self.file_service = FileService(logger)
  
  def read(self, path):
    self.logger.info(f"Read input starts with {path} path")
    self.logger.debug(f"Params path: {path}")
    try:
      reports = self.file_service.read(path)
      self.logger.debug(f"Reports: {reports}")
    except Exception as e:
      self.logger.error(f"We have an Exception: {e}")
      raise
      self.logger.info(f"Read input ends with {path} path")
    return reports