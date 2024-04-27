from fastapi import FastAPI

from core.exceptions import get_error_message_response

prefix = ''

from fastapi import applications
from fastapi.openapi.docs import get_swagger_ui_html


def swagger_monkey_patch(*args, **kwargs):
    """
    Wrap the function which is generating the HTML for the /docs endpoint and
    overwrite the default values for the swagger js and css.
    """
    return get_swagger_ui_html(
        *args, **kwargs,
        swagger_js_url="https://cdn.staticfile.org/swagger-ui/5.0.0/swagger-ui-bundle.min.js",
        swagger_css_url="https://cdn.staticfile.org/swagger-ui/5.0.0/swagger-ui.min.css")


# Actual monkey patch
applications.get_swagger_ui_html = swagger_monkey_patch

app = FastAPI(title="words.vip", docs_url=f"{prefix}/docs", redoc_url=f"{prefix}/redoc",
              openapi_url=f"{prefix}/openapi.json",
              swagger_ui_oauth2_redirect_url=f"{prefix}/docs/oauth2-redirect",
              description="service api & open Api")


@app.get("/")
def root():
    return {"status": "Hello,World!"}


@app.exception_handler(Exception)
def all_exception(request, execpt: Exception):
    print(f"all_exception_catch: {execpt}")
    return get_error_message_response(500, 500, str(execpt))
