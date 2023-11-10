import json
import boto3
from PIL import Image, ImageDraw
import PIL.Image
from io import BytesIO

s3_client = boto3.client('s3')
rk_client = boto3.client('rekognition')

def lambda_handler(event, context):
    
    # 需改為自己的 bucket_name
    bucket_name = "tsou-workshop"
    source_image = "HandsOn2_Sakura.jpg"
    
    for i in range(1, 7):
        
        target_image = "HandsOn2_Target_" + str(i) + ".jpg"
        result_image = "HandsOn2_Result_" + str(i) + ".jpg"
        
        # 要求 Rekognition 進行圖片比對
        rk_response = rk_client.compare_faces(
            TargetImage = {
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': target_image
                }
            },
            SourceImage = {
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': source_image
                }
            },
            SimilarityThreshold = 0
        )
        
        # 接下來要把 Rekognition 抓出來的 BoundingBox 畫到圖片上
        
        # 從 S3 把 Target 圖片抓來準備畫圖
        s3_response = s3_client.get_object(
            Bucket = bucket_name,
            Key = target_image
        )
        image_content = s3_response['Body'].read()
        image = Image.open(BytesIO(image_content))
        draw = ImageDraw.Draw(image)
        
        
        # 處理剛才 Rekognition 抓到的 BoundingBox
        # Rekognition 回傳的是 "左、上、寬、高" 相對於原本圖片的 "比例"
        # 畫圖需轉換為 "左上角、右下角" 的 "像素"
        position = []
        image_width, image_height = image.size
        for faceMatch in rk_response['FaceMatches']:
            if faceMatch['Similarity'] >= 90:
                box = faceMatch['Face']['BoundingBox']
                position = [
                    box['Left'] * image_width,
                    box['Top'] * image_height, 
                    (box['Left'] + box['Width']) * image_width,
                    (box['Top'] + box['Height']) * image_height
                ]
        
        # 畫出框框並存成圖片
        draw.rectangle(position, outline="red", width=2)
        modified_image = BytesIO()
        image.save(modified_image, format="JPEG")
        modified_image.seek(0)
        
        s3_client.put_object(Body=modified_image, Bucket=bucket_name, Key=result_image)# 實作 2. whereIsMyWife
import json
import boto3
from PIL import Image, ImageDraw
import PIL.Image
from io import BytesIO

s3_client = boto3.client('s3')
rk_client = boto3.client('rekognition')

def lambda_handler(event, context):
    
    # 需改為自己的 bucket_name
    bucket_name = "tsou-workshop"
    source_image = "HandsOn2_Sakura.jpg"
    
    for i in range(1, 7):
        
        target_image = "HandsOn2_Target_" + str(i) + ".jpg"
        result_image = "HandsOn2_Result_" + str(i) + ".jpg"
        
        # 要求 Rekognition 進行圖片比對
        rk_response = rk_client.compare_faces(
            TargetImage = {
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': target_image
                }
            },
            SourceImage = {
                'S3Object': {
                    'Bucket': bucket_name,
                    'Name': source_image
                }
            },
            SimilarityThreshold = 0
        )
        
        # 接下來要把 Rekognition 抓出來的 BoundingBox 畫到圖片上
        
        # 從 S3 把 Target 圖片抓來準備畫圖
        s3_response = s3_client.get_object(
            Bucket = bucket_name,
            Key = target_image
        )
        image_content = s3_response['Body'].read()
        image = Image.open(BytesIO(image_content))
        draw = ImageDraw.Draw(image)
        
        
        # 處理剛才 Rekognition 抓到的 BoundingBox
        # Rekognition 回傳的是 "左、上、寬、高" 相對於原本圖片的 "比例"
        # 畫圖需轉換為 "左上角、右下角" 的 "像素"
        position = []
        image_width, image_height = image.size
        for faceMatch in rk_response['FaceMatches']:
            if faceMatch['Similarity'] >= 90:
                box = faceMatch['Face']['BoundingBox']
                position = [
                    box['Left'] * image_width,
                    box['Top'] * image_height, 
                    (box['Left'] + box['Width']) * image_width,
                    (box['Top'] + box['Height']) * image_height
                ]
        
        # 畫出框框並存成圖片
        draw.rectangle(position, outline="red", width=2)
        modified_image = BytesIO()
        image.save(modified_image, format="JPEG")
        modified_image.seek(0)
        
        s3_client.put_object(Body=modified_image, Bucket=bucket_name, Key=result_image)