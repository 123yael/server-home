# example/views.py
from datetime import datetime
import platform
from django.db import connection

print(platform.node())

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel!</h1>
            <p>The current time is { now }.</p>
        </body>
    </html>
    '''
    # raw_query = "SELECT * FROM category"
    # cursor = connection.cursor()
    # cursor.execute(raw_query)
    # cursor.fetchall()

    try:
        raw_query = "SELECT * FROM category"
        with connection.cursor() as cursor:
            cursor.execute(raw_query)
            results = cursor.fetchall()
    except Exception as e:
        print(f"Error executing SQL query: {e}")
    return HttpResponse(results[0][1])


def name(request):
    return HttpResponse(platform.node())