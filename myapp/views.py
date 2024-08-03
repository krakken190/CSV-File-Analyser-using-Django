from django.shortcuts import render
from .forms import CSVUploadForm, DataFilterForm
import pandas as pd
import numpy as np
import os
from django.conf import settings
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

def home(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            file_path = os.path.join(settings.MEDIA_ROOT, csv_file.name)
            
            with open(file_path, 'wb+') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)
            
            df = pd.read_csv(file_path)
            
            filter_form = DataFilterForm(columns=df.columns)
            
            context = analyze_data(df)
            context['form'] = form
            context['filter_form'] = filter_form
            context['file_path'] = file_path
            
            return render(request, 'myapp/results.html', context)
    else:
        form = CSVUploadForm()
    return render(request, 'myapp/home.html', {'form': form})

def filter_data(request):
    if request.method == 'POST':
        file_path = request.POST.get('file_path')
        df = pd.read_csv(file_path)
        
        filter_form = DataFilterForm(request.POST, columns=df.columns)
        if filter_form.is_valid():
            column = filter_form.cleaned_data['column']
            value = filter_form.cleaned_data['value']
            
            if column and value:
                df = df[df[column].astype(str).str.contains(value, case=False)]
        
        context = analyze_data(df)
        context['filter_form'] = filter_form
        context['file_path'] = file_path
        
        return render(request, 'myapp/results.html', context)

def analyze_data(df):
    summary = df.describe().to_html()
    head = df.head().to_html()
    
    numerical_columns = df.select_dtypes(include=[np.number]).columns
    
    plots = []
    for col in numerical_columns[:3]:
        plt.figure(figsize=(10, 5))
        sns.histplot(df[col], kde=True)
        plt.title(f'Distribution of {col}')
        
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()
        
        graphic = base64.b64encode(image_png).decode('utf-8')
        plots.append(graphic)
        plt.close()
    
    missing_data = df.isnull().sum().to_frame().reset_index()
    missing_data.columns = ['Column', 'Missing Values']
    missing_data['Percentage'] = (missing_data['Missing Values'] / len(df)) * 100
    missing_data = missing_data.to_html()
    
    return {
        'summary': summary,
        'head': head,
        'plots': plots,
        'missing_data': missing_data,
    }