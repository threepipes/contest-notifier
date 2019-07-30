from pyquery import PyQuery as pq
import requests as req
import time
import json
import os
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("id", help="contest id")
args = parser.parse_args()


contst_number = args.id
url = f'https://codeforces.com/contest/{contst_number}/standings'
webhook_url = os.getenv('SLACK_WEBHOOK', '')


def check_testing_status():
    status = pq(url)('span.contest-status')
    status_text = pq(status).text().strip()
    print(status_text)
    return status_text == 'Final standings'


while not check_testing_status():
    time.sleep(60)

response = req.post(webhook_url, json.dumps({
    'text': f'Finish contest {contest_number} system testing.'
}))
print(response.text)
