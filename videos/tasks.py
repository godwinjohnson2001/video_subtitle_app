
import os
import subprocess
import logging
from celery import shared_task
from django.conf import settings
from .models import Video, Subtitle

# Set up logging
logger = logging.getLogger(__name__)

@shared_task
def extract_subtitles_task(video_id):
    try:
        # Fetch video from the database
        video = Video.objects.get(id=video_id)
        video_path = video.video_file.path
        

        ccextractor_path = r'C:\Program Files (x86)\CCExtractor\ccextractor.exe'  # Use the full path to CCExtractor

        # Temporary subtitle file path
        subtitle_output_path = os.path.join(settings.MEDIA_ROOT, f'{video.title}_sub.srt')

        # CCExtractor command to extract subtitles
        command = [ccextractor_path, video_path, '-o', subtitle_output_path]

        # Execute the command and capture the result
        result = subprocess.run(command, capture_output=True, text=True)

        # Check if the process was successful
        if result.returncode != 0:
            logger.error(f"CCExtractor failed with error: {result.stderr}")
            return {'status': 'failed', 'error': result.stderr}

        # Save the subtitles in the database if the file exists
        if os.path.exists(subtitle_output_path):
            with open(subtitle_output_path, 'r') as subtitle_file:
                content = subtitle_file.read()

            # Create subtitle record in the database
            Subtitle.objects.create(video=video, content=content, subtitle_file=subtitle_output_path)

            return {'status': 'success', 'message': 'Subtitles extracted successfully'}

        else:
            logger.error(f"Subtitle file not found at: {subtitle_output_path}")
            return {'status': 'failed', 'error': 'Subtitle file not created'}

    except Video.DoesNotExist:
        logger.error(f"Video with ID {video_id} does not exist.")
        return {'status': 'failed', 'error': 'Video not found'}

    except Exception as e:
        logger.error(f"An error occurred: {str(e)}")
        return {'status': 'failed', 'error': str(e)}
