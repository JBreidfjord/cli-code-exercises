import os

import requests
import typer
from rich import print

app = typer.Typer()


def api_url(route: str):
    return "http://localhost:8000" + route


@app.command()
def get(course_code: int, exercise_id: int):
    print("Fetching exercise from server...")

    response = requests.get(api_url(f"/{course_code}/{exercise_id}"), stream=True)
    if response.status_code != 200:
        print("Error received from server:", response.text)
        raise typer.Abort()

    os.makedirs(f"../exercises/{course_code}", exist_ok=True)
    with open(f"../exercises/{course_code}/{exercise_id}.py", "wb") as file:
        for chunk in response.iter_content(chunk_size=1024):
            file.write(chunk)

    print(f"Success! File saved to 'exercises/{course_code}/{exercise_id}.py'")


if __name__ == "__main__":
    app()
