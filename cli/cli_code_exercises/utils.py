import os.path

import typer
from requests import Response


def api_url(route: str) -> str:
    return "http://localhost:8000" + route


def check_status(response: Response) -> None:
    if response.status_code != 200:
        print("Error received from server:", response.text)
        raise typer.Abort()


def check_file_exists(filepath: str) -> None:
    if not os.path.exists(filepath):
        print("File not found:", filepath)
        raise typer.Abort()


def open_file(filepath: str) -> bytes:
    check_file_exists(filepath)
    with open(filepath, "rb") as file:
        file_bytes = file.read()
    return file_bytes
