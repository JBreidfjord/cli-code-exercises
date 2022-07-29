import os
import secrets
import shutil

from fastapi import HTTPException


def check_exercise_exists(exercise_filepath: str) -> None:
    # TODO: Replace file check with check to master list of exercises
    if not os.path.exists(exercise_filepath):
        raise HTTPException(status_code=404, detail="Exercise not found")


def create_temp_dir(course_code: int, exercise_id: int, submission_file: bytes, type: str) -> str:
    test_filename = f"../exercise_tests/{course_code}/{exercise_id}_{type}_test.py"
    check_exercise_exists(test_filename)

    temp_dir = "../tmp/"
    test_dir = secrets.token_hex(16)
    os.makedirs(temp_dir + test_dir)
    with open(f"{temp_dir}{test_dir}/submission.py", "wb") as file:
        file.write(submission_file)
    shutil.copyfile(test_filename, f"{temp_dir}{test_dir}/test.py")

    return temp_dir + test_dir
