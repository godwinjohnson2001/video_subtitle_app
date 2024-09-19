# video_subtitle_app
# Django Video subtitle app with Subtitle extraction and Search Functionality.

This is a Django-based project that allows users to upload video files, extract subtitles (multi-language), display them as closed captions, and search within the subtitles. The project is integrated with PostgreSQL for database management and uses CCExtractor to extract subtitles from the videos.

## Features

1. **Video Upload**: Users can upload video files to the platform.
2. **Subtitle Extraction**: Automatically extracts multi-language subtitles using CCExtractor and stores them in the PostgreSQL database and .SRT file is stored in project's media folder.
3. **Subtitle Search**: Users can search for specific phrases within the subtitles and retrieve the exact timestamps. Clicking on a timestamp starts the video from that point.(Unfortunately this feature is not working as expected.) 
4. **List View of Uploaded Videos**: A list of all uploaded videos, which can be selected to view and interact with.

## Technology Stack

- **Backend**: Django
- **Database**: PostgreSQL
- **Subtitle Extraction**: [CCExtractor](https://www.ccextractor.org/)
- **Frontend**: HTML, CSS (Django templates)
- **Search Functionality**: Case-insensitive search within subtitles
- **Media Management**: Django handles media files (videos and subtitles)

## Prerequisites

1. **Python 3.6+**
2. **PostgreSQL**
3. **Django 3.0+**
4. **CCExtractor** installed on the system. Download from [CCExtractor](https://www.ccextractor.org/).


## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/godwinjohnson2001/video_subtitle_app.git
cd video_subtitle_app
```
### 2. Install the required python packages
```bash
pip install -r requirements.txt
```
### 3. Configure PostgreSQL
```sql
CREATE DATABASE video_dba;
CREATE USER postgres WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE video_dba TO postgres;
```
If any problem while configuring postgreSQL first check that the python package named psycopg2 is installed or not. It must be installed when we run requirements.txt.

### 4. Update the DATABASES setting in the settings.py file
```settings.py
# video_subtitle_app/settings.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'video_dba',
        'USER': 'postgres',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 6. Download and Install CCExtractor based on your OS
```download from here
https://ccextractor.org/public/general/downloads/
```
After downloading do these steps for windows users...
(1.)Unzip the contents to a folder, for example C:\Program Files (x86)\CCExtractor. Copy the path to it and add it to the the PATH system variable.

  (a)Open File Explorer, right-click on "This PC" and click on Properties.

  (b)On the System panel select Advanced system settings.

  (c)On the Advanced tab, click Environment Variables... and edit the PATH system variable to add the path you copied (use a ; to separate values).

(2.)Rename ccextractorwin.exe to ccextractor.exe.

After the completion of this process open cmd from a video included folder and run the command  "ccextractor videoname.video_extension".After completing the task it says success or failure,if success, then it creates .SRT file and that SRT file contains the subtitle of this video. If it shows "No captions where found in the Input" then don't get panic because ccextractor works only with some videos only.

### 7. Run Celery worker
```bash
celery -A video_subtitle_app worker -P eventlet
```
Celery is configured to handle background tasks like video processing, subtitle extraction, and potentially other time-consuming operations.
### 8. Run the Development Server
```bash
python manage.py runserver
```
Both 7 and 8 must be run simultaneously, so first run celery worker on a terminal and then take another terminal and run the development server.Because both must be run while dealing with this project.

## How to Use
### 1. Uploading Videos
  (a). Navigate to http://127.0.0.1:8000/upload/ to upload a video.
  (b). The uploaded video will be processed, and subtitles in multiple languages (English, Spanish, and French by default) will be extracted and stored.

### 2. Video List and Playback
  (a). Go to http://127.0.0.1:8000/videos/ to see the list of uploaded videos.
  (b). Click on a video title to view the video with integrated subtitles.
### 3. Search Subtitles
  (a). On the video detail page, use the search bar to enter a phrase.
  (b). The system will return the matching phrases along with their timestamps.
  (c). Clicking on a timestamp will play the video from that specific point.


## Successful Subtitle Extraction
In the successful case, CCExtractor was able to process the uploaded video and generate two .srt files:
1. First .srt file: This file is located in the root of the media folder.This is 0 byte sized file which does not contain anything.
2. Second .srt file: This file is located inside the media folder, within a subfolder named video, which contains both the uploaded video and the extracted .srt file.
### File Structure:
(a) /media
(b) extracted_subtitle.srt (First .srt file)
(c) /video
       (1.) uploaded_video.mp4 (The original uploaded video)
       (2.) extracted_subtitle.srt (Second .srt file, specific to the video)


## Most Challenging task
Most challenging task that i faced while developing this project is the subtitle extraction with CCExtractor. I have spend more time to work with CCExtractor. Actually the problem is CCExtractor generates subtitle, with only some of the videos only. Another most challenging task is the runnig of celery worker, i have runned the celery worker with a different command that i mentioned here then it raises the error 'value not found error(expected 3 and got 0)' then i search this problem with may of the sites and friends and last i got that, download the python package eventlet and then run this command "celery -A video_subtitle_app worker -p eventlet" hence it works. Eventlet is a Python networking library that supports concurrency via green threads, which are lightweight, cooperative threads that allow you to manage concurrency without the overhead of traditional operating system threads. These are the most challenging tasks that was faced while developing this project.

## About Docker-compose.yml file
I initially aimed to use Docker for containerizing the project and included a docker-compose.yml configuration. This was to ensure easy setup and deployment, allowing for consistent development and production environments.Despite investing significant time and effort in troubleshooting, I encountered persistent issues with Docker not running properly on my system. Due to time constraints and the submission deadline for this project, I was unable to fully integrate Docker as planned.Also i am dealing with docker first time.
Therefore, Docker support has been excluded from this version of the project.Hence run the project without Docker, please follow the instructions for the standard Python/Django setup as described above.

## Screenshots
The screenshots of different images related to this project is added in the screenshot folder. These screenshots serve as a visual reference to better understand the user experience and functionality of the project.

## About search functionality
This project was designed to include a search functionality that allows users to search for specific phrases within the video and retrieve the corresponding timestamps. However, due to time constraints, the search feature is not fully functional and may not work as expected in this version. While the groundwork for the search functionality has been implemented, it requires further refinement to handle edge cases and return accurate results. I plan to revisit and improve this feature in the future when time permits.
For now, all other core features, such as video upload and subtitle extraction, are fully operational.

## generated SRT file 
During the development and testing of this project, the given two videos failed to have their subtitles extracted using CCExtractor. Despite multiple attempts, the tool was unable to process these particular files successfully. This could be due to the video format or encoding, which might not be fully supported by CCExtractor.
However, a third video that I uploaded was successfully processed using CCExtractor, and its subtitles were extracted without issues. The generated .srt subtitle file from the video is included in this repository for reference.
 
