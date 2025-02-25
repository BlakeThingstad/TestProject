import azure.functions as func
import logging

app = func.FunctionApp()

@app.route(route="test_function", auth_level=func.AuthLevel.Anonymous)
def test_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    return func.HttpResponse("This HTTP triggered function executed successfully.")