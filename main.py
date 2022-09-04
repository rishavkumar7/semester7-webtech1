from fastapi import FastAPI 

app=FastAPI()

@app.get("/HomePage")
async def HomePage():
<<<<<<< HEAD
    return "Welcome All, This is my Assignment 1. Here I've build a basic website using fastAPI."
=======
    return "Welcome all, This is my Assignment 1. Here I've build a basic website using fastAPI."
>>>>>>> main
