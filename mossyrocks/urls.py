from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'news.views.index', name='home'),
     url(r'^login/$', 'django.contrib.auth.views.login'),
     url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
     url(r'^addtourdate/$', 'news.views.addtourdate'),
     url(r'^editcontact/$', 'news.views.editcontact'),
     url(r'^addSounds/$', 'news.views.addSounds'),
     url(r'^deleteSounds/(\d+)/$', 'news.views.deleteSounds'),
     url(r'^deleteStory/(\d+)/$', 'news.views.deleteStory'),
     url(r'^deleteTourdate/(\d+)/$', 'news.views.deleteTourdate'),
    #url(r'^mossyrocks/', include('mossyrocks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
