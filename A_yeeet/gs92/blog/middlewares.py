class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('____one time initialization_______')
        
    def __call__(self, request):
        print('-')
        print('-')
        print('-')
        print('-')
        print('This is before view')
        response = self.get_response(request)
        print('-')
        print('-')
        print('-')
        print('-')
        print('This is after view')
        print('*777777777777')
        return response