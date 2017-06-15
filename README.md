client to make requests against PAL. 

## Install guide
install python3. 
run
python3 setup.py install
run pal_client


### Example commands
Target is the url of the PAL RESTful API deployment. 
This could be 
```
http://localhost:5000, which the Client defaults to. 
```

```
pal_client download bucket key.log --target /tmp/file --target http://206.167.181.159:5000
pal_client upload bucket key-2.log --target /tmp/upload_file --target http://206.167.181.159:5000
pal_client symlink bucket key-3 --target bucket/key-2.log --target http://206.167.181.159:5000
```