from django import forms
from prueba8.models import *

class Buscar(forms.Form):
    #businessentity_buscar = forms.ModelChoiceField(queryset=Employee.objects.all().order_by('businessentityid'), to_field_name='businessentityid', label='businessentityid')
    #businessentity_buscar = forms.ModelChoiceField(queryset=Employeedepartmenthistory.objects.all().order_by('businessentityid'), to_field_name='businessentityid', label= "businessentityid", widget=forms.Select(attrs={'class':'form-select'}), required=False, empty_label="businessentityid")
    #jobtitle_buscar = forms.ModelChoiceField(queryset=Employee.objects.all().order_by('nationalidnumber'), to_field_name='jobtitle', label= "jobtitle", widget=forms.Select(attrs={'class':'form-select'}), required=False, empty_label="jobtitle")
    #gender_buscar = forms.ModelChoiceField(queryset=Employee.objects.all().order_by('nationalidnumber'), to_field_name='gender', label= "gender", widget=forms.Select(attrs={'class':'form-select'}), required=False, empty_label="gender")
  
    genero =(("1", "M"),("2", "F"))

    businessentityid_buscar = forms.ModelChoiceField(queryset=Person.objects.all().order_by('businessentityid'), to_field_name='businessentityid', label='businessentityid')
    jobtitle_buscar = forms.ModelChoiceField(queryset=Employee.objects.all().order_by('nationalidnumber'), to_field_name='jobtitle', label= "jobtitle", widget=forms.Select(attrs={'class':'form-select'}), required=False, empty_label="jobtitle")
    gender_buscar = forms.ChoiceField(choices = genero,required=False)