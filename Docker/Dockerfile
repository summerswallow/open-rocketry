FROM jupyter/scipy-notebook
USER root
RUN conda install -c defaults qtconsole  pillow
RUN conda install plotly jupyter_contrib_nbextensions numpy-stl pythreejs
RUN apt update
RUN pip install python-jose s3contents boto3 snowflake-connector-python snowflake-sqlalchemy plotly_express 
RUN apt install git -y
RUN apt-get install software-properties-common -y
RUN add-apt-repository ppa:openscad/releases 
RUN apt install openscad -y
#COPY login.py /opt/conda/lib/python3.7/site-packages/notebook/auth/login.py
RUN mkdir /usr/share/notebook
RUN pip install solidpython viewscad
RUN pip install pydoc-markdown
RUN chown $NB_USER /usr/share/notebook
RUN mkdir /usr/local/share/jupyter
RUN chown $NB_USER /usr/local/share/jupyter
#RUN jupyter nbextension install  jupyterlab-datawidgets
#RUN npm config set strict-ssl false
#RUN npm install jupyter-threejs
#RUN jupyter nbextension install jupyter-threejs
#RUN jupyter lab build
RUN apt install emacs -y
RUN pip install viewscad
#COPY start-notebook.sh /usr/local/bin/
COPY openssl.cnf /etc/ssl/
USER $NB_USER
RUN touch .rnd
CMD ["start-notebook.sh", "--NotebookApp.base_url=/notebook/"]
# docker run -p8889:8888 -it -v/personal/open-rocketry-tools/:/home/jovyan/rocketry f6161bb35a03
