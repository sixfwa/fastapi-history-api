from fastapi import FastAPI, Response
import events_service as _service

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "hello world"}


@app.get("/events")
async def events():
    return _service.get_all_events()


@app.get("/events/{month}")
async def events_month(month: str):
    return _service.month_events(month)


@app.get("/events/{month}/{day}")
async def events_of_day(month: str, day: int):
    return _service.day_events(month, day)


@app.get("/events/today")
async def today():
    return _service.todays_events()