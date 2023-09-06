from typing import Any
from django import http
from django.http.response import JsonResponse
from django.views import View
from .models import Personas
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django import forms
import json
# Create your views here.

class PersonasView(View):
    

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    #Filtro de Busqueda por ID y tambien de muestreo general.

    def get(self, request, id=0):
        if (id > 0):
            personas = list(Personas.objects.filter(id=id).values())
            if len(personas) > 0:
                persona = personas [0]
                datos = {'message':'Success', 'persona': persona}
            else:
                datos = {'message':'Personas no encontradas...'}
                return JsonResponse(datos)
        else:
            personas= list(Personas.objects.values())
            if len(personas)>0:
                datos={'message':'Success', 'personas':personas}
            else:
                datos={'message':'Personas no encontradas...'}
            return JsonResponse(datos)
        return JsonResponse(datos)

#Filtro de busqueda por Si vive o No en GBA 

    def vive_en_gba(self, request, GBA=True):
         if (GBA == True):
            personas= list(Personas.objects.filter(GBA=True).values())
            datos ={'message':'Success', 'personas':personas}
         else:
            personas= list(Personas.objects.filter(GBA=False).values())
            datos ={'message':'Success', 'personas':personas }
            return JsonResponse(datos)

    def post(self,request):
        # print(request.body)
        jd=json.loads(request.body)
        # print(jd)
        Personas.objects.create(nombre=jd['nombre'],apellido=jd['apellido'],DNI=jd['DNI'],fecha_nacimiento=jd['fecha_nacimiento'], GBA=jd['GBA'])
        datos={'message':'Success'}
        return JsonResponse(datos)

    def put(self,request, id): 
        jd=json.loads(request.body)
        personas = list(Personas.objects.filter(id=id).values())
        if len(personas) > 0:
            persona = Personas.objects.get(id=id)
            persona.nombre = jd['nombre']
            persona.apellido = jd['apellido']
            persona.DNI = jd['DNI']
            persona.fecha_nacimiento = jd['fecha_nacimiento']
            persona.GBA = jd['GBA']
            persona.save()
            datos={'message':'Success'}
        else: 
            datos={'message':'Personas no encontradas...'}
        return JsonResponse(datos) 


    def delete(self,request, id): 
        personas = list(Personas.objects.filter(id=id).values())
        if len(personas) > 0:
            Personas.objects.filter(id=id).delete()
            datos={'message':'Success'}
        else:
            datos={'message':'Personas no encontradas...'}
        return JsonResponse(datos)