from django.shortcuts import render



def page_not_found(request, error):

    return render(
        request,
        'core/404.html',
        {'path': request.path},
        status=404
    )

