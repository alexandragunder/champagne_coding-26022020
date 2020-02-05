# champagne_coding-26022020
Champagne Coding with Redpill Linpro on February 26, 2020

## Set-up

To re-create the environment:
- Make sure ```conda``` is installed
- ```conda create --name champagne_coding --file environment.txt``` OR ```conda create --name champagne_coding --file explicit_env.txt```
-- __NOTE:__ if this doesn't work and you're using Windows, you may have to install the Python packages as you go through the code
- ```conda activate champagne_coding```
- Start a jupyter notebook (```jupyter notebook```) 



## Docker

Running the code locally:

```
docker build . -t champ
docker run -p 8080:8080 champ
```
