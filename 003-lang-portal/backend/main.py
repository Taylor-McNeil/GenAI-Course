from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import word_route

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"])


app.include_router(word_route.router, prefix="/api",tags=["words"])  

@app.get("/")
def root():
    return {"message": "Hello World"}