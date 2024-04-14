import uvicorn
from fastapi import FastAPI
from controllers.url_analysis_controller import url_analysis_router

app = FastAPI()

app.include_router(url_analysis_router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)