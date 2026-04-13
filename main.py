from fastapi import FastAPI, Body
from fizzbuzz import Fizzbuzz
from pydantic import BaseModel, Field

app = FastAPI()

class FizzbuzzRequest(BaseModel):
    size: int = Field(gt = 0, le = 200, description = "Defines the length of the automated list of values")
    f: int = Field(gt = 1, le = 200, description = "Sets the fizz divisor number")
    b: int = Field(gt = 1, le = 200, description = "Sets the buzz divisor number")

class FizzbuzzResult(BaseModel):
    string_list: list
    size: int
    index: int

@app.get("/")
def read_root():
    return{"message": "Hello, Foo!"}

@app.post("/fizzbuzz", response_model = FizzbuzzResult)
def fizzbuzz_runner(request: FizzbuzzRequest = Body(...)):
    fb_instance = Fizzbuzz(request.size)
    f, b = request.f, request.b
    multiplied = f * b
    for i in range(request.size):
        if (fb_instance.index + 1) % multiplied == 0:
            fb_instance.fizzbuzz()
        elif (fb_instance.index + 1) % f == 0:
            fb_instance.fizz()
        elif (fb_instance.index + 1) % b == 0:
            fb_instance.buzz()
        else:
            fb_instance.number()
        fb_instance.index += 1
    return fb_instance



