from fastapi import FastAPI
from app.utils.config import settings
from fastapi.middleware.cors import CORSMiddleware
from app.routes import file_router

# Initialize FastAPI app
app = FastAPI(title=settings.APP_NAME, version=settings.APP_VERSION)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (use specific origins in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

api_version_prefix = f"/api/{settings.API_VERSION}"

# Include routers with the common API version prefix
routers = [
    file_router.router
]

# Dynamically include all routers
for router in routers:
    app.include_router(router, prefix=api_version_prefix)