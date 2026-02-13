# Ansible-Practice

Репозиторий содержит решение практического задания по настройке Nginx (статические файлы, балансировка Round-Robin) с использованием Ansible и кастомного Python-модуля.

## Структура проекта
* `library/nginx_port.py` — кастомный Ansible-модуль для генерации конфига Nginx.
* `inventory/hosts.ini` — описание хостов (rrobin, web1, web2).
* `playbook.yml` — основной сценарий развертывания.
* `templates` - конфиги для проксирования на сервера web1 и web2 + кастомные страницы и видимые файлы
## Что реализовано

### 1. Раздача статики (Задание №1)
На сервере настроена раздача файлов через директиву `autoindex on`.
* **URL:** `http://<IP_host>/files`
* **Путь на сервере:** `/var/www/my_files/`

### 2. Кастомный модуль (Задание №2)
Написан модуль `nginx_port`, который принимает параметры `port` и `dest`. 
Модуль программно генерирует конфигурационный файл Nginx. В рамках демонстрации модуль создает дополнительный конфиг на порту **8081**.
```yaml
- nginx_port:
    port: 8081
    dest: /etc/nginx/http.d/custom_mod.conf
```


## Скрины рабочего сайта
**web1**

<img width="363" height="68" alt="image" src="https://github.com/user-attachments/assets/ac942afc-e061-474e-afad-ad90acb40a13" />

**web2**

<img width="337" height="76" alt="image" src="https://github.com/user-attachments/assets/f26e424b-3ed6-45ce-9d97-c4a20bb6dccf" />

**/files**

<img width="592" height="202" alt="image" src="https://github.com/user-attachments/assets/7f369f83-2a10-4d1c-ba17-68e038f4c177" />


# **Запуск**
1. `git clone https://github.com/HAigiz/Ansible-Practice.git`
2. `docker compose up --build -d`
3. `ansible-playbook -i inventory/hosts.ini playbook.yml`
4. В поисковой строке вводим <адрес_хоста:8080> вас перекинет на один из двух серверов `web1` или `web2` и по пути <адрес_хоста:8080/files> откроется список файлов, которые подтягиваются из директории `my_files`
