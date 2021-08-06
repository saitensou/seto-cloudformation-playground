# Deployment Steps

1. Go to the stack as not support deploy multiple stack at once
   `cd BootstrapStepStack`
1. packaging
   `aws cloudformation package --template-file template.yaml --s3-bucket seto-cloudformation-play --output-template-file ./finalStack.yaml`
1. verification (only upload the changeset but changes are not deployed)
   `aws cloudformation deploy --capabilities CAPABILITY_IAM --template-file ./finalStack.yaml --stack-name seto-test-stack --no-execute-changeset`
1. deployment
   `aws cloudformation deploy --capabilities CAPABILITY_IAM --template-file ./output/finalStack.yaml --stack-name seto-test-stack`
