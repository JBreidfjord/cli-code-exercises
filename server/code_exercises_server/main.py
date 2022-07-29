import os.path

import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

app = FastAPI()


@app.get("/{course_code}/{exercise_id}")
async def get_exercise(course_code: int, exercise_id: int):
    filename = f"exercises/{course_code}/{exercise_id}.py"

    if not os.path.exists(filename):
        raise HTTPException(status_code=404, detail="Exercise not found")

    return FileResponse(filename)


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
