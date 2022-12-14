import csv
import datetime as dt
import logging

from prettytable import PrettyTable

from constants import BASE_DIR, DATETIME_FORMAT


def control_output(results, cli_args) -> None:
    output = cli_args.output
    if output == "pretty":
        pretty_output(results)
    elif output == "file":
        file_output(results, cli_args)
    else:
        default_output(results)


def default_output(results) -> None:
    for row in results:
        print(*row)


def pretty_output(results) -> None:
    table = PrettyTable()
    table.field_names = results[0]
    table.align = "l"
    table.add_rows(results[1:])
    print(table)


def file_output(result, cli_args) -> None:
    result_dir = BASE_DIR / "results"
    result_dir.mkdir(exist_ok=True)

    file_name = (
        f"{cli_args.mode}_{dt.datetime.now().strftime(DATETIME_FORMAT)}.csv"
    )
    file_path = result_dir / file_name

    with open(file_path, mode="w", encoding="utf-8") as csv_file:
        writer = csv.writer(csv_file, dialect="unix")
        writer.writerows(result)

    logging.info(f"Файл с результатами был сохранён: {file_path}")
