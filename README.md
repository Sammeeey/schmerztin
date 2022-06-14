## resources
### scrapy / manual approach
- https://hashes.com/en/tools/hash_identifier helped me to identify that the encryption type is base64
- [How to decode base64 in Python](https://stackoverflow.com/a/25487483)

### Playwright approach
- [use telegram-send library](https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580) to send notificatoins in case of earlier appointment
#### Deployment
- general structure derived from [heroku-playwright-example](https://github.com/playwright-community/heroku-playwright-example) (which is based on the [heroku-playwright-buildpack](https://github.com/playwright-community/heroku-playwright-buildpack))
- [official Docker Runtime and Image](https://github.com/microsoft/playwright-python/issues/1215#issuecomment-1073766201) can be used to run playwright-python on Heroku
- Dockerfile derived from [Docker Python Language Guide](https://docs.docker.com/language/python/build-images/#create-a-dockerfile-for-pythonhttps://docs.docker.com/language/python/build-images/#create-a-dockerfile-for-python)
- add lines for local testing in Dockerfile based on [Herokus *Testing image locally*](https://devcenter.heroku.com/articles/container-registry-and-runtime#testing-an-image-locally)
    - best practice `CMD` from link to examplary Dockerfile

## non-resources
### scrapy / manual approach
- in https://stackoverflow.com/a/17606452 suggested https://github.com/blackploit/hash-identifier didn't work since it seems not to cover base64
- https://github.com/psypanda/hashID does [not find the correct base64 type](https://github.com/psypanda/hashID/issues/52) (although base64 seems to be supported)

## base 64 hashes (delivering possible appointments)
### 22-06-13_12-20
W1t7ImlkIjoiUHJheGlzRELCpygwOjAtMzMwODI0IzAsIDI3NSlfUHJheGlzRELCpygwOjAtMzAwMzk4IzAsIDQyMSkiLCJleElkIjoiUHJheGlzRELCpygwOjAtMzMwODI0IzAsIDI3NSkiLCJuYW1lIjoiVGVybWluZSBmw7xyIE5ldXBhdGllbnRlbiBEci4gUGlvY2giLCJ2aWRlb0FwcG9pbnRtZW50IjpmYWxzZSwiaW5zdGl0dXRpb25JZCI6IjZhMzQwODgwLTU4OGEtNGZlMC1hMDY0LWM5NjIyMmJmOTM5NiIsInBoeXNpY2lhbklkIjoiUHJheGlzRELCpygwOjAtMzAwMzk4IzAsIDQyMSkiLCJwaHlzaWNpYW5FeElkIjoiUHJheGlzRELCpygwOjAtMzAwMzk4IzAsIDQyMSkiLCJwaHlzaWNpYW5OYW1lIjoiRHIuIFBpb2NoIiwicHJvcG9zYWxzUGVySG91ciI6MCwicHJvcGVydGllcyI6e319XSwiMjAyMi0wOC0xMyIsMjkse30sIjIwMjItMDktMTEiLG51bGwsbnVsbCxudWxsXQ==

## possible approach to request available appointments
- imitate a POST request with data similar to `dec_pr3.json`
    - try to cover larger time span between requested dates
    - use Pythons base64 built-in module to encode respective data and send it as `data` in the body of POST request (see `posix_curl_command.py`)

## possible approach with Playwright
- use JavaScript capable framework (Playwright) along with (headless) browser to request and navigate in target page
- get (unclean) information from automatically rendered page (just like in normal browser)
- send telegram notification as soon as earlier appointment (compared to currently booked one) is available
