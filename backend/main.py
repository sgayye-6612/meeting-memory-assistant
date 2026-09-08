from fastapi import FastAPI, WebSocket

app = FastAPI(title="Meeting Memory Assistant")


@app.get("/")
def root():
    return {"message": "Meeting Memory Assistant API is running!"}


@app.websocket("/ws/meeting")
async def meeting_websocket(websocket: WebSocket):
    await websocket.accept()

    await websocket.send_json({
        "type": "status",
        "message": "Connected to the live meeting."
    })

    while True:
        message = await websocket.receive_text()

        await websocket.send_json({
            "type": "transcript",
            "text": message
        })
