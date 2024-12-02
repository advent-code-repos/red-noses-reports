class RedNosedReportService:
    def __init__(self, logger):
        self.logger = logger

    def count_safe_level(self, reports: []):
        self.logger.debug(f"Starts with param reports: {reports}")
        safe = 0
        for report in reports:
            self.logger.debug(f"Report is: {report}")
            levels = report.levels
            if self.safe(levels):
                safe += 1

        return safe

    def safe(self, levels):
        differences = [
            int(levels[i + 1]) - int(levels[i]) for i in range(len(levels) - 1)
        ]
        self.logger.debug(f"Differences are: {differences}")

        if all(-3 <= diff <= -1 for diff in differences):
            self.logger.debug("safe")
            return True
        elif all(1 <= diff <= 3 for diff in differences):
            self.logger.debug("safe")
            return True

        self.logger.debug("unsafe")
        return False
