from django.shortcuts import render
# from .models import Container
from .apis import create_container_with_owner
# Create your views here.


def index(request):
    if request.method == 'POST':
        name_container = request.POST.get("name_container")
        name_owner = request.POST.get("name_owner")
        ssh_key = request.POST.get("ssh_key")

        # container = Container(name_container, name_owner, ssh_key)
        # container.save()
        container_ip = create_container_with_owner(name_container, name_owner, ssh_key)
        return render(request, "get_container_id.html", locals())

    return render(request, "index.html", locals())