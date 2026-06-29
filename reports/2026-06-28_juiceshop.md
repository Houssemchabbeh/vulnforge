# VulnForge Scan Report — JUICESHOP (2026-06-28)

## Summary

| Severity | Count | Score |
|----------|-------|-------|
| Critical | 0 | 0 |
| High | 0 | 0 |
| Medium | 10 | 40 |
| Low | 19 | 19 |
| Info | 11 | 0 |
| **Total** | **40** | **59** |

**Risk Score: 59** 🟡

---

## Findings

### [Medium] Content Security Policy (CSP) Header Not Set
**Source:** ZAP  
**URL:** http://juiceshop:3000  
**CWE:** CWE-693  

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

**Solution:** Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

---

### [Medium] Content Security Policy (CSP) Header Not Set
**Source:** ZAP  
**URL:** http://juiceshop:3000/  
**CWE:** CWE-693  

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

**Solution:** Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

---

### [Medium] Content Security Policy (CSP) Header Not Set
**Source:** ZAP  
**URL:** http://juiceshop:3000/ftp  
**CWE:** CWE-693  

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

**Solution:** Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

---

### [Medium] Content Security Policy (CSP) Header Not Set
**Source:** ZAP  
**URL:** http://juiceshop:3000/ftp/eastere.gg  
**CWE:** CWE-693  

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

**Solution:** Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

---

### [Medium] Content Security Policy (CSP) Header Not Set
**Source:** ZAP  
**URL:** http://juiceshop:3000/sitemap.xml  
**CWE:** CWE-693  

Content Security Policy (CSP) is an added layer of security that helps to detect and mitigate certain types of attacks, including Cross Site Scripting (XSS) and data injection attacks. These attacks are used for everything from data theft to site defacement or distribution of malware. CSP provides a set of standard HTTP headers that allow website owners to declare approved sources of content that browsers should be allowed to load on that page — covered types are JavaScript, CSS, HTML frames, fonts, images and embeddable objects such as Java applets, ActiveX, audio and video files.

**Solution:** Ensure that your web server, application server, load balancer, etc. is configured to set the Content-Security-Policy header.

---

### [Medium] Cross-Domain Misconfiguration
**Source:** ZAP  
**URL:** http://juiceshop:3000  
**CWE:** CWE-264  

Web browser data loading may be possible, due to a Cross Origin Resource Sharing (CORS) misconfiguration on the web server.

**Solution:** Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance).Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive set of domains, or remove all CORS headers entirely, to allow the web browser to enforce the Same Origin Policy (SOP) in a more restrictive manner.

**Evidence:** `Access-Control-Allow-Origin: *`

---

### [Medium] Cross-Domain Misconfiguration
**Source:** ZAP  
**URL:** http://juiceshop:3000/assets/public/favicon_js.ico  
**CWE:** CWE-264  

Web browser data loading may be possible, due to a Cross Origin Resource Sharing (CORS) misconfiguration on the web server.

**Solution:** Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance).Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive set of domains, or remove all CORS headers entirely, to allow the web browser to enforce the Same Origin Policy (SOP) in a more restrictive manner.

**Evidence:** `Access-Control-Allow-Origin: *`

---

### [Medium] Cross-Domain Misconfiguration
**Source:** ZAP  
**URL:** http://juiceshop:3000/chunk-VS3A3LTT.js  
**CWE:** CWE-264  

Web browser data loading may be possible, due to a Cross Origin Resource Sharing (CORS) misconfiguration on the web server.

**Solution:** Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance).Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive set of domains, or remove all CORS headers entirely, to allow the web browser to enforce the Same Origin Policy (SOP) in a more restrictive manner.

**Evidence:** `Access-Control-Allow-Origin: *`

---

### [Medium] Cross-Domain Misconfiguration
**Source:** ZAP  
**URL:** http://juiceshop:3000/robots.txt  
**CWE:** CWE-264  

Web browser data loading may be possible, due to a Cross Origin Resource Sharing (CORS) misconfiguration on the web server.

**Solution:** Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance).Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive set of domains, or remove all CORS headers entirely, to allow the web browser to enforce the Same Origin Policy (SOP) in a more restrictive manner.

**Evidence:** `Access-Control-Allow-Origin: *`

---

### [Medium] Cross-Domain Misconfiguration
**Source:** ZAP  
**URL:** http://juiceshop:3000/sitemap.xml  
**CWE:** CWE-264  

Web browser data loading may be possible, due to a Cross Origin Resource Sharing (CORS) misconfiguration on the web server.

**Solution:** Ensure that sensitive data is not available in an unauthenticated manner (using IP address white-listing, for instance).Configure the "Access-Control-Allow-Origin" HTTP header to a more restrictive set of domains, or remove all CORS headers entirely, to allow the web browser to enforce the Same Origin Policy (SOP) in a more restrictive manner.

**Evidence:** `Access-Control-Allow-Origin: *`

---

### [Low] Cross-Origin-Embedder-Policy Header Missing or Invalid
**Source:** ZAP  
**URL:** http://juiceshop:3000  
**CWE:** CWE-693  

Cross-Origin-Embedder-Policy header is a response header that prevents a document from loading any cross-origin resources that don't explicitly grant the document permission (using CORP or CORS).

**Solution:** Ensure that the application/web server sets the Cross-Origin-Embedder-Policy header appropriately, and that it sets the Cross-Origin-Embedder-Policy header to 'require-corp' for documents.If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Embedder-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-embedder-policy).

---

### [Low] Cross-Origin-Embedder-Policy Header Missing or Invalid
**Source:** ZAP  
**URL:** http://juiceshop:3000/  
**CWE:** CWE-693  

Cross-Origin-Embedder-Policy header is a response header that prevents a document from loading any cross-origin resources that don't explicitly grant the document permission (using CORP or CORS).

**Solution:** Ensure that the application/web server sets the Cross-Origin-Embedder-Policy header appropriately, and that it sets the Cross-Origin-Embedder-Policy header to 'require-corp' for documents.If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Embedder-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-embedder-policy).

---

### [Low] Cross-Origin-Embedder-Policy Header Missing or Invalid
**Source:** ZAP  
**URL:** http://juiceshop:3000/ftp  
**CWE:** CWE-693  

Cross-Origin-Embedder-Policy header is a response header that prevents a document from loading any cross-origin resources that don't explicitly grant the document permission (using CORP or CORS).

**Solution:** Ensure that the application/web server sets the Cross-Origin-Embedder-Policy header appropriately, and that it sets the Cross-Origin-Embedder-Policy header to 'require-corp' for documents.If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Embedder-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-embedder-policy).

---

### [Low] Cross-Origin-Embedder-Policy Header Missing or Invalid
**Source:** ZAP  
**URL:** http://juiceshop:3000/juice-shop/build/routes/fileServer.js:53:13  
**CWE:** CWE-693  

Cross-Origin-Embedder-Policy header is a response header that prevents a document from loading any cross-origin resources that don't explicitly grant the document permission (using CORP or CORS).

**Solution:** Ensure that the application/web server sets the Cross-Origin-Embedder-Policy header appropriately, and that it sets the Cross-Origin-Embedder-Policy header to 'require-corp' for documents.If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Embedder-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-embedder-policy).

---

### [Low] Cross-Origin-Embedder-Policy Header Missing or Invalid
**Source:** ZAP  
**URL:** http://juiceshop:3000/sitemap.xml  
**CWE:** CWE-693  

Cross-Origin-Embedder-Policy header is a response header that prevents a document from loading any cross-origin resources that don't explicitly grant the document permission (using CORP or CORS).

**Solution:** Ensure that the application/web server sets the Cross-Origin-Embedder-Policy header appropriately, and that it sets the Cross-Origin-Embedder-Policy header to 'require-corp' for documents.If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Embedder-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-embedder-policy).

---

### [Low] Cross-Origin-Opener-Policy Header Missing or Invalid
**Source:** ZAP  
**URL:** http://juiceshop:3000  
**CWE:** CWE-693  

Cross-Origin-Opener-Policy header is a response header that allows a site to control if others included documents share the same browsing context. Sharing the same browsing context with untrusted documents might lead to data leak.

**Solution:** Ensure that the application/web server sets the Cross-Origin-Opener-Policy header appropriately, and that it sets the Cross-Origin-Opener-Policy header to 'same-origin' for documents.'same-origin-allow-popups' is considered as less secured and should be avoided.If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Opener-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-opener-policy).

---

### [Low] Cross-Origin-Opener-Policy Header Missing or Invalid
**Source:** ZAP  
**URL:** http://juiceshop:3000/  
**CWE:** CWE-693  

Cross-Origin-Opener-Policy header is a response header that allows a site to control if others included documents share the same browsing context. Sharing the same browsing context with untrusted documents might lead to data leak.

**Solution:** Ensure that the application/web server sets the Cross-Origin-Opener-Policy header appropriately, and that it sets the Cross-Origin-Opener-Policy header to 'same-origin' for documents.'same-origin-allow-popups' is considered as less secured and should be avoided.If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Opener-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-opener-policy).

---

### [Low] Cross-Origin-Opener-Policy Header Missing or Invalid
**Source:** ZAP  
**URL:** http://juiceshop:3000/ftp  
**CWE:** CWE-693  

Cross-Origin-Opener-Policy header is a response header that allows a site to control if others included documents share the same browsing context. Sharing the same browsing context with untrusted documents might lead to data leak.

**Solution:** Ensure that the application/web server sets the Cross-Origin-Opener-Policy header appropriately, and that it sets the Cross-Origin-Opener-Policy header to 'same-origin' for documents.'same-origin-allow-popups' is considered as less secured and should be avoided.If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Opener-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-opener-policy).

---

### [Low] Cross-Origin-Opener-Policy Header Missing or Invalid
**Source:** ZAP  
**URL:** http://juiceshop:3000/juice-shop/build/routes/fileServer.js:53:13  
**CWE:** CWE-693  

Cross-Origin-Opener-Policy header is a response header that allows a site to control if others included documents share the same browsing context. Sharing the same browsing context with untrusted documents might lead to data leak.

**Solution:** Ensure that the application/web server sets the Cross-Origin-Opener-Policy header appropriately, and that it sets the Cross-Origin-Opener-Policy header to 'same-origin' for documents.'same-origin-allow-popups' is considered as less secured and should be avoided.If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Opener-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-opener-policy).

---

### [Low] Cross-Origin-Opener-Policy Header Missing or Invalid
**Source:** ZAP  
**URL:** http://juiceshop:3000/sitemap.xml  
**CWE:** CWE-693  

Cross-Origin-Opener-Policy header is a response header that allows a site to control if others included documents share the same browsing context. Sharing the same browsing context with untrusted documents might lead to data leak.

**Solution:** Ensure that the application/web server sets the Cross-Origin-Opener-Policy header appropriately, and that it sets the Cross-Origin-Opener-Policy header to 'same-origin' for documents.'same-origin-allow-popups' is considered as less secured and should be avoided.If possible, ensure that the end user uses a standards-compliant and modern web browser that supports the Cross-Origin-Opener-Policy header (https://caniuse.com/mdn-http_headers_cross-origin-opener-policy).

---

### [Low] Dangerous JS Functions
**Source:** ZAP  
**URL:** http://juiceshop:3000/main.js  
**CWE:** CWE-749  

A dangerous JS function seems to be in use that would leave the site vulnerable.

**Solution:** See the references for security advice on the use of these functions.

**Evidence:** `bypassSecurityTrustHtml(`

---

### [Low] Deprecated Feature Policy Header Set
**Source:** ZAP  
**URL:** http://juiceshop:3000  
**CWE:** CWE-16  

The header has now been renamed to Permissions-Policy.

**Solution:** Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header instead of the Feature-Policy header.

**Evidence:** `Feature-Policy`

---

### [Low] Deprecated Feature Policy Header Set
**Source:** ZAP  
**URL:** http://juiceshop:3000/chunk-5K74DZ2F.js  
**CWE:** CWE-16  

The header has now been renamed to Permissions-Policy.

**Solution:** Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header instead of the Feature-Policy header.

**Evidence:** `Feature-Policy`

---

### [Low] Deprecated Feature Policy Header Set
**Source:** ZAP  
**URL:** http://juiceshop:3000/chunk-PX7UKXVL.js  
**CWE:** CWE-16  

The header has now been renamed to Permissions-Policy.

**Solution:** Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header instead of the Feature-Policy header.

**Evidence:** `Feature-Policy`

---

### [Low] Deprecated Feature Policy Header Set
**Source:** ZAP  
**URL:** http://juiceshop:3000/chunk-VS3A3LTT.js  
**CWE:** CWE-16  

The header has now been renamed to Permissions-Policy.

**Solution:** Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header instead of the Feature-Policy header.

**Evidence:** `Feature-Policy`

---

### [Low] Deprecated Feature Policy Header Set
**Source:** ZAP  
**URL:** http://juiceshop:3000/sitemap.xml  
**CWE:** CWE-16  

The header has now been renamed to Permissions-Policy.

**Solution:** Ensure that your web server, application server, load balancer, etc. is configured to set the Permissions-Policy header instead of the Feature-Policy header.

**Evidence:** `Feature-Policy`

---

### [Low] Timestamp Disclosure - Unix
**Source:** ZAP  
**URL:** http://juiceshop:3000  
**CWE:** CWE-497  

A timestamp was disclosed by the application/web server. - Unix

**Solution:** Manually confirm that the timestamp data is not sensitive, and that the data cannot be aggregated to disclose exploitable patterns.

**Evidence:** `1666666667`

---

### [Low] Timestamp Disclosure - Unix
**Source:** ZAP  
**URL:** http://juiceshop:3000/sitemap.xml  
**CWE:** CWE-497  

A timestamp was disclosed by the application/web server. - Unix

**Solution:** Manually confirm that the timestamp data is not sensitive, and that the data cannot be aggregated to disclose exploitable patterns.

**Evidence:** `1666666667`

---

### [Low] Timestamp Disclosure - Unix
**Source:** ZAP  
**URL:** http://juiceshop:3000/styles.css  
**CWE:** CWE-497  

A timestamp was disclosed by the application/web server. - Unix

**Solution:** Manually confirm that the timestamp data is not sensitive, and that the data cannot be aggregated to disclose exploitable patterns.

**Evidence:** `1528301887`

---

### [Info] Modern Web Application
**Source:** ZAP  
**URL:** http://juiceshop:3000  
**CWE:** CWE--1  

The application appears to be a modern web application. If you need to explore it automatically then the Ajax Spider may well be more effective than the standard one.

**Solution:** This is an informational alert and so no changes are required.

**Evidence:** `<script>
    window.addEventListener("load", function(){
      window.cookieconsent.initialise({
        "palette": {
          "popup": { "background": "var(--theme-primary)", "text": "var(--theme-text)" },
          "button": { "background": "var(--theme-accent)", "text": "var(--theme-text)" }
        },
        "theme": "classic",
        "position": "bottom-right",
        "content": { "message": "This website uses fruit cookies to ensure you get the juiciest tracking experience.", "dismiss": "Me want it!", "link": "But me wait!", "href": "https://www.youtube.com/watch?v=9PnbKL3wuH4" }
      })});
  </script>`

---

### [Info] Modern Web Application
**Source:** ZAP  
**URL:** http://juiceshop:3000/  
**CWE:** CWE--1  

The application appears to be a modern web application. If you need to explore it automatically then the Ajax Spider may well be more effective than the standard one.

**Solution:** This is an informational alert and so no changes are required.

**Evidence:** `<script>
    window.addEventListener("load", function(){
      window.cookieconsent.initialise({
        "palette": {
          "popup": { "background": "var(--theme-primary)", "text": "var(--theme-text)" },
          "button": { "background": "var(--theme-accent)", "text": "var(--theme-text)" }
        },
        "theme": "classic",
        "position": "bottom-right",
        "content": { "message": "This website uses fruit cookies to ensure you get the juiciest tracking experience.", "dismiss": "Me want it!", "link": "But me wait!", "href": "https://www.youtube.com/watch?v=9PnbKL3wuH4" }
      })});
  </script>`

---

### [Info] Modern Web Application
**Source:** ZAP  
**URL:** http://juiceshop:3000/juice-shop/build/routes/fileServer.js:53:13  
**CWE:** CWE--1  

The application appears to be a modern web application. If you need to explore it automatically then the Ajax Spider may well be more effective than the standard one.

**Solution:** This is an informational alert and so no changes are required.

**Evidence:** `<script>
    window.addEventListener("load", function(){
      window.cookieconsent.initialise({
        "palette": {
          "popup": { "background": "var(--theme-primary)", "text": "var(--theme-text)" },
          "button": { "background": "var(--theme-accent)", "text": "var(--theme-text)" }
        },
        "theme": "classic",
        "position": "bottom-right",
        "content": { "message": "This website uses fruit cookies to ensure you get the juiciest tracking experience.", "dismiss": "Me want it!", "link": "But me wait!", "href": "https://www.youtube.com/watch?v=9PnbKL3wuH4" }
      })});
  </script>`

---

### [Info] Modern Web Application
**Source:** ZAP  
**URL:** http://juiceshop:3000/juice-shop/node_modules/express/lib/router/index.js:328:13  
**CWE:** CWE--1  

The application appears to be a modern web application. If you need to explore it automatically then the Ajax Spider may well be more effective than the standard one.

**Solution:** This is an informational alert and so no changes are required.

**Evidence:** `<script>
    window.addEventListener("load", function(){
      window.cookieconsent.initialise({
        "palette": {
          "popup": { "background": "var(--theme-primary)", "text": "var(--theme-text)" },
          "button": { "background": "var(--theme-accent)", "text": "var(--theme-text)" }
        },
        "theme": "classic",
        "position": "bottom-right",
        "content": { "message": "This website uses fruit cookies to ensure you get the juiciest tracking experience.", "dismiss": "Me want it!", "link": "But me wait!", "href": "https://www.youtube.com/watch?v=9PnbKL3wuH4" }
      })});
  </script>`

---

### [Info] Modern Web Application
**Source:** ZAP  
**URL:** http://juiceshop:3000/sitemap.xml  
**CWE:** CWE--1  

The application appears to be a modern web application. If you need to explore it automatically then the Ajax Spider may well be more effective than the standard one.

**Solution:** This is an informational alert and so no changes are required.

**Evidence:** `<script>
    window.addEventListener("load", function(){
      window.cookieconsent.initialise({
        "palette": {
          "popup": { "background": "var(--theme-primary)", "text": "var(--theme-text)" },
          "button": { "background": "var(--theme-accent)", "text": "var(--theme-text)" }
        },
        "theme": "classic",
        "position": "bottom-right",
        "content": { "message": "This website uses fruit cookies to ensure you get the juiciest tracking experience.", "dismiss": "Me want it!", "link": "But me wait!", "href": "https://www.youtube.com/watch?v=9PnbKL3wuH4" }
      })});
  </script>`

---

### [Info] Storable and Cacheable Content
**Source:** ZAP  
**URL:** http://juiceshop:3000/robots.txt  
**CWE:** CWE-524  

The response contents are storable by caching components such as proxy servers, and may be retrieved directly from the cache, rather than from the origin server by the caching servers, in response to similar requests from other users. If the response data is sensitive, personal or user-specific, this may result in sensitive information being leaked. In some cases, this may even result in a user gaining complete control of the session of another user, depending on the configuration of the caching components in use in their environment. This is primarily an issue where "shared" caching servers such as "proxy" caches are configured on the local network. This configuration is typically found in corporate or educational environments, for instance.

**Solution:** Validate that the response does not contain sensitive, personal or user-specific information. If it does, consider the use of the following HTTP response headers, to limit, or prevent the content being stored and retrieved from the cache by another user:Cache-Control: no-cache, no-store, must-revalidate, privatePragma: no-cacheExpires: 0This configuration directs both HTTP 1.0 and HTTP 1.1 compliant caching servers to not store the response, and to not retrieve the response (without validation) from the cache, in response to a similar request.

---

### [Info] Storable but Non-Cacheable Content
**Source:** ZAP  
**URL:** http://juiceshop:3000/assets/public/favicon_js.ico  
**CWE:** CWE-524  

The response contents are storable by caching components such as proxy servers, but will not be retrieved directly from the cache, without validating the request upstream, in response to similar requests from other users.

**Evidence:** `max-age=0`

---

### [Info] Storable but Non-Cacheable Content
**Source:** ZAP  
**URL:** http://juiceshop:3000/chunk-5K74DZ2F.js  
**CWE:** CWE-524  

The response contents are storable by caching components such as proxy servers, but will not be retrieved directly from the cache, without validating the request upstream, in response to similar requests from other users.

**Evidence:** `max-age=0`

---

### [Info] Storable but Non-Cacheable Content
**Source:** ZAP  
**URL:** http://juiceshop:3000/chunk-PX7UKXVL.js  
**CWE:** CWE-524  

The response contents are storable by caching components such as proxy servers, but will not be retrieved directly from the cache, without validating the request upstream, in response to similar requests from other users.

**Evidence:** `max-age=0`

---

### [Info] Storable but Non-Cacheable Content
**Source:** ZAP  
**URL:** http://juiceshop:3000/chunk-VS3A3LTT.js  
**CWE:** CWE-524  

The response contents are storable by caching components such as proxy servers, but will not be retrieved directly from the cache, without validating the request upstream, in response to similar requests from other users.

**Evidence:** `max-age=0`

---

### [Info] Storable but Non-Cacheable Content
**Source:** ZAP  
**URL:** http://juiceshop:3000/styles.css  
**CWE:** CWE-524  

The response contents are storable by caching components such as proxy servers, but will not be retrieved directly from the cache, without validating the request upstream, in response to similar requests from other users.

**Evidence:** `max-age=0`

---
