
from ninja import NinjaAPI, Schema, File
from ninja.files import UploadedFile
from typing import List, Optional
from datetime import datetime
from .models import Element
from typing import Union
import pandas as pd

api = NinjaAPI()

class ElementSchema(Schema):
    id: int
    date: Optional[str]
    name: Union[str, int]
    code: Optional[Union[str, int]] = None
    customer_name: Optional[Union[str, int]] = None
    bucket: Optional[Union[str, float]] = None
    galon: Optional[Union[str, float]] = None
    kilo: Optional[Union[str, float]] = None
    half_kilo: Optional[Union[str, float]] = None
    kes: Optional[Union[str, float]] = None
    notes: Optional[Union[str, float]] = None

    @staticmethod
    def from_orm(element: Element):
        return ElementSchema(
            id=element.id,
            date=str(element.date) if element.date else None,
            name=element.name,
            code=element.code,
            customer_name=element.customer_name,
            bucket=element.bucket,
            galon=element.galon,
            kilo=element.kilo,
            half_kilo=element.half_kilo,
            kes=element.kes,
            notes= element.notes
        )

@api.get("/elements", response=List[ElementSchema])
def get_elements(request):
    elements = Element.objects.all()
    filters = request.GET.dict()

    for field, value in filters.items():
        if hasattr(Element, field) and value:
            elements = elements.filter(**{f"{field}__icontains": value})

    return [ElementSchema.from_orm(element) for element in elements]

@api.post("/elements", response=ElementSchema)
def add_element(request, payload: ElementSchema):
    payload_dict = payload.dict()

    if 'date' in payload_dict and payload_dict['date']:
        try:
            payload_dict['date'] = datetime.strptime(payload_dict['date'], "%Y-%m-%d").date()
        except ValueError:
            payload_dict['date'] = None

    for field in ['bucket', 'galon', 'kilo', 'half_kilo', 'kes']:
        if field in payload_dict and payload_dict[field] is not None:
            payload_dict[field] = str(payload_dict[field])

    element = Element.objects.create(**payload_dict)
    return ElementSchema.from_orm(element)

@api.put("/elements/{element_id}", response=ElementSchema)
def edit_element(request, element_id: int, payload: ElementSchema):
    try:
        element = Element.objects.get(id=element_id)
    except Element.DoesNotExist:
        return api.create_response(request, {"error": "Element not found."}, status=404)

    payload_dict = payload.dict()

    if 'date' in payload_dict and payload_dict['date']:
        try:
            payload_dict['date'] = datetime.strptime(payload_dict['date'], "%Y-%m-%d").date()
        except ValueError:
            payload_dict['date'] = None

    for field in ['bucket', 'galon', 'kilo', 'half_kilo', 'kes']:
        if field in payload_dict and payload_dict[field] is not None:
            payload_dict[field] = str(payload_dict[field])

    for attr, value in payload_dict.items():
        setattr(element, attr, value)

    element.save()
    return ElementSchema.from_orm(element)

@api.delete("/elements/{element_id}")
def delete_element(request, element_id: int):
    try:
        element = Element.objects.get(id=element_id)
        element.delete()
        return {"success": True}
    except Element.DoesNotExist:
        return api.create_response(request, {"error": "Element not found."}, status=404)

@api.post("/elements/upload-excel/")
def upload_excel(request, file: UploadedFile = File(...)):
    try:
        df = pd.read_excel(file.file)

        df.rename(columns={
            "ID": "id",
            "Date": "date",
            "Name": "name",
            "Code": "code",
            "Customer Name": "customer_name",
            "Bucket": "bucket",
            "Galon": "galon",
            "Kilo": "kilo",
            "Half Kilo": "half_kilo",
            "Kes": "kes",
        }, inplace=True)

        valid_columns = ["id", "date", "name", "code", "customer_name", "bucket", "galon", "kilo", "half_kilo", "kes"]
        df = df[valid_columns]
        df = df.where(pd.notnull(df), None)

        errors = []
        success_count = 0

        for index, row in df.iterrows():
            record = row.to_dict()

            if record.get("date"):
                if not record["date"]:
                     record["date"] = None
                elif isinstance(record["date"], datetime):
                    record["date"] = record["date"].date().isoformat()
                else:
                    try:
                        record["date"] = datetime.strptime(str(record["date"]), "%Y-%m-%d").date()
                    except ValueError:
                        try:
                            record["date"] = datetime.strptime(str(record["date"]), "%d/%m/%Y").date()
                        except ValueError:
                            record["date"] = None

            for field in ['bucket', 'galon', 'kilo', 'half_kilo', 'kes']:
                if field in record and record[field] is not None:
                    record[field] = str(record[field])

            try:
                payload = ElementSchema(**record)
                payload_dict = payload.dict()

                if payload_dict.get("date"):
                    payload_dict["date"] = datetime.strptime(payload_dict["date"], "%Y-%m-%d").date()
                Element.objects.create(**payload_dict)
                success_count += 1
            except Exception as e:
                errors.append({"row": index + 1, "error": str(e)})

        return {
            "success": True,
            "message": f"Uploaded {success_count} elements successfully.",
            "errors": errors
        }
    except Exception as e:
        return api.create_response(request, {"error": str(e)}, status=400)

@api.delete("/elements/delete-all/")
def delete_all_elements(request):
    try:
        Element.objects.all().delete()
        return {"success": True, "message": "All elements have been deleted successfully."}
    except Exception as e:
        return api.create_response(request, {"error": str(e)}, status=500)
