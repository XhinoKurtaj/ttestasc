from typing import List
from fastapi import APIRouter, HTTPException, status
# from project import db
from api import deps
from databases import Database
from schemas.time_log import CreateTimeLog

router = APIRouter()

@app.post('/log', response_model=PostDB, status_code=status.HTTP_201_CREATED)
async def create_post(time_log: CreateTimeLog, database: Database = Depends(deps.get_db)) -> PostDB:
    insert_query    = time_log.insert().value(time_log.dict())
    time_id         = await database.execute(insert_query)
    time_db         = await get_log_or_404(post_id, database)
    return time_db


@app.get('/log')
async def list_posts(
    pagination  :   Tuple[int, int]     = Depends(pagination),
    database    :   Database            = Depends(get_database),
) -> List[PostDB]:
    skip, limit     = pagination
    select_query    = post.select().offset(skip).limit(limit)
    rows            = await database.fetch_all(select_query)
    results         = [PostDB(**row) for row in rows]
    return results 


@app.patch('/posts/{id}', response_model=PostDB)
async def update_post(
    post_update     :       PostPartialUpdate,
    post            :       PostDB      = Depends(get_post_or_404),
    database        :       Database    = Depends(get_database),
)   ->  PostDB:
    update_query = (
        post.update()
        .where(posts.c.id == post.id)
        .values(post_update.dict(exclude_unset=True))
    )
    post_id = await database.execute(update_query)
    post_db = await get_post_or_404(post_id, database)
    return 

@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    post        : PostDB    = Depends(get_post_or_404),
    database    : Database  = Depends(get_database),
):
    delete_query = posts.delete().where(posts.c.id == post.id)
    await database.execute(delete_query)
   

async def pagination(
    skip    : int = Query(0, ge=0),
    limit   : int = Query(10, ge=0),
) -> Tuple[int, int]:
    capped_limit = min(100, limit)
    return (skip, capped_limit)


async def get_log_or_404(
    id: int, database: Database = Depends(get_database)
) -> CreateTimeLog:
    select_query    =   time_log.select().where(posts.c.id == id)
    raw_log        =   await database.fetch_one(select_query)
    if raw_log is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return CreateTimeLog(**raw_post)