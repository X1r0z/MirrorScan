# -*- coding:utf-8 -*-

import leancloud

def reportformat(result):
    repos = dict()
    for item in result:
        if item.get('target') in repos:
            if item.get('level') in repos[item.get('target')]:
                if item.get('name') in repos[item.get('target')][item.get('level')]:
                    repos[item.get('target')][item.get('level')][item.get('name')].append(item.get('body'))
                else:
                    repos[item.get('target')][item.get('level')][item.get('name')] = [item.get('body')]
            else:
                repos[item.get('target')][item.get('level')] = dict()
                repos[item.get('target')][item.get('level')][item.get('name')] = [item.get('body')]
        else:
            repos[item.get('target')] = dict()
            repos[item.get('target')][item.get('level')] = dict()
            repos[item.get('target')][item.get('level')][item.get('name')] = [item.get('body')]
    return repos

def getpage(query):
    totalPage = query.count()
    skipPage = 10
    perPage = totalPage / skipPage
    if perPage * skipPage != totalPage:
        perPage += 1
    return perPage, skipPage

def getdata(name, per, **kwargs):
    result = list()
    skipPage = 100
    skip = 0
    for _ in range(per):
        query = leancloud.Query(name)
        for k, v in kwargs.items():
            if isinstance(v, list):
                query.contained_in(k, v)
            else:
                query.equal_to(k, v)
        query.skip(skip)
        query.limit(skipPage)
        result += query.find()
        skip += skipPage
    return result