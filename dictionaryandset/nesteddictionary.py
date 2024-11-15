student = {
  "name" : "rahul kumar",
   "subjects" :{
      "phy" :97,
       "chem" : 98,
       "math" :86
   }
}
print(student["subjects"]["chem"])
print(student.keys())
student.update({"City" : "delhi"})
new_dict = {"nationality":"hidu"}
student.update(new_dict)
print(student)
