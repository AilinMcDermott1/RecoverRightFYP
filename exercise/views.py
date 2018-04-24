# from django.shortcuts import render
#
#
# def exercise(request):
#     search_result2 = {}
#     if 'exercise' in request.POST:
#         form2 = ExerciseForm(request.POST)
#         if form2.is_valid():
#             search_result2 = form2.search2()
#         else:
#             form = ExerciseForm()
#         return render(request, 'nutrition/exercise.html', {'form2': form2, 'search_results2': search_result2})