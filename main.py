from fastapi import FastAPI

app = FastAPI(debug=True)

@app.get("/api/v1/users", name="user", tags=["Userssss"])
def get_users ():
  return {"name":"Myname", "age": "My Age"}

@app.post("/api/v1/users", name="register", tags=["Auth"])
def create_user ():
  return {"name":"Myname", "age": "My Age"}
