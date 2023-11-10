# AWS_workshop

# Hands-on 1: Textbook Translate

### Step 1: Upload files in src to AWS S3

1. Search E3
2. Create a bucket
    - Bucket name should be unique
    - Choose **us-east-1** region
    - Select **create bucket**
3. Access bucket
4. Upload files

### Step 2: Code in Lambda

1. Search Lambda
2. Create function
    - Give a function name
    - Choose **python 3.11**
    - Select **********************create bucket**********************
3. Code in **lambda_function**
4. Press ************Deploy************
5. Press ********Test********
    - Give a event name

### Step 3: Add permissions

1. Select ****Configuration>Permission****
2. Press the **link** under role name access IAM
3. Click ******Add permissions > Attach Policies******
4. Select
    - [ ]  **AmazonS3FullAccess**
    - [ ]  **TranslateReadOnly**
    - [ ]  **AmazonTextractFullAccess**
5. Press **Add permission**
6. Successfully execute and ********************result.txt******************** is generate in S3 bucket

# Hands-on 2: Find Someone

### Step 1: Code in Lambda

(Same as the previous)

### Step 2: Add layers

1. Press **Layers**
2. Press **********************Add a layer**********************
    1. Select **Specify an ARN**
    2. Paste **arn:aws:lambda:us-east-1:770693421928:layer:Klayers-p311-Pillow:2**
        
        <aside>
        💡 [ARN reference](https://github.com/keithrozario/Klayers) (Remember to choose the match Runtime **version** and **region**)
        
        </aside>
        
    3. Press ************Verify************
    4. Press **Add**

### Step 3: Add permissions

1. Select ****Configuration>Permission****
2. Press the **link** under role name access IAM
3. Click ******Add permissions > Attach Policies******
4. Select
    - [ ]  **AmazonS3FullAccess**
    - [ ]  **AmazonRekognitionReadOnly**
5. Press **Add permission**

### Step 4: Fix Timeout

The origin timeout is 3 sec.

1. Select ****Configuration>General configuration****
2. Press ********Edit********
3. Edit timeout to 10 sec. and save
4. Successfully execute and 6 results are generate in S3 bucket