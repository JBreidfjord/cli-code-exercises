import os

import requests
import typer
from rich import print

from cli_code_exercises.utils import api_url, check_status, open_file

app = typer.Typer()


@app.command()
def get(course_code: int, exercise_id: int):
    print("Fetching exercise from server...")

    response = requests.get(api_url(f"/{course_code}/{exercise_id}"), stream=True)
    check_status(response)

    os.makedirs(f"../exercises/{course_code}", exist_ok=True)
    with open(f"../exercises/{course_code}/{exercise_id}.py", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

    print(f"Success! File saved to 'exercises/{course_code}/{exercise_id}.py'")


@app.command()
def develop(course_code: int, exercise_id: int, path: str = ""):
    if not path:
        path = f"../exercises/{course_code}/{exercise_id}.py"

    submission = open_file(path)

    response = requests.post(
        api_url(f"/develop/{course_code}/{exercise_id}"),
        {"submission": submission},
    )
    check_status(response)
    print(response.text)


@app.command()
def submit(course_code: int, exercise_id: int, path: str = ""):
    if not path:
        path = f"../exercises/{course_code}/{exercise_id}.py"

    submission = open_file(path)

    response = requests.post(
        api_url(f"/submit/{course_code}/{exercise_id}"),
        {"submission": submission},
    )
    check_status(response)
    print(response.text)


if __name__ == "__main__":
    app()
