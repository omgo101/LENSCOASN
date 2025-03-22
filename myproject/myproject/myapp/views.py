from django.shortcuts import render
import pandas as pd
from django.http import JsonResponse

# Import Excel function
def import_excel(request):
    if request.method == 'POST':
        excel_file = request.FILES['file']
        data = pd.read_excel(excel_file)
        
        # Example: Return JSON response of Excel data
        data_dict = data.to_dict(orient='records')
        return JsonResponse({'data': data_dict})
    
    return render(request, 'home.html')
def home(request):
    return render(request, 'home.html')