from django import forms
from .models import Employee
from .models import Position




class AddEmployeeForm(forms.ModelForm):


    class Meta:
        model = Employee
        fields = ["name", "employee_position_q", "salary_amount", "foto_employee", 'parent'] #

        #field2 = forms.ModelChoiceField(queryset=Position.objects.all(), to_field_name="1", to_field_name="2")

    # def as_p(self):
    #     "Returns this form rendered as HTML <p>s."
    #     return self._html_output(
    #         normal_row=u'<p%(html_class_attr)s>%(label)s</p> %(field)s%(help_text)s',
    #         error_row=u'%s',
    #         row_ender='</p>',
    #         help_text_html=u' <span class="helptext">%s</span>',
    #         errors_on_separate_row=True)

    # def as_plain(self):
    #     "Returns this form rendered as HTML <tr>s -- excluding the <table></table>."
    #     return self._html_output(
    #         normal_row='%(label)s%(errors)s%(field)s%(help_text)s',
    #         error_row='%s',
    #         row_ender=' ',
    #         help_text_html='<br /><span class="helptext">%s</span>',
    #         errors_on_separate_row=False)