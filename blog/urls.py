from django.conf.urls import url


from . import views

urlpatterns = [
    url(r'^$', views.ArticleListView.as_view(), name='blog_index'),
    url(r'^article/publish$', views.ArticlePublishView.as_view(), name='article_publish'),
    url(r'^article/(?P<title>\w+\.?\w+)$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/(?P<title>\w+\.?\w+)/edit$', views.ArticleEditView.as_view(), name='article_edit')
]
