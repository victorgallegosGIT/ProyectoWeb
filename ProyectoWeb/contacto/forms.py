from typing import Text
from django import forms

class FormularioContacto(forms.Form):
    nombre=forms.CharField(label="Nombre", required=True)
    email=forms.CharField(label="Email", required=True)

    contenido=forms.CharField(label="contenido", widget=forms.Textarea)

