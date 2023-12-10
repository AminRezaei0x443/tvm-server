import uvicorn
from tvm_server.srv import app
from dotenv import load_dotenv
import os


def main():
    load_dotenv()
    tg_port = os.environ.get("PORT", "8118")
    uvicorn.run(app, host="0.0.0.0", port=int(tg_port), log_level="info")


if __name__ == "__main__":
    main()
