class RedNosedReportService:
    def __init__(self, logger):
        self.logger = logger
        self.safed = []
        self.valutation = []

    def count_safe_level(self, reports: []):
        self.logger.debug(f"Starts with param reports: {reports}")
        safe = 0
        for report in reports:
            self.logger.debug(f"Report is: {report}")
            levels = report.levels
            if self.safe(levels):
                safe += 1

        return safe

    def count_safe_dampener(self, reports: []):
        self.logger.debug(f"Starts with param reports: {reports}")
        safe = 0
        for report in reports:
            self.logger.debug(f"Report is: {report}")
            levels = report.levels
            self.logger.debug(f"VALUTATION: {levels}")
            self.valutation.append(levels)
            if self.safe(levels):
                self.logger.debug("safe: ok!")
                self.safed.append(levels)
                safe += 1
            elif self.can_be_safe(levels):
                self.logger.debug("can be safe: ok!")
                safe += 1

        self.logger.debug(f"SAFED: {self.safed}")
        self.logger.debug(f"VALUTATIONS: {self.valutation}")
        return safe

    def safe(self, levels):
        differences = [
            int(levels[i + 1]) - int(levels[i]) for i in range(len(levels) - 1)
        ]
        self.logger.debug(
            f"Levels are: {levels} and differences are: {differences}"
        )

        if all(-3 <= diff <= -1 for diff in differences):
            self.logger.debug(f"Report with {levels} is safe")
            return True
        elif all(1 <= diff <= 3 for diff in differences):
            self.logger.debug(f"Report with {levels} is safe")
            return True

        self.logger.debug(f"Report with {levels} is unsafe")
        return False

    def can_be_safe(self, levels):
        for i in range(len(levels)):
            modified_levels = levels[:i] + levels[i + 1 :]
            if self.safe(modified_levels):
                self.safed.append(modified_levels)
                return True
