class RedNosedReportService:
    def __init__(self, logger):
        self.logger = logger

    def count_safe_level(self, reports: []):
        self.logger.debug(f"Starts with param reports: {reports}")
        safe = 0
        for report in reports:
            self.logger.debug(f"Report is: {report}")
            policy = report.report_policy
            self.logger.debug(f"The policy is: {policy}")
            levels = report.levels
            if not self.unstable(levels):
                safe += 1

        return safe

    def unstable(self, levels):
        asc = desc = True
        for x, y in zip(levels, levels[1:]):
            self.logger.debug(f"x {x} and y {y}")
            diff = abs(int(x) - int(y))
            if x < y:
                desc = False
            elif x > y:
                asc = False
            if not asc and not desc:
                return True
            elif diff > 3 or diff < 1:
                return True

        return False
