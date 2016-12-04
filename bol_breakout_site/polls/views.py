from django.http import HttpResponse



from django.http import StreamingHttpResponse
import json

def index(request):
	
	if request.method=='POST':
		return HttpResponse("Hello POST"+str(received_json_data))

		received_json_data=json.loads(request.POST['data'])
		#received_json_data=json.loads(request.body)
		#return StreamingHttpResponse('it was post request: '+str(received_json_data))
		#return HttpResponse("Hello POST"+str(received_json_data))

	return HttpResponse("Bye")
