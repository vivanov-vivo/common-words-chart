## Python Most-Common-Word-Counter Application

A Python application that runs in a containerized Docker environment. Upon receiving a GET request along with a set of environmental variables, it returns a list of the most common words in a set of text files in JSON format.

### Contents
- Dockerfile
- Python program
- Directory with .txt test files
- Kubernetes yaml file

### Prerequisites
To complete this tutorial, you will need the following:

- Free Docker Account
        You can [sign-up](https://hub.docker.com/) for a free Docker account and receive free unlimited public repositories 
- Docker [intsalled and running locally](https://docs.docker.com/desktop/)
- [kubectl installed](https://kubernetes.io/docs/tasks/tools/)
- Local Kubernetes. For example, [minikube](https://minikube.sigs.k8s.io/docs/start/)
- [Minikube](https://minikube.sigs.k8s.io/docs/handbook/registry/) and [Docker](https://www.docker.com/blog/how-to-use-your-own-registry-2/) registries configuration 

### How it works
The Dockerfile creates an image based on the Python 3.9 slim image, which will run our script.py application. Inside a container, which will be created based on the image, `/app` will be the working directory of the code. This directory will contain the copied test files with which the code executes: `/app/text_files/`. Two environmental variables will be used to run the script:
- FILE_PATHS
- NUMOFWORDS
These variables will indicate the .txt files we want to include in our word counting as well as the number of words to display in the result. **Note:** The files on which the code executes don't have to be exclusively inside `/app/text_files/`. They can exist elsewhere on the container. As long as you know the path and specify it when running a container, the code will include these files in its execution.

### How to run in Docker
1. After downloading and extracting the contents of the .zip file (or pulling the repository), change directory to common-words-chart
2. run the following command:
```
$ docker build -t <image-name> .
```
Replace `<image-name>` with the name of your choice, for example common-words-img. If the system prompts you with an error requiring you to run the command with sudo privileges, enter:
```
$ sudo !!
```
This will rerun the `docker build` command with sudo privileges.

3. Once the building is complete, run:
```
$ docker run -p 8080:8080 -e FILE_PATHS="/file/path/one,/file/path/two<,/file/path/two, etc>" -e NUMOFWORDS=<number> <image-name>
```
Replace `/file/path/one` and `/file/path/two` with the files you wish to use (you can include more than two), as well as `<number>` with an integer representing the number of words you wish to display. 
**Note:** The paths to the files *must* be separated by a comma ','. Replace `<image-name>` with the name you provided in the `docker build` command in the previous step.

4. Connect to one of the displayed addresses you see on the screen from the end of the previous step (e.g., 127.0.0.1:8080). The result should be displayed in your browser in JSON format with the maximum occurring word and the value of its occurrences.

### How to deploy in Kubernetes
1. Change directory to common-words-chart directory

2. Run the following command:
```
$ kubectl apply -f app_folder_script.yaml
```
3. Check that all new resources are running:
```
$ kubectl get all -n common-words-namespace
```
4. Get url to access application:
```
$ minikube service common-words-service -n common-words-namespace --url
```
5. Try to open it in your browser (ensure there is no proxy set).
