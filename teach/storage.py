from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import os, time, random
from django.conf import settings

class FileStorage(FileSystemStorage):    
    def __init__(self, location=settings.MEDIA_ROOT, base_url=settings.MEDIA_URL):
        super(FileStorage, self).__init__(location, base_url)
        
    def _save(self, name, content):
        ext = os.path.splitext(name)[1]
        d = os.path.dirname(name)
        fn = time.strftime('%Y%m%d%H%M%S')
        fn = fn + '_%d' % random.randint(0,100)
        name = os.path.join(d, fn + ext)
        return super(FileStorage, self)._save(name, content)