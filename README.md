# PEPBS4

<details>
  <summary>Содержание</summary>
  <ul>
    <li>
      <a href="#описание">Описание</a>
      <ul>
        <li><a href="#-возможности">Возможности</a></li>
        <li><a href="#технологии">Технологии</a></li>
      </ul>
    </li>
    <li>
      <a href="#-начало-работы">Начало работы</a>
      <ul>
          <li><a href="#-зависимости">Зависимости</a></li>
          <li><a href="#установка">Установка</a></li>
      </ul>
    </li>
    <li>
      <a href="#-использование">Использование</a>
      <ul>
        <li><a href="#параметры-cli">Параметры CLI</a></li>
        <li><a href="#mode">Mode</a></li>
      </ul>
    </li>
    <li><a href="#автор-проекта-ilya-petrukhin">Автор проекта</a></li>
  </ul>
</details>

<a name="описание"></a>

### 🔥 Возможности

- Скачать документацию на текущую версию Python в формате `pdf-a4`
- Получить ссылки на документации последних версии Python
- Получить ссылки на статьи об изменениях в каждой версии Python
- Узнать общее количество документов PEP в каждом статусе.

### Технологии

[![BeautifulSoup][BS4-badge]][BS4-url]
[![Request-cache][Request-cache-badge]][Request-cache-url]

## ⚙ Начало Работы

Чтобы запустить локальную копию проекта, следуй инструкциям ниже.

### ⚠ Зависимости

- [Python 3.7+][Python-url]

### Установка

1. **Клонируй репозиторий**

    ```shell
    git clone https://github.com/tvules/PEPBS4.git
    cd PEPBS4
    ```

2. **Установи зависимости проекта**

    ```shell
    pip install -r requirements.txt
    ```

## 👀 Использование

```shell
python src/main.py <mode> <args>
```

### Параметры CLI

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

### Mode

- **download** - Скачать документацию последней версии Python.
- **latest-versions** - Получить ссылки на документации всех версий Python.
- **pep** - Узнать общее количество документов PEP в каждом статусе.
- **whats-new** - Получить ссылки на статьи об изменениях во всех версиях
  Python 3.

---

<h4 align="center">
Автор проекта: <a href="https://github.com/tvules">Ilya Petrukhin</a>
</h4>

<!-- MARKDOWN BADGES & URLs -->

[Python-url]: https://www.python.org/

[BS4-url]: https://beautiful-soup-4.readthedocs.io

[BS4-badge]: https://img.shields.io/badge/Beautifulsoup4-808080?style=for-the-badge

[Request-cache-url]: https://requests-cache.readthedocs.io

[Request-cache-badge]: https://img.shields.io/badge/Requests--Cache-5fb7ff?style=for-the-badge
