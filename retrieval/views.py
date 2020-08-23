from django.shortcuts import render
from retrieval import main

def result(request):
    return render(request, 'hasil.html')


def import_csv(request):                                                    
    if request.method == 'POST':
        text = request.POST['input_text']
        result, query, execute_time, idnya, scorenya, judulnya, isinya, daerahnya, attrs, proximity, query, queries = main.main(text)
        content = {'result': result, 'query': query, 'execute_time': execute_time, 'idnya': idnya, 'scorenya': scorenya, 'judulnya': judulnya, 'isinya': isinya, 'daerahnya': daerahnya, 'attrs':attrs, 'proximity': proximity, 'query': query, 'queries': queries}
        return render(request, 'hasil.html', content)
    return render(request, 'index.html')

def cerita_page(request, id):
    dict_judul, dict_daerah, dict_text = main.detail()
    contentnya = {'id': id, 'dict_judul' : dict_judul, 'dict_daerah': dict_daerah, 'dict_text': dict_text}
    return render(request, 'cerita.html', contentnya)