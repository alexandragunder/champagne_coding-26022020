# champagne_coding-26022020
Champagne Coding with Redpill Linpro on February 26, 2020

## Set-up

To re-create the environment:
- Make sure ```conda``` is installed
- Option 1: ```conda env create --name champagne_coding -f environment.yml``` 
- Option 2: If that doesn't work, try ```conda create --name champagne_coding --file explicit_env.txt```

__NOTE:__ if this doesn't work and you're using Windows, you may have to install the Python packages as you go through the code

- ```conda activate champagne_coding```
- Start a jupyter notebook (```jupyter notebook```) 


# Simple git workflow

Initial checkout from server to local host

```
  git clone <url>
```

Pull changes from server to local host
```
  git pull
```

Commit changes *locally*
```
  git commit -a -m "Commit message"
```

Push committed changes to origin server
```
  git push
```

## Docker

If you have docker installed, you can test the code locally with:
```
docker build . -t champagne-coding
docker run -p 8080:8080  --volume="$PWD:/app" -it champagne-coding
```

The application is then available on http://0.0.0.0:8080/ in your web browser
