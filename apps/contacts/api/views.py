from rest_framework import generics
from .serializer import ContactSerializer
from ..models import Contact


class ContactCreateAPIView(generics.CreateAPIView):
    # http://127.0.0.1:8000/contact/create
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
