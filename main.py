import os
from collections import defaultdict
import logging

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('file_extensions.log'),
            logging.StreamHandler()
        ]
    )

def find_all_extensions(directory):
    extensions = defaultdict(int)

    for root, _, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            ext = ext.lower()  # приводим к нижнему регистру
            if ext:  # игнорируем файлы без расширения
                extensions[ext] += 1

    return dict(sorted(extensions.items(), key=lambda item: item[1], reverse=True))

def log_extensions(extensions):
    logging.info("Найденные расширения файлов:")
    for ext, count in extensions.items():
        logging.info(f"{ext}: {count} файлов")
    logging.info(f"Всего уникальных расширений: {len(extensions)}")

def main():
    setup_logging()
    directory = input("Введите путь к директории: ").strip()

    if not os.path.isdir(directory):
        logging.error("Указанная директория не существует!")
        return

    extensions = find_all_extensions(directory)
    log_extensions(extensions)

if __name__ == "__main__":
    main()
