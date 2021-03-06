from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

from datetime import datetime, timedelta

from library.models import *
from book_issue.models import *
from book_issue.serializers import *
from userprofile.serializers import *
from django.http import Http404

class ProfileDetail(APIView):

    def get(self, request, emp_id=None):
        # import pdb
        # pdb.set_trace()
        try:
            profile = UserProfile.objects.get(employee_id=emp_id)
        except UserProfile.DoesNotExist:
            raise Http404("UserProfile Details: Profile not found")

        serializer = ProfileSerializer(profile, many=False)
        return Response(serializer.data)

