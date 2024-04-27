import uvicorn as uvicorn

# dont delete
# noinspection PyUnresolvedReferences
from starlette.staticfiles import StaticFiles

# noinspection PyUnresolvedReferences
from routes.base import *

# noinspection PyUnresolvedReferences
from routes.user_route import *

from starlette.staticfiles import StaticFiles

# app.mount("/admin", StaticFiles(directory="static"), name="static")

if __name__ == '__main__':
    uvicorn.run(app='main:app', host='0.0.0.0', port=8086, reload=True)
    # uvicorn.run(app, host='0.0.0.0', port=8000, debug=True)
