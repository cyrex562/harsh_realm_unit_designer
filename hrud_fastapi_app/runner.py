import sys

import uvicorn
from hrud_fastapi_app.fastapi_app import app

def run():
    uvicorn.run(app, host="0.0.0.0", port=8000)

if __name__ == "__main__":
    sys.exit(run())