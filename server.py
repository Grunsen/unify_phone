from fastapi import FastAPI, Body, Form, Cookie
from fastapi.responses import Response


app = FastAPI()


@app.post("/unify_phone_from_json")
def unify_phone_from_json(data: dict = Body(...)):
    num = data["phone"]
    clear_num = ""
    for char in num:
        if char.isdigit():
            clear_num += char
    if len(clear_num) < 10 or len(clear_num) > 11 or clear_num[-10] != '9':
        phone = clear_num
    else:
        phone = "8 (9{}{}) {}{}{}-{}{}-{}{}".format(*clear_num[-9:])
    return Response(phone, media_type="text/html")

@app.post("/unify_phone_from_form")
def unify_phone_from_json(value: str = Form(...)):
    num = value
    if len(num) < 10 or len(num) > 11 or num[-10] != '9':
        phone = num
    else:
        phone = "8 (9{}{}) {}{}{}-{}{}-{}{}".format(*num[-9:])
    return Response(phone, media_type="text/html")

@app.get("/unify_phone_from_query")
def unify_phone_from_json(phone: str):
    num = phone
    if len(num) < 10 or len(num) > 11 or num[-10] != '9':
        unified_phone = num
    else:
        unified_phone = "8 (9{}{}) {}{}{}-{}{}-{}{}".format(*num[-9:])
    return Response(unified_phone, media_type="text/html")
