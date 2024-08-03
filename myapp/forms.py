from django import forms

class CSVUploadForm(forms.Form):
    csv_file = forms.FileField(label='Select a CSV file')

class DataFilterForm(forms.Form):
    column = forms.ChoiceField(choices=[], required=False)
    value = forms.CharField(max_length=100, required=False)
    
    def __init__(self, *args, **kwargs):
        columns = kwargs.pop('columns', [])
        super().__init__(*args, **kwargs)
        self.fields['column'].choices = [(col, col) for col in columns]