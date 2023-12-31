import uvicorn
from fastapi import FastAPI
from config.database import ENGINE, BASE
from middlewares.error_handler import ErrorHandler
from routes.user import user
from routes.movie import movie


BASE.metadata.create_all(bind=ENGINE)
app = FastAPI()
app.title = ""
app.version = ""
app.add_middleware(ErrorHandler)


# Add routes of API
app.include_router(user)
app.include_router(movie)


@app.get("/")
def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=1234, reload=True, workers=2)