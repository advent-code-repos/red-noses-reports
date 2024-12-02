from models.report import Report


class FileService:
    def __init__(self, logger):
        self.logger = logger

    def read(self, path: str):
        self.logger.info(f"Read input at {path} path")
        try:
            with open(path, "r") as file:
                return [Report(line.split()) for line in file]
        except (FileNotFoundError, ValueError) as e:
            self.logger.error(f"We have an Exception: {e}")
            raise RuntimeError(f"Errore during reading file: {e}")
