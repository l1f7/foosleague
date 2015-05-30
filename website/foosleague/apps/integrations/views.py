from django.shortcuts import render

# class GetStreakHolder(TemplateView):

#     template_name = 'integrations/streak.html'

#     def get(self, *args, **kwargs):
#         # try:
#         token = self.request.GET.get('token')
#         if token == 'asdgasdhasdhasdhasdhasdh':
#             text = self.request.GET.get('text')
#             user_name = self.request.GET.get('user_name')

#             try:
#                 staff = Staff.objects.get(slack_username=user_name)
#                 user_name = staff.name.split()[0]
#             except:
#                 user_name = self.request.GET.get('user_name')

#             fo = open('responses.txt', 'wb+')
#             fo.write("%s says: %s" % (user_name, text,))
#             fo.close()

#         return super(ReceiveMessage, self).get(*args, **kwargs)
#         # except:
#         #     return HttpResponseNotFound('<h1>Page not found</h1>')

