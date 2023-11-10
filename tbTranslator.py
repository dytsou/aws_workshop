import json
import boto3

s3_client = boto3.client('s3')
tt_client = boto3.client('textract')
ts_client = boto3.client('translate')

def lambda_handler(event, context):
    
    # 需改為自己的 bucket_name 和 file_name
    bucket_name = "tsou-workshop"
    file_name = "HandsOn1_os.png"
    
    result = ""
    result_file_name = 'result.txt'
    
    # 要求 textract 偵測圖片中的文字
    tt_response = tt_client.detect_document_text(
        Document = { 
          'S3Object': {
                'Bucket': bucket_name,
                'Name': file_name
            }
      }
    )
    
    # 處理 textract 回傳的內容
    for item in tt_response['Blocks']:
        if item['BlockType'] == 'LINE':
            result += item['Text'] + ' '
    print('\n\n---文字偵測結果---\n' + result)
    
    # 要求 translate 翻譯文字
    ts_response = ts_client.translate_text(
        Text = result,
        SourceLanguageCode = 'en',
        TargetLanguageCode = 'zh-TW'
    )
    
    # 處理 Translate 回傳結果
    result += ts_response['TranslatedText']
    print('\n\n---文字翻譯結果---\n' + ts_response['TranslatedText'])
    
    # 將結果以文檔形式存入 s3
    s3_client.put_object(
        Body = result,
        Bucket = bucket_name,
        Key = result_file_name,
        ContentType=' text/plain;charset=utf-8'
    )