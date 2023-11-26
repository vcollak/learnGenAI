"""
Claude model calling Bedrock directly without the bedrock client 
"""


import boto3  # aws client for python
import json  # able to handle json


# Create a boto3 clinet by passing the right service
# To instantiate models, you need to use bedrock-runtime service
# Make sure the region matches your aws config
bedrock = boto3.client(service_name="bedrock-runtime", region_name="us-east-1")

# Claude prompts are structured with Human: and Assistant:. The
# Former is what we are asking the model to do. The latter is where the
# AI responds
prompt = (
    "\n\nHuman: In 100 words or less summarize the book 'Zero to One' \n\nAssistant:"
)

# Claude requires certain setting as parameters
body = json.dumps(
    {
        "prompt": prompt,
        "max_tokens_to_sample": 8191,
        "temperature": 0,
        "top_k": 250,
        "top_p": 0.9,
        "stop_sequences": [],
    }
)

# We're using the Claude AI model. AWS Bedrock has other
# models that you could pick
modelId = "anthropic.claude-v2"
accept = "application/json"
contentType = "application/json"

# Invoking the model will call the services and wait for a response.
response = bedrock.invoke_model(
    body=body, modelId=modelId, accept=accept, contentType=contentType
)

print("Raw response:")
print(response)


# We're just loading the response body
# just the body
print("-------")
print("Body:")
response_body = json.loads(response.get("body").read())
print(response_body)
