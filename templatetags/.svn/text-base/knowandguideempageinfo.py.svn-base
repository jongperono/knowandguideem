from django import template
from apps.intent.pes.knowandguideem.models.peskgmhierarchy import PesKgmHierarchy
register = template.Library()     

@register.simple_tag
def get_child(pid,html):
    hierarchy = PesKgmHierarchy.objects.filter(parent_id=pid)
    html+="--"
    for parent in hierarchy:
    
        html+=parent.description+"<br>"
        html+="--"
    return html

@register.simple_tag
def parse_hierarchy():
    html=""
    parent = PesKgmHierarchy.objects.all()
    
    for child in parent:
        html=get_child(child.id,html)
        
   
    return html



    



