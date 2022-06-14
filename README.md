## resources
### Playwright approach
- [use telegram-send library](https://medium.com/@robertbracco1/how-to-write-a-telegram-bot-to-send-messages-with-python-bcdf45d0a580) to send notifications in case of earlier appointment
#### Deployment
- general structure derived from [heroku-playwright-example](https://github.com/playwright-community/heroku-playwright-example) (which is based on the [heroku-playwright-buildpack](https://github.com/playwright-community/heroku-playwright-buildpack))
- [official Docker Runtime and Image](https://github.com/microsoft/playwright-python/issues/1215#issuecomment-1073766201) can be used to run playwright-python on Heroku
- Dockerfile derived from [Docker Python Language Guide](https://docs.docker.com/language/python/build-images/#create-a-dockerfile-for-pythonhttps://docs.docker.com/language/python/build-images/#create-a-dockerfile-for-python)
- add lines for local testing in Dockerfile based on [Herokus *Testing image locally*](https://devcenter.heroku.com/articles/container-registry-and-runtime#testing-an-image-locally)
    - best practice `CMD` from link to examplary Dockerfile

## non-resources


## possible approach with Playwright
- use JavaScript capable framework (Playwright) along with (headless) browser to request and navigate in target page
- get (unclean) information from automatically rendered page (just like in normal browser)
- send telegram notification as soon as earlier appointment (compared to currently booked one) is available
