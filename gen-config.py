import json
import os

templates_dir = "./templates"
generate_dir = "./server-config"

with open("deploy.config.json") as fj:
    deploy_config = json.load(fj)

python_environment_code = ("source /home/<web-name>/server-config/linux_install_python.sh") if (
    deploy_config.get("python-version").find(".") != -1) else (
    "sudo virtualenv -p python3 --no-site-packages --download /home/.pyenvs/<web-name>")

if not os.path.exists(generate_dir):
    os.mkdir(generate_dir)
templates = [f for f in os.listdir(templates_dir)]


def replace_template(temp_file, save_path):
    with open(os.path.join(templates_dir, temp_file), "r", encoding='utf-8') as rfp:
        text = rfp.read()
        text = text.replace("<create_python_environment_code>", python_environment_code)
        for K, V in deploy_config.items():
            text = text.replace("<" + K + ">", V)
        with open(save_path, "w", encoding='utf-8') as wfp:
            wfp.write(text)


for template in templates:
    if template == "deploy.sh":
        replace_template(template, os.path.join(template))
    elif not (template == "linux_install_python.sh" and deploy_config.get("python-version").find(".") == -1):
        replace_template(template, os.path.join(generate_dir, template))
