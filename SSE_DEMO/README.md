SSE（Server-Sent Events）是一种基于 HTTP 协议的技术，用于实现服务器主动向客户端推送数据。它利用了 HTTP 的长连接特性，在客户端与服务器之间建立一条持久化连接，并通过这条连接实现服务器向客户端的实时数据推送 ‌
SSE 的响应头中需要设置 Content-Type: text/event-stream、Cache-Control: no-cache、Connection: keep-alive 和 Access-Control-Allow-Origin: \*等 ‌

前端实现 SSE 的方式主要有两种：使用 EventSource 对象和通过 fetch API。使用 EventSource 对象可以建立与服务器的连接，监听服务器推送的事件，并在接收到数据后进行处理。这种方式支持自动重连和跨域问题处理，但不支持自定义请求头 ‌。通过 fetch API 实现则需要手动处理流数据和错误处理，但可以支持自定义请求头和更复杂的操作。
