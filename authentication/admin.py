from django.contrib import admin
from.models import Country,Department,City, User
# Register your models here.
#aqui van tablas en donde se vana ingresar datos.
#vamos a importar los modelos 
#model viene del archivo model.py 


#ahora vamos a registrar el que queremos que salga con interfax grafica.
admin.site.register(Country)
admin.site.register(Department)
admin.site.register(City)
admin.site.register(User)   

