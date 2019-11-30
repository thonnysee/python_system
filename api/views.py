from django.contrib.auth import get_user_model


from rest_auth.registration.views import RegisterView


class CustomRegisterView(RegisterView):
    queryset = get_user_model().objects.all()
