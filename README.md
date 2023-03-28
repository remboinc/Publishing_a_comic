# Post comics to your VK group
Each time the script is launched, it downloads a comic from https://xkcd.com/ and publishes it in your VK community
![image](https://github.com/remboinc/Publishung_a_comic/blob/main/example_post_vk.png?raw=true)
## How to start
Clone the project:
```
git clone https://github.com/remboinc/Publishung_a_comic
```
Create a virtual environment on directory project:
```
python3.10 -m venv env
```
Start virtual environment:
```
.env/bin/activate
```
Before start to deploy install requirements:
```
pip install -r requirements.txt
```
You need to create an `.env` file, get your API token on the [VK website](https://dev.vk.com/api/access-token/implicit-flow-user) and insert it into the access_token variable in the `.env` file.

To run the script, enter the command:
```
python publishing_a_comic_vk.py
```

