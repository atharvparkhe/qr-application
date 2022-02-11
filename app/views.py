from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
import uuid, qrcode, cv2


@api_view(["POST"])
def generateQR(request):
    try:
        ser = GenerateSerializer(data = request.data)
        if ser.is_valid():
            qr = qrcode.make(ser.data["text"])
            file_name = "data/download/" + str(uuid.uuid4()) + ".jpeg"
            qr.save(file_name)
            return Response({"message":"QR Generated", "file":file_name}, status=status.HTTP_200_OK)
        return Response({"error":ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["POST"])
def readQR(request):
    try:
        ser = ReadSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            d = cv2.QRCodeDetector()
            text, _, _ = d.detectAndDecode(cv2.imread(str(ser.data["file"])[1:]))
            if not text:
                return Response({"message":"Invalid Image. Upload image of QR code."}, status=status.HTTP_403_FORBIDDEN)
            return Response({"message":"QR Decoded", "text":text}, status=status.HTTP_200_OK)
        return Response({"error":ser.errors}, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"error":str(e), "message":"Something went wrong"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)