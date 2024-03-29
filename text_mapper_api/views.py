"""
Module providing views for the ParaSearcher API.
"""

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import CustomUser, Paragraph, Word
from .serializers import CustomUserSerializer, ParagraphSerializer


class SignUpView(generics.CreateAPIView):
    """
    View for user signup.
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class LoginView(APIView):
    """
    View for user login.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Authenticate user and generate tokens.
        """
        email = request.data.get('email')
        password = request.data.get('password')
        user = CustomUser.objects.filter(email=email).first()

        if user and user.check_password(password):
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            })
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class RefreshTokenView(APIView):
    """
    View for refreshing access token using refresh token.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Generate a new access token using a refresh token.
        """
        refresh_token = request.data.get('refresh_token')

        if not refresh_token:
            return Response({'error': 'Refresh token is required'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            refresh_token = RefreshToken(refresh_token)
            access_token = str(refresh_token.access_token)
            return Response({'access_token': access_token}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': 'Invalid refresh token'}, status=status.HTTP_401_UNAUTHORIZED)


class ParagraphCreateView(APIView):
    """
    View for creating paragraphs.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """
        Create paragraphs and associated words.
        """
        paragraphs = request.data.get('paragraphs', [])
        for paragraph_text in paragraphs.split('\n\n'):
            paragraph = Paragraph.objects.create(text=paragraph_text.strip())
            words = paragraph_text.lower().split()
            for word in words:
                Word.objects.create(word=word, paragraph=paragraph)
        return Response({'message': 'Paragraphs and words created successfully'}, status=status.HTTP_201_CREATED)


class SearchView(APIView):
    """
    View for searching paragraphs by word.
    """
    permission_classes = [IsAuthenticated]

    def get(self, request):
        """
        Search paragraphs by word.
        """
        print(request.user)
        word = request.query_params.get('word', '').lower()
        if not word:
            return Response({'error': 'Word parameter is required'}, status=status.HTTP_400_BAD_REQUEST)

        matching_paragraphs = Paragraph.objects.filter(
            words__word=word).distinct()
        serializer = ParagraphSerializer(matching_paragraphs, many=True)
        return Response(serializer.data)
