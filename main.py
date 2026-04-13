from fastapi import FastAPI
from pydantic import BaseModel
from fizzbuzz import Fizzbuzz

app = FastAPI()

class Greeting(BaseModel):
    name: str
    surname: str
    age: int

@app.get("/")
def read_root():
    return{"message": "Hello, Foo!"}

# @app.post("/greet/")
# def create_greeting(greet: Greeting):
#     return greet

@app.post("/fizzbuzz")
def fizzbuzz_runner(size: int, f, b):
    fb_instance = Fizzbuzz(size)
    f, b = int(f), int(b)
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
    return fb_instance.string_list
            


def main():
    read_root()



if __name__ == "__main__":
    main()
