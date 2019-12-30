## Hello!!
# Flask-Prime 
Will give you an rest api for checking if an number is *Two sided prime number of not* in a form of bollean (True/False)

### Method

Use your *Host URL* like localhost , Public IP or DNS name and port 8000 where the function is executed with below api URL to get the result. 

/tsp/<your number>
Example:
``` 
example.com:8000/tsp/500
#will return 
	False
```
For a valid two sided Prime number 
```
example.com:8000/tsp/3797
#will give
	True
```


In addition to above root will return default instruction for execution
```
example.com:8000/

Hi, use /tsp/(your number) to check if it is a double sided prime number


```
