from rest_framework import serializers
from quickstart.models import Account
from quickstart.models import UserPledge
from quickstart.models import pledgefeed


class RegistrationSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},write_only = True)
    """serialisizes a user profile"""
    class Meta:
        model = Account
        fields = ('email','username','password','password2')
        extra_kwargs = {
        'password': {
        'write_only': True,
        'style': {'input_type': 'password'}
        }
        }
    def save(self):
        account = Account(
                        email= self.validated_data['email'],
                        username = self.validated_data['username'],)
        password = self.validated_data['password']


        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Password must match'})
        account.set_password(password)
        account.save()
        return account

class PledgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = pledgefeed
        fields = ( 'title','details','totalmoney','photo','deadline')

class PledgeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = pledgefeed
        fields = ( 'id','title','photo','amountraised','totalmoney','deadline','author')

class PledgeDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = pledgefeed
        fields = ( 'id','title','details','totalmoney','photo','amountraised','deadline','author','timedates')

class MessageAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPledge
        fields = ('user','pledge','amountpledged','timedates','message')