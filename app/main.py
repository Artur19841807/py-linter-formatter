def format_linter_error(error: dict) -> dict:
    return {"line": error["line_number"], "text": f"{error['code']}{error['text']} ({error['column_number']})"}


def format_single_linter_file(file_path: str, errors: list) -> dict:
    return {file_path: [format_linter_error(error) for error in errors]}


def format_linter_report(linter_report: dict) -> list:
    return {file_path: [format_linter_error(error) for  error in errors] for file_path, errors in errors.items()}
