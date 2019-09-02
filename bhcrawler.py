#!/usr/bin/env python
# -*- coding: utf-8 -*-
# bhcrawler.py - Crawl all BlackHat briefings slides.
# Project Repos:    https://github.com/bertonhu/bhcrawler
# Author:           https://twitter.com/Berton_Hu
#                   https://bertonhu.com

import requests
import argparse
import json
import os


def crawler(args):
    if args.code:
        htmlcode = requests.get('https://www.blackhat.com/' + args.code + '/briefings/schedule/sessions.json')
        htmlcode.encoding = 'utf-8'
        json_dic = htmlcode.json()

        for item in json_dic['sessions']:
            slides = json_dic['sessions'][item]['bh_files']['slides']['url']
            whitepapers = json_dic['sessions'][item]['bh_files']['whitepaper']['url']
            source_code = json_dic['sessions'][item]['bh_files']['source_code']['url']
            try:
                fo = open('./' + args.code + '.txt', mode='a')
                if slides != "":
                    fo.write(slides.encode('utf-8').strip() + '\n')
                if whitepapers != "":
                    fo.write(whitepapers.encode('utf-8').strip() + '\n')
                if source_code != "":
                    fo.write(source_code.encode('utf-8').strip() + '\n')
            except:
                print 'Error'
        print 'BlackHat ' + args.code + ' briefings slides URL written to ' + args.code + '.txt!'
    else:
        print "Please input event code."


def main():
    parser = argparse.ArgumentParser(description='BlackHat Slides Crawler - Crawl all BlackHat briefings slides URL.')
    parser.add_argument('-code', help='BlackHat event code: us-18, eu-18, asia-18', required=True)
    args = parser.parse_args()
    crawler(args)


if __name__ == '__main__':
    main()
