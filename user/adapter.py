from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):
    def save_user(self,request,user,form,commit=True):

        user = super(AccountAdapter,self).save_user(request,user,form,commit=True)

        user.years_in_germany = form.cleaned_data.get("years_in_germany")
        user.date_moved_to_germany = form.cleaned_data.get("date_moved_to_germany")
        user.save()