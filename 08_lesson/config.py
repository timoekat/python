import os

BASE_URL = "https://ru.yougile.com/api-v2/"

API_KEY = os.getenv("YOUGILE_API_KEY")

HEADERS = {
    "Authorization": f"Bearer {API_KEY}"
}


PROJECT_ID = "09c0a97d-9bd3-4227-ab80-d4ba82f3c4bf"


PROJECT_TITLE = "EkaterinaT"
UPDATED_PROJECT_TITLE = "UpdatedProjectTitle"
