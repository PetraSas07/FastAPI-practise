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

def fizzbuzz_runner(size, f, b):
    fb_instance = Fizzbuzz(size)
    multiplied = f * b
    for i in range(size):
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

@app.get("/")
def fizzbuzz_base():
    return{"message": "Hello, from FizzBuzz!"}

@app.post("/fizzbuzz", response_model = FizzbuzzResult)
def fizzbuzz_custom(request: FizzbuzzRequest = Body(...)):
    return fizzbuzz_runner(request.size, request.f, request.b)


@app.get("/fizzbuzz_example")
def fizzbuzz_filled(size: int = 15, f: int = 2, b: int = 3):
    return fizzbuzz_runner(size, f, b)



