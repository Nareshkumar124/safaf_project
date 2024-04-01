from fastapi import FastAPI, Form,HTTPException
from pydantic import EmailStr
from typing import Annotated
from datetime import datetime
from sheet import sendData


app = FastAPI(docs_url="/")


@app.post("/submit-form")
async def submit_form_data(
    title: Annotated[str, Form()],
    surname: Annotated[str, Form()],
    name: Annotated[str, Form()],
    designation: Annotated[str, Form()],
    department: Annotated[str, Form()],
    organization: Annotated[str, Form()],
    address: Annotated[str, Form()],
    city: Annotated[str, Form()],
    postalCode: Annotated[str, Form()],
    country: Annotated[str, Form()],
    age: Annotated[int, Form()],
    accommodation: Annotated[bool, Form()],
    mobile: Annotated[str, Form()],
    email: Annotated[EmailStr, Form()],
    date: Annotated[datetime, Form()],
):
    
    try:
        data = [
                title,
                surname,
                name,
                designation,
                department,
                organization,
                address,
                city,
                postalCode,
                country,
                age,
                accommodation,
                mobile,
                email,
                date.strftime("%Y-%m-%d %H:%M:%S"),
            ]

        return sendData(data)
    
    except Exception as e:
        raise HTTPException(status_code=500,detail="Internal Server Error.")
    
    

    
    

def fun2():...
