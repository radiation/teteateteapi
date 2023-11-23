from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserListCreateView.as_view(), name='user-list-create'),
    path('user/create/', UserListCreateView.as_view(), name='user-create'),
    path('user/id/<int:id_value>', UserListByIDView.as_view(), name='user-list-create'),

    path('meeting/', MeetingListView.as_view(), name='meeting-list'),
    path('meeting/create/', MeetingCreateView.as_view(), name='meeting-create'),
    path('meeting/user/<int:user_id_value>', MeetingListByUserView.as_view(), name='meeting-list-by-user'),

    path('actionitem/', UserListCreateView.as_view(), name='actionitem-list-create'),
    path('actionitem/create/', ActionItemListCreateView.as_view(), name='actionitem-create'),
    path('actionitem/user/<int:user_id_value>', ActionItemListByUserView.as_view(), name='actionitem-list-create'),
    path('actionitem/meeting/<int:meeting_id_value>', ActionItemListByUserView.as_view(), name='actionitem-list-create'),

    path('question/', QuestionListCreateView.as_view(), name='question-list-create'),
    path('question/create/', QuestionListCreateView.as_view(), name='question-create'),
    path('question/id/<int:id_value>', QuestionListByIDView.as_view(), name='question-list-create'),

    path('questionanswer/', QuestionAnswerListCreateView.as_view(), name='questionanswer-list-create'),
    path('questionanswer/create/', QuestionAnswerListCreateView.as_view(), name='questionanswer-create'),
    path('questionanswer/id/<int:id_value>', QuestionAnswerListByIDView.as_view(), name='questionanswer-list-create'),    
]
