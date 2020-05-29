from import_export import resources
from fees.models import Fee
from .models import Student
from django.contrib.auth.hashers import make_password

class FeesResource(resources.ModelResource):

    class Meta:
        model = Fee
        fields = ('student__code','student__username', 'school', 'student__grade', 'value','bank_account','created','payment_date')
        export_order = ('student__code','student__username', 'school', 'student__grade', 'value','bank_account','created','payment_date')

class StudentResource(resources.ModelResource):
    def before_import_row(self,row, **kwargs):
        value = row['password']
        row['password'] = make_password(value)

    class Meta:
        model = Student
        import_id_fields = ('code',)
        fields = ('code','username', 'password','school', 'grade', 'study_fees', 'study_payment', 'bus_fees','message','total_paid')
        export_order = ('code','username', 'password','school', 'grade', 'payment_1', 'payment_2', 'bus_fees','message','total_paid')
