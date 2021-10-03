from chirps.models import Chirp
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

class ChirpsHandler(View):
    
    def get(self, request):
        chirps = Chirp.objects.all()
        chirps_count = Chirp.objects.count()
        
        chirps_serialized_data = []  # to store serialized data
        for chirp in chirps:
            chirps_serialized_data.append({
                'id': chirp.id,
                'text': chirp.text,
            })

        data = {
            'chirps': chirps_serialized_data,
            'count': chirps_count,
        }

        return JsonResponse(data)