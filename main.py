from configs.logger import logger
from controllers.factories import create_red_nosed_report

INPUT_PATH = "inputs/input.example"


def main():
    logger.info("[AD24 - day 2] Red-Nosed Reports")

    red_nosed_report = create_red_nosed_report(logger)
    logger.debug(
        "RedNosed Report controller successfully created "
        f"{red_nosed_report}"
    )

    report_safe = red_nosed_report.read(INPUT_PATH)
    report_safe_hard = 0

    logger.info(
        "========================= SOLUTIONs =========================="
    )
    logger.info(f"Report safe value: {report_safe}")
    logger.info(
        f"Report safe (hard): {report_safe_hard}"
    )
    logger.info(
        "=============================================================="
    )


if __name__ == "__main__":
    main()