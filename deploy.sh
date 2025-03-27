#!/bin/bash
set -e

echo "=== Aplicando configuração Terraform ==="
terraform init
terraform apply -auto-approve

echo "=== Exportando variáveis do Terraform para Ansible ==="
export ACR_LOGIN_SERVER=$(terraform output -raw acr_login_server)
export APP_URL=$(terraform output -raw app_url)

# Extrair webapp_name do app_url
export WEBAPP_NAME=$(echo $APP_URL | sed -e 's|https://||' -e 's|\.azurewebsites\.net||')

echo "=== Executando Ansible para build e deploy ==="
cd ansible
ansible-playbook playbook.yml -e "acr_login_server=$ACR_LOGIN_SERVER webapp_name=$WEBAPP_NAME"

echo "=== Implantação completa! ==="
echo "Acesse sua aplicação em: $APP_URL"
