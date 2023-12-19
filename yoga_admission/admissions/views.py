from django.shortcuts import render,HttpResponse

# Create your views here.
# admissions/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import YogaParticipant
from .serializers import YogaParticipantSerializer

def index(request):
    return render(request, 'index.html')


@api_view(['POST'])
def enroll_participant(request):
    if request.method == 'POST':
        data = request.data

        # Basic validation
        age = data.get('age')
        if not (18 <= age <= 65):
            return Response({'error': 'Invalid age. Age should be between 18 and 65.'}, status=status.HTTP_400_BAD_REQUEST)

        # Mock function for payment (replace this with actual payment logic)
        payment_response = CompletePayment(data)

        # Check the payment status
        if payment_response['payment_status'] == 'success':
            # Save participant data to the database
            serializer = YogaParticipantSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Enrollment successful'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Invalid data. Unable to save participant.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            # Payment failed, return an error response
            return Response({'error': 'Enrollment failed. Payment not completed.'}, status=status.HTTP_400_BAD_REQUEST)

# Mock payment logic
def CompletePayment(user_data):
    try:
        # Perform payment logic here (this is a mock function)
        payment_status = 'success'
        message = 'Payment successful'
    except Exception as e:
        # Handle payment failure
        payment_status = 'failure'
        message = f'Payment failed: {str(e)}'

    return {'payment_status': payment_status, 'message': message}