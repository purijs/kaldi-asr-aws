import boto3
import requests
import json
from botocore.exceptions import ClientError
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    hasError=0
    audioLength=0
    
    # YOUR AWS API INVOKE URL
    awsApiUrl = '' 
    
    # YOUR AWS API KEY GOES INTO 'x-api-key'
    awsApiHeaders = {'content-type': 'application/json', 'x-api-key':''}
    customerFiles=[]

    if request.method == 'POST':
        
        # Remove dots(.) from filenames
        customerKey=request.form['email'].split('@')[0].replace('.','_')

        # YOUR AWS IAM ACCESS KEY AND SECRET, GET IT FROM THE IAM CONSOLE
        s3_client = boto3.client('s3', aws_access_key_id='', aws_secret_access_key='')

        data_files = request.files.getlist('file')

        for data_file in data_files:

            file_contents = data_file.read()

            try:
                
                # Remove dots(.) from filenames
                data_file.filename=str(data_file.filename).replace(' ','')
                customerFiles.append(data_file.filename)
                
                # To identify a user's file, append email to filename with a fixed seperator
                filename=customerKey+'_sep_'+data_file.filename

                # ENTER YOUR BUCKET NAME
                s3_client.put_object(Body=file_contents, Bucket='', Key='incoming/'+filename)

            except ClientError as e:
                logging.error(e)
                hasError=1
        
        if hasError == 0:
            
            awsApiBody={'customerKey':customerKey, 'files':customerFiles}
            callAPI=requests.post(awsApiUrl, data=json.dumps(awsApiBody), headers=awsApiHeaders)
        
    return render_template('index.html', error=hasError)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port='8080',
        debug=False
    )

