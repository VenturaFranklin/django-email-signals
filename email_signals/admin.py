from django.contrib import admin
from . import models, forms

class SignalConstraintInline(admin.TabularInline):
    form = forms.SignalConstraintAdminForm
    model = models.SignalConstraint
    extra = 0


@admin.register(models.Signal)
class SignalAdmin(admin.ModelAdmin):
    list_display = ('name', 'content_type', 'signal_type', 'constraints_count',
                    'active',)

    form = forms.SignalAdminForm
    inlines = [SignalConstraintInline]
