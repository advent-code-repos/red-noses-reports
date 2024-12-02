from models.report import Report
from models.policy import Policy


class FileService:
    def __init__(self, logger):
        self.logger = logger

    def read(self, path: str):
        self.logger.info(f"Read input at {path} path")
        try:
            with open(path, "r") as file:
                for line in file:
                    return [
                        Report(line.split(), self._setup_policy(line.split()))
                        for line in file
                    ]
        except (FileNotFoundError, ValueError) as e:
            self.logger.error(f"We have an Exception: {e}")
            raise RuntimeError(f"Errore during reading file: {e}")

    def _setup_policy(self, levels):
        return Policy.DECREASE if levels[0] > levels[1] else Policy.INCREASE
