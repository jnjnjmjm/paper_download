# thesis_download_script
一个自动下载论文的脚本。通过谷歌学术获取pdf链接，谷歌学术找不着pdf的就找不着。

```python
pip install requests
pip install bs4
python ./main.py Path
```
其中Path替换为txt文件的路径。

txt文件应该包含需要下载的论文的题目，以回车分隔。和test.txt类似。

右键你的txt文件，复制文件地址，将他直接粘贴作为参数。

将代理服务开启到7890端口，或在代码中修改请求的代理部分。


A script that automatically download a batch of thesis.

```python
pip install requests
pip install bs4
python ./main.py Path
```
 
Path should be inplaced by path of txt file.

The txt file should contains title of thesis that you want to download, seperated with break. Just like test.txt.

When your txt file is ready, right-click the file and copy file path, then directly paste it into the command line as the argument.

Open your proxy service at port 7890, or edit the code to fit your environment.