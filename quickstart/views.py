from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from quickstart.serializers import RegistrationSerializer
from quickstart.serializers import PledgeSerializer, PledgeListSerializer,PledgeDetailSerializer,MessageAccountSerializer
from quickstart.models import pledgefeed
from quickstart.models import Account,UserPledge
from django.http.response import JsonResponse
import requests

from rest_framework_simplejwt.tokens import RefreshToken


from datetime import date
# Create your views here.



#Reg view
@api_view(['POST',])
def registration_view(request):
    if request.method=='POST':
        serializer = RegistrationSerializer(data = request.data)
        data={}
        if serializer.is_valid():
            account= serializer.save()
            data['response']= "Your profile was successfully created"
            data['email'] = account.email
            tr=account.email
            data['username'] = account.username
            # acc = Account.objects.get(email=tr)
            # print(acc)
            # rt=acc.id
            # print(rt)
            # refresh = RefreshToken.for_user(tr)
            # print(refresh)
            # data['token']=refresh.access_token
            url = 'http://127.0.0.1:8000/api/v1/login/'
            myobj = {'email': tr,
                     'password':'password'}

            x = requests.post(url, data=myobj)

            print(x.json())
            data['token'] = x.json()['access']

        else:
            data = serializer.errors

        return Response(data)

@api_view(['POST',])
@permission_classes((IsAuthenticated,))
def pledge_view(request):
    #acc = Account.objects.get(pk=3)
    acc =request.user
    accc = Account.objects.get(email=acc)
    acc=accc.username
    print(acc)

    pledge_feed= pledgefeed(author= accc.username)
    # pledger_list = pledge_feed.get_all_pledge()
    if request.method=='POST':
        serializer = PledgeSerializer(pledge_feed, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            # return Response({'details':serializer.data, 'pledgers':}, status=status.HTTP_201_CREATED)
            return Response({'details':serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', ])
def pledge_list_view(request):

    if request.method == 'GET':
        snippets = pledgefeed.objects.all()
        serializer = PledgeListSerializer(snippets, many=True)

        return Response(serializer.data)

@api_view(['GET','POST', ])
@permission_classes((IsAuthenticated,))
def pledge_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """

    try:
        snippet = pledgefeed.objects.get(id=pk)
    except pledgefeed.DoesNotExist:
        return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        snip2 = UserPledge.objects.filter(pledge=pk)

        tutorial_serializer = PledgeDetailSerializer(snippet)
        data = tutorial_serializer.data
        total= data['totalmoney']
        amountraised=data['amountraised']
        data['amountremaining'] = total-amountraised
        message_serializer = MessageAccountSerializer(snip2,many=True)
        answers_list = list(snip2)

        return JsonResponse({'details':data,'pledger':message_serializer.data}, status=status.HTTP_201_CREATED)

        # return JsonResponse(tutorial_serializer.data)
    elif request.method == 'POST':
        data = request.data
        pledge = pledgefeed.objects.get(id=pk)
        se=int(data['amount'])
        pledgefeed.objects.filter(id=pk).update(amountraised=pledge.amountraised +se )

        user_that_pledged= request.user.username
        # user_that_pledged = User.objects.get(username=request.user.username)
        UserPledge.objects.create(
        user = user_that_pledged,
        pledge = pledge.id,
        amountpledged = se,
        message = data['message'],
        author = pledge.title
        )
        snippet = pledgefeed.objects.get(id=pk)
        tutorial_serializer = PledgeDetailSerializer(snippet)
        return JsonResponse(tutorial_serializer.data)


#
# @api_view(['POST', ])
# def pledge_detail(request, pk):
