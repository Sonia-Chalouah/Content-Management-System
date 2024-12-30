from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.db.models import Q
from .models import WordPhrase

def word_list(request):
    # Search functionality
    query = request.GET.get('q', '')  # Get the 'q' parameter from the URL
    words = WordPhrase.objects.filter(
        Q(word_phrase__icontains=query) | Q(translation__icontains=query)
    ) if query else WordPhrase.objects.all()

    # Pagination
    paginator = Paginator(words, 10)  # 10 entries per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'query': query,
    }
    return render(request, 'content/word_list.html', context)

def edit_word(request, pk):
    word = get_object_or_404(WordPhrase, pk=pk)

    if request.method == 'POST':
        word.word_phrase = request.POST.get('word_phrase')
        word.translation = request.POST.get('translation')
        word.example_sentence = request.POST.get('example_sentence')
        word.save()
        return redirect('word_list')  # Redirect back to the list page

    context = {
        'word': word,
    }
    return render(request, 'content/edit_word.html', context)
