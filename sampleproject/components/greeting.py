from typing import Any, Dict

from django_components import component


@component.register("greeting")
class Greeting(component.Component):
    def get(self, request, *args, **kwargs):
        slots = {"message": "Hello, world!"}
        context = {"name": request.GET.get("name", "")}
        return self.render_to_response(context, slots)

    def get_context_data(self, name, *args, **kwargs) -> Dict[str, Any]:
        return {"name": name}

    template = """
        <div id="greeting">Hello, {{ name }}!</div>
        {% slot "message" %}{% endslot %}
    """

    css = """
        #greeting {
            display: inline-block;
            color: blue;
            font-size: 2em;
        }
    """

    js = """
        document.getElementById("greeting").addEventListener("click", (event) => {
            alert("Hello!");
        });
    """
