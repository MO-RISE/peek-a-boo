# peek-a-boo
Simple dockerized service exposing a videofeed through WebRTC via a HTTP frontend. Utilizes [WebGearRTC](https://abhitronix.github.io/vidgear/latest/gears/webgear_rtc/overview/) from [VidGear](https://abhitronix.github.io/vidgear/latest/). Automatically built as a docker image on release. The image is available from here: https://github.com/orgs/MO-RISE/packages

Example setup:
```yaml
version: '3'
services:

  peek-a-boo:
    image: "ghcr.io/mo-rise/peek-a-boo"
    ports:
      - 8000:8000
    environment:
      - SOURCE=rtsp://rtsp.stream/pattern
      - FRAME_SIZE_REDUCTION=50
      - LOG_LEVEL=DEBUG
```

Head to http://localhost:8000 which should yield:

![](screenshot.PNG)
