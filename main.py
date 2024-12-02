from configs.logger import logger
from controllers.factories import create_red_nosed_report

INPUT_PATH = "inputs/input"


def main():
    logger.info("[AD24 - day 2] Red-Nosed Reports")

    red_nosed_report = create_red_nosed_report(logger)
    logger.debug(
        "RedNosed Report controller successfully created "
        f"{red_nosed_report}"
    )

    reports = red_nosed_report.read(INPUT_PATH)
    logger.debug(f"Reports are: {reports}")
    report_safe = red_nosed_report.safe(reports)
    logger.debug(f"Report safe is: {report_safe}")
    report_safe_dampener = red_nosed_report.dampener(reports)
    logger.debug(f"Report Dampener safe is: {report_safe_dampener}")

    logger.info(
        "========================= SOLUTIONs =========================="
    )
    logger.info(f"Report safe value: {report_safe}")
    logger.info(f"Report safe (Dampener): {report_safe_dampener}")
    logger.info(
        "=============================================================="
    )


if __name__ == "__main__":
    main()
