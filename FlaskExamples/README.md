# Flask Examples



## Preparation

1. Install `Miniconda`

   To download and install, see [Docs>>Miniconnda]( https://docs.conda.io/en/latest/miniconda.html)

2. Setup  `ENVIRONMENT`

   >Computer >> Advanced Settings >> Environment Variables
   >
   >```shell
   >CONDA_HOME = <CONDA_HOME>
   >```
   >
   >>For example, you may install conda at this foler`D:\Workspace\Conda`
   >>
   >>Then set `CONDA_HOME` to `D:\Workspace\Conda`

3. Create `env`

   ```hell
   conda env list
   ```

   ```shell
   conda create -n <ENV_NAME> python=<VER>
   ```

   >**Create `flask` with python version `3.8` **
   >
   >```shell
   >conda create -n flask python=3.8
   >```

4. Install packages

   ```shell
   conda install <PACKAGE_NAME> -n <ENV_NAME> -y
   ```

   >The core package is `flask`, the extra packages are:  `flask-httpauth`, `flask-restful`, etc.
   >
   >**Package usage**
   >
   >```python
   >from flask import Flask
   >from flask_httpauth import HTTPBasicAuth
   >from flask_restful import Api
   >```

## Scripts

1. Activate `Conda`

   ```shell
   @CALL "%CONDA_HOME%\condabin\conda.bat" activate flask
   @echo %~dp0
   @cmd
   ```

2. Run Server

   ```shell
   cd <DIR>
   conda activate <ENV>
   python exmple.py
   ```

   

3. Test with [CURL](https://curl.haxx.se/)

   - GET 

     ```shell
     curl -i http://127.0.0.1:8000/tasks
     ```

   - POST

     ```shell
     curl -i -H "Content-Type: application/json" -X POST -d '{"title":"Read a book"}' http://localhost:8000/tasks
     ```

4. Test with a WebBrowser (**recomended**)

    Install extension Postman` or any tools you like.
