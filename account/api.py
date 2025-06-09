from django.http import JsonResponse
from rest_framework.decorators import api_view,authentication_classes, permission_classes

from account.forms import SignupForm

@api_view(['POST'])
@authentication_classes([])  # No authentication required for signup
@permission_classes([])  # No permission required for signup
def signup(request):
    """
    Endpoint per la registrazione di un nuovo utente.
    """
    data = request.data
    message = 'success'
    code = 201 #code for success on creation
    form = SignupForm({
        'email': data.get('email'),
        'name': data.get('name'),
        'password1': data.get('password1'),
        'password2': data.get('password2')
    }
     )
    if form.is_valid():
        form.save()
        #TODO: send email to user for verification
    else:
        message = ''
        if form.errors:
            for field, errors in form.errors.items():
                
                message += f"{'\n'.join(errors)} "
                message +="\n"
            print(message)
               
               
            
        else:
            message = 'Invalid data provided'
        code = 400 #code for bad request
    
    
    
    return JsonResponse({'message': message}, status=code)