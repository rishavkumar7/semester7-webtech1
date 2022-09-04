from fastapi import FastAPI 

app=FastAPI()

@app.get("/HomePage")
async def HomePage():
    return "Welcome All, This is my Assignment 1. Here I've build a basic website using fastAPI."