Source used: https://aws.amazon.com/what-is/restful-api/

Question 1. REST APIs are scalable because they are stateless and follow a client-server architecture. The server doesn't store client session information, so any request can be handles by any server instance. As a reuslt, systems can add more servers to handle higher traffic. They also support caching and layered systems, which improves performances and reduces server load.


Question 2. In our mail server, the resources are email messages. Can be created, retrieved, listed, or deleted through REST endpoints.

Question 3. We use GET, POST, DELTE, but not PUT. PUT is used to update an existing resource, so we extand the server by adding another endpoint (PUT /mail/id) to allow someone to edit the contents of the email, like the recipient or the message. 

Question 4. API keys are used to authenticate and identify applications that access an API. Allow providers to track usage, prevent abuse, and control access to services. 