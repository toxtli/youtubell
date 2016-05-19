import time
import json
import cherrypy
import requests
from pytube import YouTube

class RootServer:

    @cherrypy.expose
    def default(self, *args, **kwargs):
        url = cherrypy.url(qs=cherrypy.request.query_string)
        print url
        if '/watch?' in url:
            error = False
            url = url.replace('youtubell','youtube')
            try:
                yt = YouTube(url)
            except:
                error = True
            if not error:
                video = yt.filter('mp4')[-1]
                raise cherrypy.HTTPRedirect(video.url)
            else:
                return 'Invalid URL or the video is private or requires login.'
        else:
            return 'Incorrect input.'

if __name__ == '__main__':
    server_config={
        'server.socket_host': '0.0.0.0',
        'server.socket_port':443,
        'server.ssl_module':'pyopenssl',
        'server.ssl_certificate':'2_youtubell.com.crt',
        'server.ssl_private_key':'private.key',
        'server.ssl_certificate_chain':'1_root_bundle.crt'
    }
    cherrypy.config.update(server_config)
    cherrypy.quickstart(RootServer(),'/')