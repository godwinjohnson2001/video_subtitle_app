from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Video, Subtitle
from .forms import VideoForm
from .tasks import extract_subtitles_task
from django.db.models import Q
import os
from django.conf import settings



# Create your views here.

def video_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            video = form.save()

            # Run subtitle extraction in the background
            extract_subtitles_task.delay(video.id)

            return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'video_upload.html', {'form': form})

def video_list(request):
    videos = Video.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    subtitles = video.subtitles.all()
    return render(request, 'video_detail.html', {'video': video, 'subtitles': subtitles})

def search_subtitles(request, video_id):
     try:
        # Ensure video exists
        video = Video.objects.get(id=video_id)
     except Video.DoesNotExist:
        return JsonResponse({'error': 'Video not found'}, status=404)

     query = request.GET.get('q', '')

     if query:
        # Get all subtitles for the video
        subtitles = Subtitle.objects.filter(video=video)
        results = []

        for subtitle in subtitles:
            # Full path to the subtitle file
            subtitle_path = os.path.join(settings.MEDIA_ROOT, str(subtitle.subtitle_file))

            if os.path.exists(subtitle_path):
                with open(subtitle_path, 'r', encoding='utf-8') as f:
                    content = f.read()

                    # Search for query in subtitle content
                    if query.lower() in content.lower():
                        results.append({
                            'language': subtitle.language,
                            'content': content,  
                            'subtitle_file': subtitle.subtitle_file.url, 
                            'timestamp': '00:00:00'  
                        })

        return JsonResponse({'results': results})
    
        return JsonResponse({'results': []})