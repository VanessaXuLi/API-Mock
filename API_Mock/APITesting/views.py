from django.shortcuts import render, HttpResponse
from django.http import request,JsonResponse

# Create your views here.




def index(request):
    def data1():

        if (request.GET.get('a') is not None) and (request.GET.get('b') is not None):
            print('test')

            m = request.GET.get('a')
            # m = int(m)

            n = request.GET.get('b')
            n = str(n)
            print(m, type(m), n, type(n))
            if (m.isdigit()) and (not n.isdigit()):
                m = int(m)

                err_code = 0
                err_msg = 'success'
                ref = "NO.{:d} is {}".format(m, n)

            else:
                err_code = 11
                err_msg = 'system error'
                ref = 'Fail'

            data = {"error_code": err_code,
                    'error_message': err_msg,
                    'references': ref

                    }
            return data
        else:
            err_code = 11
            err_msg = 'system error'
            ref = 'Fail'
            data = {
                "error_code": err_code,
                'error_message': err_msg,
                'references': ref
            }
            return data

    data = data1()
    print(data)


    return render(request,'index.html',context=data)


