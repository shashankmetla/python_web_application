from django.urls import path
from .views import (
    AllCategories,
    CategoryPost,
    PostCreate,
    PostDetail,
    DraftPostList,
    PostUpdate,
)


urlpatterns = [ 
    path("categories/", AllCategories.as_view(), name="categories"),
    path("categories/<slug:slug>/", CategoryPost.as_view(), name="post_by_category"),
    path("write/", PostCreate.as_view(), name="new_post"),
    path("update/<slug:slug>/", PostUpdate.as_view(), name="post_update"),
    path("post/<slug:slug>/", PostDetail.as_view(), name="post_detail"),
    path("drafts/", DraftPostList.as_view(), name="post_draft"),
]
