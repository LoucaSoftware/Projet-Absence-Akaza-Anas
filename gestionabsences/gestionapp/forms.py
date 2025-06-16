# gestionapp/forms.py
from django import forms

class ImportAbsencesForm(forms.Form):
    fichier_csv = forms.FileField(label="Fichier CSV d'absences")