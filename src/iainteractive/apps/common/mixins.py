"""Common Mixins module"""

# Django
from django.http import HttpResponse

# Others
import csv


class ExportCsvMixin:
    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)

        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([self.print_object_field(obj, field) for field in field_names])

        return response

    def print_object_field(self, obj, field):
        if field == 'city':
            return obj.get_city_display()
        return getattr(obj, field)

    export_as_csv.short_description = "Export Selected"