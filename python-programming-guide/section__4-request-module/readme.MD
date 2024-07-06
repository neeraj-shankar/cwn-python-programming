## HTTP Requests Module

### What are headers in a request
- HTTP headers are additional pieces of information sent along with an HTTP request or response.
- They provide metadata about the message being sent and are used to convey various details that are not part of the main content.
- Headers are comprised of key-value pairs, where the key represents the header name and the value represents the corresponding information.

### Different Types of Headers

1. Content-Type: Specifies the media type of the message body (e.g., text/html, application/json).
2. Content-Length: Indicates the size of the message body in octets (bytes).
3. User-Agent: Identifies the client making the request (e.g., web browser, crawler).
4. Accept: Specifies the media types that are acceptable for the response.
5. Authorization: Provides authentication credentials for accessing protected resources.
6. Cache-Control: Directives for caching mechanisms in both requests and responses.
7. Cookie: Contains HTTP cookies previously sent by the server with Set-Cookie.
8. Date: Indicates the date and time at which the message was originated.
9. Host: Specifies the domain name of the server (e.g., example.com).
10. Referer: Indicates the address of the previous web page from which a link to the currently requested page was followed.
11. Server: Contains information about the software used by the origin server.
12. Connection: Controls whether the network connection stays open after the current transaction finishes.
13. Content-Disposition: Specifies presentation information for the recipient (e.g., inline, attachment).
14. ETag: An identifier for a specific version of a resource.
15. Location: Indicates the URL to which a client should be redirected.
16. Retry-After: Informs the client how long to wait before making a new request.


### Advanced- Session Objects
- The Session object allows you to persist certain parameters across requests.
- It also persists cookies across all requests made from the Session instance, and will use urllib3’s connection pooling.
- So if you’re making several requests to the same host, the underlying TCP connection will be reused, which can result in a significant performance increase
- A Session object has all the methods of the main Requests API.



