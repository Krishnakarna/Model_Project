from django.contrib import admin
from Model_App.models import EmployeeModel
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['eno','ename','adress','salary','mail']
    list_editable = ['salary']
    list_filter = ['adress']
    readonly_fields = ['ename']
    list_per_page = 2
    search_fields = ['salary']
    exclude = ['adress']
    fields = ['eno','ename']
    list_display_links = ['ename']
admin.site.register(EmployeeModel,EmployeeModelAdmin)




