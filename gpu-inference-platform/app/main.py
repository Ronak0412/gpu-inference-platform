from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/generate")
def generate(prompt: str):
    # placeholder — real vLLM call comes in week 3
    return {"prompt": prompt, "completion": "stub response"}