import csv
import datetime as dt

from .constants import BASE_DIR, DATETIME_FORMAT


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = {}
        self.results_dir = BASE_DIR / 'results'
        self.results_dir.mkdir(exist_ok=True)

    def process_item(self, item, spider):
        self.results[item['status']] = self.results.get(item['status'], 0) + 1
        return item

    def close_spider(self, spider):
        self.results['Total'] = sum(self.results.values())
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_path = f'{self.results_dir}/status_summary_{now_formatted}.csv'
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Статус', 'Количество'])
            writer.writerows(self.results.items())
