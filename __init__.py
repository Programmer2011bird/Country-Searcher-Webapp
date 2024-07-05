from typing import Any
import API
from flask import *

SERVER: Flask = Flask(__name__)


@SERVER.route("/")
def Home() -> str:
    return render_template("Search.html")


@SERVER.route("/Search_Name", methods=["GET", "POST"])
def Search_Name() -> str:
    NAME: str = str(request.form.get("country_name"))
    ENDPOINT: str = f"name/{NAME}"

    return API.Get_Json(ENDPOINT)


@SERVER.route("/Search_Code", methods=["GET", "POST"])
def Search_Code() -> Any:
    CODE: str = str(request.form.get("country_code"))
    ENDPOINT: str = f"alpha/{CODE}"
    
    return API.Get_Json(ENDPOINT)


@SERVER.route("/Search_Currency", methods=["GET", "POST"])
def Search_Currency() -> Any:
    CURRENCY: str = str(request.form.get("country_currency"))
    ENDPOINT: str = f"currency/{CURRENCY}"
    
    return API.Get_Json(ENDPOINT)


@SERVER.route("/Search_Language", methods=["GET", "POST"])
def Search_Language() -> Any:
    LANGUAGE: str = str(request.form.get("country_language"))
    ENDPOINT: str = f"lang/{LANGUAGE}"
    
    return API.Get_Json(ENDPOINT)


@SERVER.route("/Search_Capital", methods=["GET", "POST"])
def Search_Capital() -> Any:
    CAPITAL: str = str(request.form.get("country_capital"))
    ENDPOINT: str = f"capital/{CAPITAL}"
    
    return API.Get_Json(ENDPOINT)



if __name__ == "__main__":
    SERVER.run(debug= True)
