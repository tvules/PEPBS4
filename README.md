# Python Docs Parser

## Возможности

- Скачать документацию на текущую версию Python в формате `pdf-a4`
- Получить ссылки на документации последних версии Python
- Получить ссылки на статьи об изменениях в каждой версии Python
- Узнать количество PEP в каждом статусе, а также общее количество PEP

## Основные технологии

- [Python 3.7](https://docs.python.org/3.7/)
- [Beautiful Soup 4](https://beautiful-soup-4.readthedocs.io/en/latest/)
- [Request-Cached](https://requests-cache.readthedocs.io/en/v0.9.7/)

## Инструкция

### Локальный запуск

Клонировать репозиторий

```bash
https://github.com/tvules/bs4_parser_pep.git
```

Установить зависимости

```bash
pip install -r requirements.txt
```

Выполнить

```bash
python src/main.py <mode> <args>
```

### Параметры командной строки

```bash
positional arguments:
  {download,latest-versions,pep,whats-new}
                        Режимы работы парсера

optional arguments:
  -h, --help            show this help message and exit
  -c, --clear-cache     Очистка кеша
  -o {pretty,file}, --output {pretty,file}
                        Дополнительные способы вывода данных
```

<h5 align="center">Автор проекта: <a href="https://github.com/tvules">Petrukhin Ilya</a></h5>
