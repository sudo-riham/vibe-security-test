import json
import sys

try:
    with open('/workspace/zap-results.json') as f:
        data = json.load(f)
    alerts = data.get('site', [{}])[0].get('alerts', [])
    high = [a for a in alerts if a.get('riskcode') in ['3', '4']]
    print(len(high))
except Exception:
    print("0")
