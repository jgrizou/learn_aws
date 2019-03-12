https://github.com/lambci/docker-lambda

# Python 3.7 requires the handler be given explicitly

# run to inspect output
docker run --rm -v "$PWD":/var/task lambci/lambda:python3.7 lambda_function.lambda_handler

# run with name to keep iterating
docker run --name aname -v "$PWD":/var/task lambci/lambda:python3.7 lambda_function.lambda_handler

# run a docker again
docker start -i aname


# install dependencies locally for lambda system target

docker run --name test2 -v "$PWD":/var/task -it lambci/lambda:build-python3.7 bash /var/task/install.sh


# zip it

cat .lambdaignore | xargs zip -9qyr lambda.zip . -x


cat .lambdaignore | xargs zip -9 -yqr ../function.zip . -x
