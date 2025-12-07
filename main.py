from fastapi import FastAPI, Path, HTTPException, Query
import json

app = FastAPI()

def load_data():
    with open('patients.json', 'r') as f:
        data = json.load(f)
    return data 


@app.get("/")
def hello():
    return {"message": "Hello, World!"} 


@app.get('/about')
def about():
    return {"message": "Fully functioning API to manage your patient records."}


@app.get('/view')
def view():
    return load_data()


@app.get('/patient/{patient_id}')
def view_patient(
    patient_id: str = Path(..., description="The patient ID", example="P001")
):
    data = load_data()

    if patient_id in data:
        return data[patient_id]

    raise HTTPException(status_code=404, detail="Patient not found")


# @app.get('/sort')
# def sort_patients(
#     sort_by: str = Query(..., description="Sort by height, weight, or bmi"),
#     order: str = Query("asc", description="Sort order: asc or desc")
# ):
#     valid_fields = ['height', 'weight', 'bmi']

#     if sort_by not in valid_fields:
#         raise HTTPException(
#             status_code=400,
#             detail=f"Invalid sort field. Choose from {valid_fields}"
#         )

#     if order not in ['asc', 'desc']:
#         raise HTTPException(
#             status_code=400,
#             detail="Invalid order. Choose asc or desc"
#         )

#     data = load_data()

#     reverse = True if order == 'desc' else False
#     sorted_data = sorted(
#         data.values(),
#         key=lambda x: x.get(sort_by, 0),
#         reverse=reverse
#     )

#     return sorted_data
@app.get('/sort')
def sort_patients(
    sort_by: str = Query(..., description="Sort on the basis of height, weight or bmi"),
    order: str = Query("asc", description="Sort in asc or desc order")
):
    valid_fields = ['height', 'weight', 'bmi']

    if sort_by not in valid_fields:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid sort field. Choose from {valid_fields}"
        )

    if order not in ['asc', 'desc']:
        raise HTTPException(
            status_code=400,
            detail="Invalid order. Choose asc or desc"
        )

    data = load_data()
    reverse = True if order == 'desc' else False

    sorted_data = sorted(
        data.values(),
        key=lambda x: x.get(sort_by, 0),
        reverse=reverse
    )

    return sorted_data

