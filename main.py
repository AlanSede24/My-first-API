# Imports
from fastapi import FastAPI

from pydantic import BaseModel

from router import router as rt

# Creación de una instancia de FastAPI
app = FastAPI()
app.title = "My application with FastAPI"
app.version = "0.2.1"
# Inclusión file router en app principal
app.include_router(rt, tags=["endpoints"])

'''
INICIA PRACTICA - CURSO PLATZI
'''

# Creación de un modelo representativo
class Item(BaseModel):
    name: str
    description: str = None
    price: float = None

# Creación de endpoints (método GET)
@app.get('/', tags = ['home'])  # endpoint 1
def message():
    return f"Hello world! It is my first App."

@app.get('/items/{item_id}', tags = ['home'])  # endpoint 2
def read_item(item_id: int, q: str = None):
    return {"item_id": item_id, "q": q}

# Creación de endpoints (método POST0)
@app.post('/items/')
async def create_item(item: Item):
    return item

'''
FIN PRACTICA - CURSO PLATZI
'''

'''
CREACION DE ENPOINTS ESPECIFICOS


# Endpoint GET para consultar Asset Server WebId a la WebAPI 
@app.get("/get_asset_server/")
async def get_data_servers():
    username = "lwirth"
    password = "Justthewayyouare10"

    # Encode in base64
    base64_credentials = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
    
    endpoint_url = "https://www.adetech-industrial.com:8443/piwebapi/assetservers"

    headers = {
        "Authorization": f"Basic {base64_credentials}",
        "Content-Type": "application/json"
    }
    
    try:
        # Make the request
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(endpoint_url, headers=headers)
        
        print(response.text)  # Log the response content
        # Handle the response
        if response.status_code == 200:
            response_data = response.json()
            items = response_data.get('Items', [])
            filtered_items = [{'Name': item.get('Name'), 'WebId': item.get('WebId')} for item in items]
            return filtered_items
        else:
            return JSONResponse(content=response.json(), status_code=response.status_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Endpoint POST para consultar Database WebID a partir de Asset Server WebId
class AssetDatabaseSearch(BaseModel):
    asset_server_webid: str
    # string_search: Optional[str] = "*"
    
@app.post("/get_database_from_asset_server/")
async def search(asset_database_search: AssetDatabaseSearch):
    username = "lwirth"
    password = "Justthewayyouare10"
    
    base64_credentials = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
    endpoint_url = f"https://www.adetech-industrial.com:8443/piwebapi/assetservers/{asset_database_search.asset_server_webid}/assetdatabases"
    
# https://www.adetech-industrial.com:8443/piwebapi/assetservers/F1RSfzoLpZW9rU-M1GRbEStegQSUctVlNSVi0wNA/assetdatabases

    headers = {
        "Authorization": f"Basic {base64_credentials}",
        "Content-Type": "application/json"
    }
    
    try:
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(endpoint_url, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            items = response_data.get('Items', [])
            filtered_items = [{'Name': item.get('Name'), 'WebId': item.get('WebId')} for item in items]
            return filtered_items
        else:
            return JSONResponse(content=response.json(), status_code=response.status_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

# Endpoint POST para consultar Element WebId a partir de Database WebId y Template Name
class ElementSearch(BaseModel):
    element_name: Optional[str] = "*"
    template_name: Optional[str] = "*"
    database_webid: str

@app.post("/get_elements_by_search/")
async def search(elements_search: ElementSearch):
    username = "lwirth"
    password = "Justthewayyouare10"
    
    base64_credentials = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
    piserver_url = "https://www.adetech-industrial.com:8443/piwebapi"
    endpoint_url = f"{piserver_url}/elements/search?query=name:{elements_search.element_name}%20templatename:={elements_search.template_name}&databaseWebId={elements_search.database_webid}"
    
# https://www.adetech-industrial.com:8443/piwebapi/elements/search?query=name:*339&databaseWebId= ...
# F1RDfzoLpZW9rF1RDfzoLpZW9rU-M1GRbEStegQD8Mw8pfIy0iCWnbAJw12twSUctVlNSVi0wNFxQQUUU-M1GRbEStegQD8Mw8pfIy0iCWnbAJw12twSUctVlNSVi0wNFxQQUU

    headers = {
        "Authorization": f"Basic {base64_credentials}",
        "Content-Type": "application/json"
    }
    
    try:
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(endpoint_url, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            items = response_data.get('Items', [])
            filtered_items = [{'Name': item.get('Name'), 'WebId': item.get('WebId'),'TemplateName': item.get('TemplateName')} for item in items]
            return filtered_items
        else:
            return JSONResponse(content=response.json(), status_code=response.status_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
    
# Endpoint POST para consultar Attributes a partir de un Element WebId
class AttributeSearch(BaseModel):
    element_webid: str
    # string_to_search: str

@app.post("/get_attributes_by_element_webid/")
async def search(attributes_search: AttributeSearch):
    username = "lwirth"
    password = "Justthewayyouare10"
    
    base64_credentials = base64.b64encode(f"{username}:{password}".encode("utf-8")).decode("utf-8")
    endpoint_url = f"https://www.adetech-industrial.com:8443/piwebapi/elements/{attributes_search.element_webid}/attributes"
    
# https://www.adetech-industrial.com:8443/piwebapi/elements/F1EmfzoLpZW9rU-M1GRbEStegQIxnluRvt7RGu9wAVXQU2LASUctVlNSVi0wNFxQQUVcRExTLTE2NQ/attributes

    headers = {
        "Authorization": f"Basic {base64_credentials}",
        "Content-Type": "application/json"
    }
    
    try:
        async with httpx.AsyncClient(verify=False) as client:
            response = await client.get(endpoint_url, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            items = response_data.get('Items', [])
            filtered_items = [{'Name': item.get('Name'), 'WebId': item.get('WebId')} for item in items]
            return filtered_items
        else:
            return JSONResponse(content=response.json(), status_code=response.status_code)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

'''