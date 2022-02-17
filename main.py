from fastapi import FastAPI

app = FastAPI()

@app.get("/user/{name}")
async def getUser(name):
    return {"message": "Hello, " + name}
