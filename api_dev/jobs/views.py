from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import jobs
from .serialzier import job_serializer

# Create your views here.

class create_job(APIView):
    def get(self, request, job_id):
            print('hii')
            
            try:
                if request.GET.get('status'):
                    jobs_list = jobs.objects.filter(status=request.GET.get('status'))

                if request.GET.get('page') and request.GET.get('page_size'):
                    jobs_list = jobs.objects.all().limit(request.GET.get('page_size'))
                

                else:
                    jobs_list = jobs.objects.filter(job_id=job_id)
                serializer = job_serializer(jobs_list, many=True)
                return Response(serializer.data)
            except Exception as e:
                return Response({'error': str(e)})

            
    def post(self, request):
        try:
            job_type = request.data.get('job_type')
            site_id = request.data.get('site_id')
            priority = int(request.data.get('priority'))
            status = request.data.get('status', 'queued') 
            if priority is None or priority < 0:
                return Response({'error': 'Please Provide the Valid Priority'}) 

            data = {
                "job_type": job_type,
                "site_id": site_id,
                "priority": priority,
                "status": status
            }
        
            serializer = job_serializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'message': 'Job created successfully', 'jobs': serializer.data})
            else:
                return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        


       # job = jobs.objects.create(job_type=job_type,site_id=site_id,priority=priority,status=status)
        # return Response({'message': 'Job created successfully', 'job_id': job.job_id}, status=status.HTTP_201_CREATED)



# data = {
#     "job_type":"weather_sync",
#     "site_id": "SITE-101",
#     "priority":3
# }



