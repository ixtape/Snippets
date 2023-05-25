from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from MainApp.models import Snippet
from MainApp.forms import SnippetForm
from django.core.exceptions import ObjectDoesNotExist


def index_page(request):
    context = {"pagename": "PythonBin"}
    return render(request, "pages/index.html", context)


def add_snippet_page(request):
    if request.method == "GET":
        form = SnippetForm()
        context = {"pagename": "Добавление нового сниппета", "form": form}
        return render(request, "pages/add_snippet.html", context)
    if request.method == "POST":
        form = SnippetForm(request.POST)

        if form.is_valid():
            form.save()
        return redirect("snippets-list")
    return render(request, "pages/add_snippet.html", {"form": form})


def snippets_page(request):
    snippets = Snippet.objects.all()
    context = {"pagename": "Просмотр сниппетов", "snippets": snippets}

    return render(request, "pages/view_snippets.html", context)


def snippet_detail(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
        context = {"pagename": "Просмотр сниппета", "snippet": snippet, "type": "view"}

        return render(request, "pages/snippet_detail.html", context)
    except ObjectDoesNotExist:
        raise Http404


def snippet_delete(request, snippet_id):
    snippet = Snippet.objects.get(id=snippet_id)
    snippet.delete()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))


def snippet_edit(request, snippet_id):
    try:
        snippet = Snippet.objects.get(id=snippet_id)
    except ObjectDoesNotExist:
        raise Http404
    if request.method == "GET":
        context = {
            "pagename": "Редактирование сниппета",
            "snippet": snippet,
            "type": "edit",
        }

        return render(request, "pages/snippet_detail.html", context)
    if request.method == "POST":
        form_data = request.POST
        snippet.name = form_data["name"]
        snippet.code = form_data["code"]
        snippet.creation_date = form_data["creation_data"]
        snippet.save()
        return redirect("snippets-list")
