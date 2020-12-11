from __future__ import print_function
import time
import boto3
transcribe = boto3.client('transcribe')
job_name = "job name"
job_uri = "s3://psyducks-cs446/BabyTalk.wav"
transcribe.start_transcription_job(
	TranscriptionJobName=job_name,
	Media={'MediaFileUri': job_uri},
	MediaFormat='wav',
	LanguageCode='en-US'
)
while True:
	status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
	if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
		break
	print("Not ready yet...")
	time.sleep(5)
print(status)