from django.contrib import admin
from . import models

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    fields = ['name','quantity','description','price','active']
    search_fields = ['name']
    actions = ['download_csv']
    list_display = ['name','description','price','active','quantity']
    list_display_links = ['name']
    list_editable = ['price','active','quantity']
    list_filter = ['name','description','price','active','quantity']

    def download_csv(self, request, queryset):
        import csv
        from django.http import HttpResponse
        from io import StringIO

        f = StringIO()
        writer = csv.writer(f)
        writer.writerow(['name','price','active','quantity',])

        for s in queryset:
            writer.writerow([s.name, s.price, s.active, s.quantity])

        f.seek(0)
        response = HttpResponse(f, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=stat-info.csv'
        return response

# Register your models here.

admin.site.register(models.Order)
admin.site.register(models.Product,ProductAdmin)
