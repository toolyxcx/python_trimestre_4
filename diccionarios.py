personas={
    "firstname":"gabriel",
    "lastname":"david",
    "age":23,
    "id":1000804100,
    "state":True
}
#muestra contenido integro
print(personas)

#muestra el valor de una key en particular
print(personas["firstname"])
#muestra el valor de una key en particular con metodo get
print(personas.get("lastname"))
#actualiza un valor 
personas["firstname"]="juliana"
print(personas["firstname"])
#agrega un nuevo elemento
personas['title']="ADSO"
print(personas)
#se ctualiza con un nuevo metodo
personas.update({"age":"18"})
print(personas)

#El método pop borra un elemento del diccionario basándose en la key indicada, permitiéndonos alterar el diccionario.
personas.pop("lastname")
print(personas)

#El método popitem borra el último elemento del diccionario
personas.popitem()
print(personas)

#del se utiliza para apuntar al elemento a borrar de un diccionario, mediante su key
del personas["id"]
print(personas)

i1 = {
"Nombre": "Jennifer",
"Apellido": "Fajardo",
"Title":"ADSO"
}
i2={
"Nombre": "Eduardo",
"Apellido": "Garcia",
"Title":"ADSO"
}
#Diccionario anidado
instructores={

"instructor1":i1,
"instructor2":i2
}
print(instructores)









