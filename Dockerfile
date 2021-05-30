FROM centos
COPY *  /Workspace/
RUN yum install python3 -y
RUN pip3 install scikit-learn
RUN pip3 install jupyter
RUN pip3 install pandas
RUN pip3 install joblib



