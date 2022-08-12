import shutil

import uvicorn
from fastapi import FastAPI, File
from fastapi.responses import FileResponse

from code_exercises_server.utils import (
    check_exercise_exists,
    create_temp_dir,
    parse_test_results,
    run_tests,
)

app = FastAPI()


@app.get("/{course_code}/{exercise_id}")
async def get_exercise(course_code: int, exercise_id: int):
    filename = f"../exercises/{course_code}/{exercise_id}.py"
    check_exercise_exists(filename)
    return FileResponse(filename)


@app.post("/develop/{course_code}/{exercise_id}")
async def develop_exercise(course_code: int, exercise_id: int, submission: bytes = File()):
    temp_dir = create_temp_dir(course_code, exercise_id, submission, type="develop")
    run_tests(temp_dir)
    results = parse_test_results(temp_dir)

    # Clean up temp directory
    shutil.rmtree(temp_dir)

    return results


@app.post("/submit/{course_code}/{exercise_id}")
async def submit_exercise(course_code: int, exercise_id: int, submission: bytes = File()):
    temp_dir = create_temp_dir(course_code, exercise_id, submission, type="submit")
    run_tests(temp_dir)
    results = parse_test_results(temp_dir)

    # Clean up temp directory
    shutil.rmtree(temp_dir)

    return results


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
