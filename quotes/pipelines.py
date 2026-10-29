# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class QuotesPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        text = adapter.get('text')
        if text:
            # Strip the curly quote marks the site wraps around each quote
            adapter['text'] = text.strip().strip('“”')
        return item
