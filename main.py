from fastapi import FastAPI
from app.api import (
    routes_auth, routes_user, routes_appointment,
    routes_document, routes_review, routes_medicine
)
from app.database import Base, engine
from app.api import routes_document
app = FastAPI(
    title="Patient-Doctor Management System",
    description="Manage patients, doctors, appointments, and more.",
    version="1.0",
    docs_url="/docs"  # Default URL for Swagger docs, can be changed here
)

Base.metadata.create_all(bind=engine)

app.include_router(routes_auth.router)
app.include_router(routes_user.router)
app.include_router(routes_appointment.router)
app.include_router(routes_document.router)
app.include_router(routes_review.router)
app.include_router(routes_medicine.router)
app.include_router(routes_document.router)