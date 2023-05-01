from rest_framework import routers
from django.urls import path,include
from .import views
from  APP.views import ClassRoomViewset, StudentViewsets , TeacherViewsets , CollegeViewsets


router = routers.DefaultRouter()
router.register(r'classroom',ClassRoomViewset)
router.register(r'college',CollegeViewsets)
router.register(r'teacher',TeacherViewsets)
router.register(r'student',StudentViewsets)

urlpatterns = router.urls
    


# urlpatterns = [
#     path('api/', include('router.urls')),
#     path('college/',views.college_view, name='college'),
#     path('student/',views.students_view, name='student'),
#     path('teacher/',views.teacher_view, name='teacher'),
#     path('class/',views.classroom_view, name='class'),
    

# ]
