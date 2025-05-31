from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.database import async_session
from app.models import User
from app.schemas import UserCreate, UserLogin, Token
from app.auth import create_access_token

router = APIRouter()

async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session


@router.post("/register")
async def register(user: UserCreate, session: AsyncSession = Depends(get_session)):
    existing = await session.execute(select(User).where(User.username == user.username))

    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Username already exists")
    
    new_user = User(username=user.username, password=user.password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return {"id": new_user.id, "username": new_user.username}


@router.post("/login", response_model=Token)
async def login(user: UserLogin, session: AsyncSession = Depends(get_session)):
    query = await session.execute(select(User).where(User.username == user.username))
    db_user = query.scalar_one_or_none()

    if not db_user or db_user.password != user.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    token = create_access_token(data={"sub": db_user.username})
    return {"access_token": token, "token_type": "bearer"}