from import_export import resources
from . models import Equipment_SI

class EquipmentSIResources(resources.ModelResource):
    class Meta:
        model = Equipment_SI
