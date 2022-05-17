# -*- coding: utf-8 -*-

from cache import LRUCache

if __name__ == '__main__':

    cache = LRUCache(3)
    cache.set('Kusova', 'Natali')
    cache.set('Jesse', 'Pinkman')
    cache.set('Walter', 'White')
    cache.set('Jesse', 'James')
    cache.set('Kusova', 'Ku')

    print('Kusova: ' + cache.get('Kusova'))  # вернёт 'Ku'

    cache.rem('Walter')
    print('Walter: ' + cache.get('Walter'))  # вернёт 'not found'