# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def hello():
#     return {"message": "Hello, World!"} 


# from fastapi import FastAPI

# app = FastAPI()


from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def hello2():
    return {"message": "Hello, this is 2nd!"}