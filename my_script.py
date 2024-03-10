import urllib3

# Create an HTTPS connection pool with custom SSL/TLS settings
http = urllib3.PoolManager(ssl=urllib3.PoolManager().ssl_context)

# Make an HTTPS request
response = http.request('GET', 'https://example.com')

# Process the response as needed
print(response.status, response.data)