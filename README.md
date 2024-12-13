# Установка
1. клонировать репозиторий
```
git clone https://github.com/assami1337/OTRPO_lab10.git && cd OTRPO_lab10
```
2. подготовить venv
```
python3 -m venv venv
```
```
source venv/bin/activate #linux/macos
```
```
./venv/Scripts/activate #windows
```
3. установить зависимости
```
pip install requirements.txt
```
# Запуск
1. установите переменные окружения `EXPORTER_HOST` и `EXPORTER_PORT`
```
export EXPORTER_HOST=
```
```
export EXPORTER_PORT=
```
значения по умолчанию 0.0.0.0 и 8000
2. запустите `exporter.py`
```
python exporter.py
```
3. запустите `prometheus`
```
prometheus --config.file=prometheus.yml
```
# Запросы PromQL
Использование процессоров
```
cpu_usage
```
Память всего и используется
```
memory_total
```
```
memory_used
```
Диск всего и используется
```
disk_total
```
```
disk_used
```
