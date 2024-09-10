from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import text_generation, sentiment_analysis, ner, performance_dashboard, feedback

app = FastAPI(
    title="LLM Insight Hub API",
    description="API for text generation, sentiment analysis, and named entity recognition using various LLM models",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Allow Angular dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(text_generation.router, prefix="/api", tags=["Text Generation"])
app.include_router(sentiment_analysis.router, prefix="/api", tags=["Sentiment Analysis"])
app.include_router(ner.router, prefix="/api", tags=["Named Entity Recognition"])
app.include_router(performance_dashboard.router, prefix="/api", tags=["Performance Dashboard"])
app.include_router(feedback.router, prefix="/api", tags=["User Feedback"])

@app.get("/")
async def root():
    return {"message": "Welcome to the LLM Insight Hub API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)