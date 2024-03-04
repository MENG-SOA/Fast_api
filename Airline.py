from pydantic import BaseModel
from fastapi import FastAPI, Request
from zeep import Client


app = FastAPI()


class Aircraft(BaseModel) :

    id: int
    model: str
    capacity: int
    range: int


aircrafts = []

# Create a Zeep client to consume the WSDL web service

client = Client('http://localhost:8088/ws/airlineservice?wsdl')

@app.get("/aircrafts")
def getAllAircrafts():
    # Call a method from the JAX-WS web service
    result = client.service.getAllAircraft()
    print(result)
    print(type(result))

    return result

    # Process the result
    # ...

    return {"message": "Response from JAX-WS web service: " + result}

