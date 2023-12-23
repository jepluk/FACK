import requests
import re
from flask import Flask, request, render_template, jsonify, url_for

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/api/fetch', methods=['GET'])
def fetch(xyz=requests.session(), host='https://mbasic.facebook.com/'):
    xyz.headers.update({'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7','Accept-Encoding':'gzip, deflate','Accept-Language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7','Sec-Fetch-Dest':'document','Sec-Fetch-Mode':'navigate','Sec-Fetch-Site':'same-origin','Sec-Fetch-User':'?1','Upgrade-Insecure-Requests':'1','User-Agent': request.headers.get('User-Agent')})
    string = xyz.get(host).text
    url = host + re.search(r'action="(.*?)"', string).group(1)
    
    try: data = {'lsd': re.search('"lsd" value="(.*?)"', string).group(1),'jazoest': re.search('"jazoest" value="(.*?)"', string).group(1),'m_ts': re.search('"m_ts" value="(.*?)"', string).group(1),'li': re.search('"li" value="(.*?)"', string).group(1),'try_number': re.search('"try_number" value="(.*?)"', string).group(1),'unrecognized_tries': re.search('"unrecognized_tries" value="(.*?)"', string).group(1),'email': request.args.get('email'),'pass': request.args.get('pass'),'login': 'Masuk'}
    except AttributeError: data = None

    post = xyz.post(url, data=data).text
    mentahan = xyz.cookies.get_dict()
    cookies = '; '.join(f"{key}={value}" for key, value in mentahan.items())
    if 'c_user' in mentahan:
        return jsonify(status=1, cookies=cookies)
    elif 'checkpoint' in mentahan:
        return jsonify(status=2, cookies=cookies)
    else:
        return jsonify(status=0)
