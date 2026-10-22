from pydantic import BaseModel

class student(BaseModel):
    name:str

new_student={"name":"Vishnu"}

result=student(**new_student) #unpacking dict
print(result)