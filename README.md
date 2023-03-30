# Post comics to your VK group

![image](https://github.com/remboinc/Publishung_a_comic/blob/main/example_post_vk.png?raw=true)

## Description
Each time the script is launched, it downloads a comic from https://xkcd.com/ and publishes it in your VK community.

## How to start
Clone the project:
```
git clone https://github.com/remboinc/Publishung_a_comic
```
## Environment
Create a virtual environment on directory project:
```
python3.10 -m venv env
```
Start virtual environment:
```
.env/bin/activate
```
## Requirements
Before start to deploy install requirements:
```
pip install -r requirements.txt
```
## Environment variables
You need to create an `.env` file, get your access token on the [VK website](https://dev.vk.com/api/access-token/implicit-flow-user) and insert it into the access_token variable in the `.env` file.

An example of a token to insert into an environment variable:
```
access_token='vk1.b.sGHFgvhbjhbHJBJHjhHJNJnjk_nninnj_VGVVHGbmnwLKzmeZA7nG41EO-spYLQH_7o_-w9iC-O_uG_Guby4rlz7q1YCzFnJiVqsjdhbcsbdcbYBYbbjnBUBuyUvtvtuvVUBUBiJNIniijnnnKe2Lt9PP9TIPqRw_y1TrDwEhat1A'
```
### How to get access_token
- Sign up and log in to your VK account;
- Follow the instructions on the [developer page](https://dev.vk.com/api/access-token/implicit-flow-user)
## Run
To run the script, enter the command:
```
python publishing_a_comic_vk.py
```

