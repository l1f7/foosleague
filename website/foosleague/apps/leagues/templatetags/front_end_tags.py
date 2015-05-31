from django.template import Library
from django import template

register = Library()


@register.simple_tag
def template_dir(this_object):
    output = dir(this_object)
    return "<code>%s</code>" % str(output)


@register.simple_tag
def template_meta(this_object):
    meta = dir(this_object._meta)
    return "<code>%s</code>" % str(meta)


@register.simple_tag
def template_class(this_object):
    cls = this_object.__class__
    return "<code>%s</code>" % str(cls)


@register.simple_tag
def template_dict(this_object):
    output = this_object.__dict__
    return "<code>%s</code>" % str(output)


@register.simple_tag
def template_repr(this_object):
    output = this_object.__repr__
    return "<code>%s</code>" % str(output)


@register.tag(name='captureas')
def do_captureas(parser, token):
    """
    Capture a block's content for re-use throughout a template.
    particularly handy for use within social meta fields that are
    virtually identical

        {% captureas meta_image %}{% block meta_image %}{% endblock %}{% endcaptureas %}
        ..
        {% if meta_image %}<meta itemprop="image" content="{{ meta_image }}">{% endif %}

    """
    try:
        tag_name, args = token.contents.split(None, 1)
    except ValueError:
        raise template.TemplateSyntaxError("'captureas' node requires a variable name.")
    nodelist = parser.parse(('endcaptureas',))
    parser.delete_first_token()
    return CaptureasNode(nodelist, args)


class CaptureasNode(template.Node):
    def __init__(self, nodelist, varname):
        self.nodelist = nodelist
        self.varname = varname

    def render(self, context):
        output = self.nodelist.render(context)
        context[self.varname] = output
        return ''

