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
You need to create an `.env` file. After that, you need to get access_token and client_id and insert it into variables in the `.env` file. 

Client_id is needed to work with the application. Access token is needed so that your application has access to your account and can publish messages in groups. 

An example of a token to insert into an environment variable:
```
access_token='vk1.b.sGHFgvhbjhbHJBJHjhHJNJnjk_nninnj_VGVVHGbmnwLKzmeZA7nG41EO-spYLQH_7o_-w9iC-O_uG_Guby4rlz7q1YCzFnJiVqsjdhbcsbdcbYBYbbjnBUBuyUvtvtuvVUBUBiJNIniijnnnKe2Lt9PP9TIPqRw_y1TrDwEhat1A'
```
An example of a client_id:
```
client_id=12345678
```
### How to get 
- [Sign up](https://id.vk.com/auth?app_id=7913379&v=1.58.6&redirect_uri=https%3A%2F%2Fvk.com%2Fjoin&uuid=2akhQyx0pHpNiIacgm2Z8&scheme=space_gray&action=eyJuYW1lIjoibm9fcGFzc3dvcmRfZmxvdyIsInBhcmFtcyI6eyJ0eXBlIjoic2lnbl91cCJ9fQ%3D%3D) and log in to your VK account;
- In order for comics to be successfully published on your community page, it must be [created](https://vk.com/groups?tab=admin).
- To post on the wall, you need a user access key. To get it, VKontakte wants an “app”. Create it on the Vkontakte page for developers. [Page for developers](https://vk.com/editapp?act=create). 
The application type should be set to `standalone`, which is an appropriate type for applications that simply run on a computer.
- Get the `client_id` of the created application. Click on the “Edit” button for the new application, you will see its `client_id` in the address bar.
- Follow the instructions on the [developer page](https://vk.com/dev/implicit_flow_user) to get accsess token.
- - Since you are using a `standalone` application, you should use Implicit Flow to get the user key
- - Remove the redirect_uri parameter from the key request
- - Specify the scope parameter separated by commas, like this: 'scope=photos,groups,wall'
## Run
To run the script, enter the command:
```
python publishing_a_comic_vk.py
```


