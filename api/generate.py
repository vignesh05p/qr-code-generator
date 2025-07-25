from fastapi import FastAPI, Form
from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO

app = FastAPI()

@app.post("/api/generate")
async def generate_qr(
    url: str = Form(...),
    fg_color: str = Form("black"),
    bg_color: str = Form("white")
):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(fill_color=fg_color, back_color=bg_color)
    buf = BytesIO()
    img.save(buf, format="PNG")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")
